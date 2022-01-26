from django.urls import path
from django.views.generic import RedirectView
from transaccionesInventarios import views as modelViews

transaccionesInv_patterns = ([
    path('',                modelViews.baseListView.as_view(),  name="Base"),
    path('add',             modelViews.Add,                     name="Add"),
    path('add/<int:pk>/',   modelViews.AddInventory,            name="AddInventory"),
    path('deduct',          modelViews.Deduce,                  name="Deduct"),
    path('deduct/<int:pk>/',modelViews.DeduceInventory,         name="DeductInventory"),
    path('search',          modelViews.Search,                  name='Search'),
    path('save',            modelViews.SaveTransaction,         name='Save'),
    path('getTransaction',  modelViews.getTransaction,          name='getTransaction'),
    path('<int:pk>',        modelViews.showTransaction,         name="showTransaction"),
], "TransaccionesInv")