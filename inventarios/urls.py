from django.urls import path
from django.views.generic import RedirectView
from inventarios import views as inventariosViews

inventarios_patterns = ([
    path('',                inventariosViews.baseListView.as_view(),name="Base"),
    path('add',             inventariosViews.CreateView.as_view(),  name="Add"),
    path('edit/<int:pk>',   inventariosViews.UpdateView.as_view(),  name="Edit"),
    path('del/<int:pk>',    inventariosViews.DeleteView.as_view(),  name="Delete"),
    path('search',          inventariosViews.Search,                name='Search'),
], "Inventarios")