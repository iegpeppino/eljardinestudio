from django.shortcuts import render
from .models import Contact, Home, Profile, About, Category, Services, Portfolio, Slider_About

def index(request):
    #Uso el contexto para mandar el contenido del model Home
    #mas actual a la página estática

    home = Home.objects.latest('updated')
    
    # Se usa la informacion About del perfil
    # mas actual y nos aseguramos que el About
    # sea el que esta ligado al perfil
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)
    categories = Category.objects.all()
    portfolio = Portfolio.objects.all()
    aslide_num = Slider_About.objects.all().count()
    contact = Contact.objects.all()
    services = Services.objects.all()

    context = {
        'home' : home,
        'about': about,
        'profiles' : profiles,
        'services' : services,
        'portfolios' : portfolio,
        'aslide_num' : aslide_num,
        'contact' : contact
        }
                
    return render(request, 'index.html', context)

    # De esta forma renderizo todos los objetos
    # en una sola página 