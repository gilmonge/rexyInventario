from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, authenticate
from usuarios.models import Perfil

# Create your views here.
def home(request):
    return redirect(reverse_lazy('login'))

def dashboard(request):
    if request.user.is_authenticated:
        datos = {}

        """ Comprueba que exite el perfil del usuario y sino lo crea """
        perfil = Perfil.objects.get_or_create(usuario=request.user)[0]
        datos["perfil"] = perfil
        """ Comprueba que exite el perfil del usuario y sino lo crea """

        return render(request, "codeBackEnd/dashboard.html", datos)
    else:
        return redirect('login')

def onLogin(request):
    ErrorRequest = reverse_lazy('login') + "?error"
    if request.method!="POST":
        return redirect(ErrorRequest)
    else:
        # reCaptcha
        if validaReCaptcha(request.POST.get("g-recaptcha-response"))==False:
            return redirect(ErrorRequest)
        # reCaptcha

        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))

        if user is not None:
            login(request, user)
            return redirect('codeBackEnd:dashboard')
        else:
            return redirect(ErrorRequest)

def viewPerfil(request):
    if request.user.is_authenticated:
        # usuarioPerfil = Perfil.objects.filter(usuario=request.user)[0]
        
        datos = {
        #     'usuarioPerfil':usuarioPerfil,
        }

        return render(request, "codeBackEnd/perfil.html", datos)
    else:
        return redirect('login')

def editPerfil(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            usuario = User.objects.filter(id=request.user.id)[0]

            usuario.first_name = request.POST['nombre']
            usuario.last_name = request.POST['apellido']
            usuario.save()

            base_url = reverse('codeBackEnd:perfil')
            query_string =  'ok_perfil'
            url = '{}?{}'.format(base_url, query_string)

            return redirect(url)
        else:
            base_url = reverse('codeBackEnd:perfil')
            query_string =  'error'
            url = '{}?{}'.format(base_url, query_string)

            return redirect('codeBackEnd:perfil')
    else:
        return redirect('login')

def editPass(request):
    ReturnRequest = reverse('codeBackEnd:perfil')
    if request.user.is_authenticated:
        if request.method == "POST":
            
            if request.POST['pass'] == request.POST['confPass']:
                usuario = User.objects.filter(id=request.user.id)[0]
                usuario.set_password(request.POST['pass'])
                usuario.save()

                login(request, usuario)

                base_url = ReturnRequest
                query_string =  'ok_pass'
                url = '{}?{}'.format(base_url, query_string)

                return redirect(url)
            else:
                base_url = ReturnRequest
                query_string =  'error'
                url = '{}?{}'.format(base_url, query_string)

                return redirect(url)
        else:
            base_url = ReturnRequest
            query_string =  'error'
            url = '{}?{}'.format(base_url, query_string)

            return redirect(url)
    else:
        return redirect('login')

def validaReCaptcha(captcha_token):
    # reCaptcha
    import requests
    import json
    from django.conf import settings

    cap_url="https://www.google.com/recaptcha/api/siteverify"
    
    cap_data={
        "secret":settings.RECAPTCHA_PRIVATE,
        "response":captcha_token
    }
    cap_server_response=requests.post(url=cap_url,data=cap_data)
    cap_json=json.loads(cap_server_response.text)

    return cap_json['success']
    # reCaptcha
