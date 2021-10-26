from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.db.models.fields import CharField, TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length= 50)
    title = models.CharField(max_length= 40, null= True)
    logo = models.ImageField(upload_to= 'image/', null= True)
    text = models.TextField(max_length= 500, null= True)
    updated = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name

class About(models.Model):
    heading = models.CharField(max_length= 50)
    subheading = models.CharField(max_length=50, null=True, default='subtitulo')
    description_1 = models.TextField(max_length= 300, null= True)
    description_2 = models.TextField(max_length= 300, null= True, blank= True)
    main_img = models.ImageField(upload_to= 'image/', null= True)
    # Indica que es la informacion actual del modelo
    updated = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.heading

    #Create a photo slideshow showing what your business is about
class Slider_About(models.Model):
    about = models.ForeignKey(About, on_delete= models.CASCADE)
    title = models.CharField(max_length= 50)
    photo = ImageField(upload_to= 'image/')

    def __str__(self):
        return self.title

class Contact(models.Model):
    title = models.CharField(max_length= 50, null= True, default= 'Contact')
    subtitle = models.CharField(max_length= 100, null= True, default= 'Our Social Links')
    wsp_number = models.CharField(max_length= 50, null= True, blank= True)

    def __str__(self):
        return self.title
    

    #Class to make cards with contact links to your social networks
    # or to business associates
class ContactCard(models.Model):
    contact = models.ForeignKey(Contact, on_delete= models.CASCADE,null= True)
    title = models.CharField(max_length= 50, null= True)
    main_img = models.ImageField(null= True)
    description = models.TextField(max_length= 300, null= True)
    url = models.CharField(max_length= 100, null= True)
    net_color = models.CharField(max_length= 10, default="#5bc0de")

    def __str__(self):
        return self.title

class AssociateCard(models.Model):
    contact = models.ForeignKey(Contact, on_delete= models.CASCADE,null= True)
    title = models.CharField(max_length= 50, null= True)
    main_img = models.ImageField(null= True)
    description = models.TextField(max_length= 300, null= True)
    url = models.CharField(max_length= 100, null= True)
    
    def __str__(self):
        return self.title

    #Showcase your employees or associates making cards with their info
    # using this model
class Profile(models.Model):
    about = models.ForeignKey(About, on_delete= models.CASCADE)
    nombre_jardinero = models.CharField(max_length= 50)
    acerca = models.TextField(max_length= 100, null= True)
    social_link = models.URLField(max_length= 200, null= True, blank= True)
    profile_img = models.ImageField(upload_to= 'profile/')

    #Provided services categories and their description
  
class Services(models.Model):
    title = models.CharField(max_length=10, null= True)
    header = models.CharField(max_length=50, null= True)
    subheader = models.CharField(max_length=100, null= True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "services"


class Category(models.Model):
    services = models.ForeignKey(Services, on_delete=models.CASCADE, null= True)
    title = models.CharField(max_length=30, default='servicio que se brinda', null= True)
    description = models.TextField(max_length=300, default='descripcion del servicio', null= True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"    

class Slider_Services(models.Model):
    services = models.ForeignKey(Services, on_delete= models.CASCADE, null= True)
    title = models.CharField(max_length= 50, null= True)
    photo = ImageField(upload_to= 'image/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "slider_services"      

class Facility(models.Model):
    services = models.ForeignKey(Services, on_delete= models.CASCADE, null= True)
    title = models.CharField(max_length= 30, default= 'instalaciones como equipo y salas de ensayo', null= True)
    description = models.TextField(max_length= 300, default= 'describir instalaciones y equipo del estudio', null= True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "facilities"  

class Slider_Facility(models.Model):
    services = models.ForeignKey(Services, on_delete= models.CASCADE, null= True)
    title = models.CharField(max_length= 50, null= True)
    photo = ImageField(upload_to= 'image/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Slider_Facilities"

    #Present your work with this portfolio    
class Portfolio(models.Model):
    title = models.CharField(max_length= 50, null= True)
    description = models.TextField(max_length= 300, null= True)

    def __str__(self):
        return self.title
   
    #Add embeded spotify or youtube players showcasing
    # the studio's works along photos and description
class Spotify_Single(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete= models.CASCADE, null= True)
    title = models.CharField(max_length= 50, default='nombre de cancion')
    artist_name = models.CharField(max_length=50, default='artista')
    spotify_url = models.CharField(max_length= 50)
    description = models.TextField(max_length= 100,null= True)
    artist_img = models.ImageField(null= True, upload_to='image/', blank= True)

    def __str__(self):
        return self.title

class Spotify_Playlist(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete= models.CASCADE, null= True)
    title = models.CharField(max_length= 50, default='nombre de playlist')
    spotify_url = models.CharField(max_length= 50)
    description = models.TextField(max_length= 100, null= True)
    artist_img = models.ImageField(null= True, upload_to= 'image/', blank= True)

    def __str__(self):
        return self.title

class Spotify_Album(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete= models.CASCADE, null= True)
    title = models.CharField(max_length= 50, default='nombre de album')
    artist_name = models.CharField(max_length=50, default='artista')
    spotify_url = models.CharField(max_length= 50)
    description = models.TextField(max_length= 100,null= True)
    artist_img = models.ImageField(null= True, upload_to='image/', blank= True)

    def __str__(self):
        return self.title

class Youtube_Video(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete= models.CASCADE, null= True)
    title = models.CharField(max_length= 50, default='nombre de cancion')
    artist_name = models.CharField(max_length=50, default='artista')
    youtube_url = models.CharField(max_length= 50)
    description = models.TextField(max_length= 100, null= True)
    artist_img = models.ImageField(null= True, upload_to= 'image/',  blank= True)

    def __str__(self):
        return self.title