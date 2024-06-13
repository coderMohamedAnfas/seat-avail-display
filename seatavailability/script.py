# script.py

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from seatavailability.models import Branch, Category  # Import models after setting up the environment

# Branch names
branch_names = [
    'COMPUTER HARDWARE ENGINEERING', 'CIVIL ENGINEERING', 'ELECTRICAL & ELECTRONICS ENGINEERING', 
    'INSTRUMENTATION ENGINEERING', 'MECHANICAL ENGINEERING', 'ELECTRONICS ENGINEERING'
]

# Category names
category_names = [
    'general', 'thslc', 'vhse', 'economically weaker sections', 'ezhava', 'muslim', 
    'latin catholic & anglo indian', 'other backward christian', 'other backward hindu', 
    'dheevara & related communities', 'viswakarma & related communities', 'kusavan & related communities', 
    'scheduled caste', 'scheduled tribe', 'persons with disabilities'
]

# Creating branches and categories
for branch_name in branch_names:
    branch, created = Branch.objects.get_or_create(name=branch_name)
    if created:
        print(f'Successfully created branch: {branch_name}')
    else:
        print(f'Branch already exists: {branch_name}')
        
    for category_name in category_names:
        category, created = Category.objects.get_or_create(branch=branch, name=category_name.upper(), defaults={'availability': 20})
        if created:
            print(f'  Successfully created category: {category_name.upper()} for branch {branch_name}')
        else:
            print(f'  Category already exists: {category_name.upper()} for branch {branch_name}')
