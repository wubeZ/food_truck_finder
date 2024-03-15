from django.core.management.base import BaseCommand
from utils.import_csv_to_mongodb import import_csv_to_mongodb

class Command(BaseCommand):
    help = 'Import data from CSV file to MongoDB'

    def handle(self, *args, **kwargs):
        
        csv_file_path = './data/food-truck-data.csv'
        import_csv_to_mongodb(csv_file_path)
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        return
