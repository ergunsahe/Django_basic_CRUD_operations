from django.urls import path

from .views import home_api, student_list_create_api, student_get_update_delete # student_list_api, student_create_api

urlpatterns = [
    path("home-api/", home_api, name="home"),
    path("list-create-api/", student_list_create_api),
    path("<int:id>/", student_get_update_delete),
    # path("list-api/", student_list_api, name="list"),
    # path("create-api/", student_create_api, name="create"),
]