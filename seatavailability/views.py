from django.shortcuts import render
from django.http import JsonResponse
from .models import College, Branch, Category

def seat_availability_view(request):
    colleges = College.objects.all().prefetch_related('branches__categories')
    data = {}

    for college in colleges:
        college_data = {}
        for branch in college.branches.all():
            categories = branch.categories.all().values('name', 'availability')
            college_data[branch.name] = list(categories)
        data[college.name] = college_data

    return JsonResponse(data)

def index_view(request):
    return render(request, 'index.html')

def edit(request):
    colleges = College.objects.all().prefetch_related('branches__categories')
    college_data = []

    for college in colleges:
        branches_data = []
        for branch in college.branches.all():
            categories = branch.categories.all()
            branches_data.append({
                'branch_name': branch.name,
                'categories': categories
            })
        college_data.append({
            'college_name': college.name,
            'branches': branches_data
        })

    return render(request, "edit.html", {'colleges': college_data})

def update_seat_availability(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        availability = request.POST.get('availability')
        try:
            category = Category.objects.get(id=category_id)
            category.availability = availability
            category.save()
            return JsonResponse({'status': 'success'})
        except Category.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Category not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})
