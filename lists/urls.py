from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListListView.as_view(), name="index"),
    path("list/<int:list_id>/",views.ItemListView.as_view(), name="todo_list"),
    # CRUD patterns for ToDoLists
    path("list/add/", views.ToDoListCreateView.as_view(), name="list-add"),
    # CRUD patterns for ToDoItems
    path("list/<int:list_id>/item/add/", views.ToDoItemCreateView.as_view(), name="item-add"),
    path("list/<int:list_id>/item/<int:pk>/", views.ItemUpdate.as_view(), name="item-update"),
    path(
        "Delete/list/<int:pk>",
        views.ToDoListDeleteView.as_view(),
        name="list-Delete"
        ),
    path(
        "Delete/list/<int:list_id>/item/<int:pk>",
        views.ToDoItemDeleteView.as_view(),
        name="item-Delete"
        ),
]
