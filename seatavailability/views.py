# seatavailability/views.py
from django.http import JsonResponse
# from .models import SeatAvailability
from django.shortcuts import render

# seatavailability/views.py
from django.http import JsonResponse
from .models import Branch,Category

def seat_availability_view(request):
    branches = Branch.objects.all().prefetch_related('categories')
    data = {}

    for branch in branches:
        categories = branch.categories.all().values('name', 'availability')
        data[branch.name] = list(categories)

    return JsonResponse(data)


def index_view(request):
    return render(request, 'index.html')
# views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import Branch, Category

def edit(request):
    branches = Branch.objects.all().prefetch_related('categories')
    branch_data = []

    for branch in branches:
        categories = branch.categories.all()
        branch_data.append({
            'branch_name': branch.name,
            'categories': categories
        })

    return render(request, "edit.html", {'branches': branch_data})

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
