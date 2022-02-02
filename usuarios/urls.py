from django.urls import path
from django.views.generic import RedirectView
from usuarios import views as modelViews

usuarios_patterns = ([
    path('',                modelViews.baseListView.as_view(),name="Base"),
    path('add',             modelViews.addUsuario,  name="Add"),
    path('addUser',             modelViews.addPostUsuario,  name="AddUser"),
    path('edit/<int:pk>',   modelViews.viewUsuario,  name="Edit"),
    path('edit/update/<int:pk>',modelViews.editUsuario,  name="Update"),
    path('edit/pass/<int:pk>',modelViews.editUsuarioPass,  name="UpdatePass"),
    path('del/<int:pk>',    modelViews.DeleteView.as_view(),  name="Delete"),
    path('search',          modelViews.Search,                name='Search'),
], "Usuarios")