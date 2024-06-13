# myproject/urls.py
from seatavailability.views import index_view
from django.urls import path
import views
urlpatterns =[
path("edit_database/",views.edit,name="edit")
]