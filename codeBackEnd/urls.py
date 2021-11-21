from django.urls import path
from django.views.generic import RedirectView
from codeBackEnd import views as codeBackEndViews

codeBackEnd_patterns = ([
    path('', codeBackEndViews.home, name="home"),
    path('onLogin', codeBackEndViews.onLogin, name="onLogin"),
    path('dashboard', codeBackEndViews.dashboard, name="dashboard"),
    path('cuenta', codeBackEndViews.viewPerfil, name="perfil"),
    path('cuenta/Edit', codeBackEndViews.editPerfil, name="perfilInformacionEdit"),
    path('cuenta/passEdit', codeBackEndViews.editPass, name="perfilPassEdit"),
], "codeBackEnd")