from django.http import Http404


class Custom404(Http404):
    def __init__(self, message='Page not found! :('):
        self.message = message
        super().__init__(self.message)


class MenuDoesNotExist(Exception):
    def __init__(self, message='Menu does not exists!'):
        self.message = message
        super().__init__(self.message)


class PathDoesNotExist(Exception):
    def __init__(self, message='Path does not exists!'):
        self.message = message
        super().__init__(self.message)