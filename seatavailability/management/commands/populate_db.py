import os
import django
import myproject.settings
# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from seatavailability.models import College, Branch, Category  # Import models after setting up the environment

# College names
college_names = [
    'College of Engineering', 'Institute of Technology', 'School of Applied Sciences'
]

# Branch names mapped to colleges
college_branches = {
    'College of Engineering': [
        'COMPUTER HARDWARE ENGINEERING', 'CIVIL ENGINEERING', 'ELECTRICAL & ELECTRONICS ENGINEERING'
    ],
    'Institute of Technology': [
        'INSTRUMENTATION ENGINEERING', 'MECHANICAL ENGINEERING', 'ELECTRONICS ENGINEERING'
    ],
    'School of Applied Sciences': [
        'BIOMEDICAL ENGINEERING', 'CHEMICAL ENGINEERING', 'SOFTWARE ENGINEERING'
    ],
}

# Category names
category_names = [
    'general', 'thslc', 'vhse', 'economically weaker sections', 'ezhava', 'muslim', 
    'latin catholic & anglo indian', 'other backward christian', 'other backward hindu', 
    'dheevara & related communities', 'viswakarma & related communities', 'kusavan & related communities', 
    'scheduled caste', 'scheduled tribe', 'persons with disabilities'
]

# Creating colleges, branches, and categories
for college_name in college_names:
    college, created = College.objects.get_or_create(name=college_name)
    if created:
        print(f'Successfully created college: {college_name}')
    else:
        print(f'College already exists: {college_name}')

    branches = college_branches.get(college_name, [])
    for branch_name in branches:
        branch, created = Branch.objects.get_or_create(college=college, name=branch_name)
        if created:
            print(f'  Successfully created branch: {branch_name} for college {college_name}')
        else:
            print(f'  Branch already exists: {branch_name} for college {college_name}')
        
        for category_name in category_names:
            category, created = Category.objects.get_or_create(branch=branch, name=category_name.upper(), defaults={'availability': 20})
            if created:
                print(f'    Successfully created category: {category_name.upper()} for branch {branch_name}')
            else:
                print(f'    Category already exists: {category_name.upper()} for branch {branch_name}')
