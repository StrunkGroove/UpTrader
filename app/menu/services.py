import itertools

from django.db.models import Q

from .models import TreeMenu
from .exceptions import Custom404, MenuDoesNotExist, PathDoesNotExist


class MenuBuilder:
    """
    A class for building tree menus.
    """
    
    @classmethod
    def build_menu(cls, requested_url: str, menu_name: str) -> dict[str, any]:
        """
        Draws a menu based on the given requested url and menu name.

        Args:
            requested_url (str): Requested url.
            menu_name (str): The name of the menu to draw.

        Returns:
            dict[str, Any]: A dictionary containing the menu tree and parent path.
        """
        records = cls._get_menu_records(requested_url, menu_name)
        tree = cls._build_tree(records)
        return {'tree': tree, 'parent_path': None}

    @classmethod
    def _get_menu_records(cls, requested_url: str, menu_name: str
                          ) -> list[TreeMenu]:
        name_paths = cls._get_name_paths(requested_url)

        if name_paths == []:
            return cls._get_menu_records_for_index_page(menu_name)
        elif menu_name != name_paths[0]:
            return cls._get_menu_records_for_not_draw_menu(
                menu_name, name_paths[0]
            )
        elif name_paths != [] and menu_name == name_paths[0]:
            return cls._get_menu_records_for_draw_menu(
                menu_name, name_paths
            )

    @staticmethod
    def _get_name_paths(requested_url: str) -> list[str]:
        return [path for path in requested_url.split('/') if path != '']
    
    @staticmethod
    def _get_menu_records_for_index_page(menu_name: str) -> list[TreeMenu]:
        return list(
            TreeMenu.objects.filter(parent__isnull=True, name=menu_name)
        )

    @classmethod
    def _get_menu_records_for_not_draw_menu(cls, menu_name: str, first_path: str
                                            ) -> list[TreeMenu]:
        """
        Gets menu record for building a menu and checks if the first 
        path exists in the database. If first path not in db it means 
        that the user is asking to draw a menu that is not in the db.

        Args:
            menu_name (str): The name of the menu to draw.
            first_path (str): The first path in requested url.

        Returns:
            list[TreeMenu]: The menu records.

        Raises:
            Custom404: If the first path in url does not exist in the database.
        """
        records = list(
            TreeMenu.objects.filter(
                Q(parent__isnull=True, name=menu_name) |
                Q(parent__isnull=True, name=first_path)
            )
        )

        try:
            cls._check_menu_exist(records, first_path)
        except MenuDoesNotExist:
            raise Custom404()
        return records

    @staticmethod
    def _check_menu_exist(records: list[TreeMenu], firs_path: str) -> None:
        """
        Checks if the first path exists in the menu records and removes it from the list.

        Args:
            records (List[TreeMenu]): The menu records to check.
            first_path (str): The first path to check.

        Raises:
            MenuDoesNotExist: If the first path does not exist in the menu records.
        """
        for i, record in enumerate(records):
            if record.name == firs_path:
                records.pop(i)
                return
        raise MenuDoesNotExist()
    
    @classmethod
    def _get_menu_records_for_draw_menu(cls, menu_name: str, name_paths: list[str]
                                            ) -> list[TreeMenu]:
        records = list(
            TreeMenu.objects \
                .filter(
                    Q(parent__isnull=True, name=menu_name) | 
                    Q(parent__name__in=name_paths),
                    depth__lte=len(name_paths) + 1,
                ) \
                .select_related('parent') \
                .order_by('depth')
            )
        
        try:
            cls._check_path_exists(records, name_paths)
        except PathDoesNotExist:
            raise Custom404()
        return records

    @classmethod
    def _check_path_exists(cls, records: list[TreeMenu], current_path: list[str]
                           ) -> None:
        if current_path == []: return
        for record in records:
            if record.name == current_path[0]:
                return cls._check_path_exists(records, current_path[1:])
        raise PathDoesNotExist()

    @classmethod
    def _build_tree(cls, records: list[TreeMenu]) -> dict[TreeMenu, dict]:
        grouped_records = cls._group_records(records)
        tree = cls._recursive_build_tree(grouped_records)
        return tree

    @staticmethod
    def _group_records(records: list[TreeMenu]
                       ) -> dict[TreeMenu, list[TreeMenu]]:
        grouped_records = itertools.groupby(records, key=lambda x: x.parent)
        return {parent: list(group) for parent, group in grouped_records}

    @classmethod
    def _recursive_build_tree(cls, nodes: dict[TreeMenu, list[TreeMenu]], 
                              parent=None) -> dict[TreeMenu, dict]:
        tree = {}
        for node in sorted(nodes.get(parent, []), key=lambda x: x.name):
            tree[node] = cls._recursive_build_tree(nodes, node)
        return tree