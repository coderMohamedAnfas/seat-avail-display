# your_app/management/commands/populate_db.py

from django.core.management.base import BaseCommand
from seatavailability.models import Branch, Category

class Command(BaseCommand):
    help = 'Populates the database with default values for branches and categories'

    def handle(self, *args, **kwargs):
        branch_names = [
            'COMPUTER HARDWARE ENGINEERING', 'CIVIL ENGINEERING', 'ELECTRICAL & ELECTRONICS ENGINEERING', 
            'INSTRUMENTATION ENGINEERING', 'MECHANICAL ENGINEERING', 'ELECTRONICS ENGINEERING'
        ]

        category_names = [
            'general', 'thslc', 'vhse', 'ews', 'ezhava', 'muslim', 
            'lc & ai', 'obc', 'obh', 
            'drc', 'vrc', 'krc', 
            'sc', 'sh', 'persons with disabilities'
        ]

        for branch_name in branch_names:
            branch, created = Branch.objects.get_or_create(name=branch_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created branch: {branch_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Branch already exists: {branch_name}'))
                
            for category_name in category_names:
                category, created = Category.objects.get_or_create(branch=branch, name=category_name.upper(), defaults={'availability': 0})
                if created:
                    self.stdout.write(self.style.SUCCESS(f'  Successfully created category: {category_name.upper()} for branch {branch_name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'  Category already exists: {category_name.upper()} for branch {branch_name}'))
