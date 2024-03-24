import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UpTrader.settings')

django.setup()

from menu.models import TreeMenu

data = [
    {
        'name': 'Cars',
        'children': [
            {
                'name': 'Sedans',
                'children': [
                    {'name': 'Toyota Camry'},
                    {'name': 'Honda Accord'},
                    {'name': 'Nissan Altima'},
                    {'name': 'Ford Fusion'}
                ]
            },
            {
                'name': 'SUVs',
                'children': [
                    {'name': 'Toyota RAV4'},
                    {'name': 'Honda CR-V'},
                    {'name': 'Nissan Rogue'},
                    {'name': 'Ford Explorer'}
                ]
            },
            {
                'name': 'Trucks',
                'children': [
                    {'name': 'Ford F-150'},
                    {'name': 'Chevrolet Silverado'},
                    {'name': 'Ram 1500'},
                    {'name': 'GMC Sierra 1500'}
                ]
            }
        ]
    },
    {
        'name': 'Electronics',
        'children': [
            {
                'name': 'Phones',
                'children': [
                    {'name': 'iPhone'},
                    {'name': 'Samsung Galaxy'},
                    {'name': 'Google Pixel'},
                    {'name': 'OnePlus'}
                ]
            },
            {
                'name': 'Laptops',
                'children': [
                    {'name': 'MacBook Pro'},
                    {'name': 'Dell XPS'},
                    {'name': 'HP Spectre'},
                    {'name': 'Lenovo ThinkPad'}
                ]
            },
            {
                'name': 'TVs',
                'children': [
                    {'name': 'Samsung QLED'},
                    {'name': 'LG OLED'},
                    {'name': 'Sony Bravia'},
                    {'name': 'TCL Roku'}
                ]
            }
        ]
    }
]

def create_menu_item(item_data, parent=None):
    item = TreeMenu.objects.create(name=item_data['name'], parent=parent)
    for child_data in item_data.get('children', []):
        create_menu_item(child_data, parent=item)

for item_data in data:
    create_menu_item(item_data)