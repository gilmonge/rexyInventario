from django.urls import path
from django.views.generic import RedirectView
from bodegas import views as modelViews

bodegas_patterns = ([
    path('',                modelViews.baseListView.as_view(),name="Base"),
    path('add',             modelViews.CreateView.as_view(),  name="Add"),
    path('edit/<int:pk>',   modelViews.UpdateView.as_view(),  name="Edit"),
    path('del/<int:pk>',    modelViews.DeleteView.as_view(),  name="Delete"),
    path('search',          modelViews.Search,                name='Search'),
], "Bodegas")