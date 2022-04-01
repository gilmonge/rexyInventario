from django.urls import path
from django.views.generic import RedirectView
from inventarios import views as modelViews

inventarios_patterns = ([
    path('',                modelViews.baseListView.as_view(),name="Base"),
    path('add',             modelViews.CreateView.as_view(),  name="Add"),
    path('edit/<int:pk>',   modelViews.UpdateView.as_view(),  name="Edit"),
    path('del/<int:pk>',    modelViews.DeleteView.as_view(),  name="Delete"),
    path('search',          modelViews.Search,                name='Search'),
    path('getProduct',      modelViews.GetProduct,            name='GetProductAjax'),
    path('addProduct',      modelViews.AddProduct,            name='AddProductAjax'),
    path('export',          modelViews.exportExcel,           name="exportExcel"),
], "Inventarios")