from django.shortcuts import render, redirect
from home.forms import CreateNewUserForm, LoginForm
from home.models import User

# def vista_prueba(request, nombre, apellido):
    
#     return render(f'<h2>Que haces {nombre} {apellido}</h2>')


def register_user(request):
    
    if request.method == "POST":
        form = CreateNewUserForm(request.POST)
        
        
        if form.is_valid():
          
            data= form.cleaned_data

            new_user= User(nombre= data['nombre'], apellido=data['apellido'],email=data['email'], contrasenia=data['contrasenia'])
            new_user.save()
            return redirect('inicio')
            
    form= CreateNewUserForm()
    
    return render(request, r'register.html', {'form': form} )


def login_user(request):
    email_register= request.GET.get('email', None)
    
    if email_register:
        user= User.objects.filter(email=email_register)
    else:
        user=None;
        
    form = LoginForm()
    
    
    return render(request,r'login.html',{'user': user, 'form': form} )



def init_home(request):
    
    
    return render(request, r'index.html')
