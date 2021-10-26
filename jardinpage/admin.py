from django.contrib import admin
from .models import (AssociateCard, ContactCard, Contact, Facility, Home, About, Profile, Category,
 Services, Portfolio, Slider_About, Slider_Facility, Slider_Services, Spotify_Playlist, Spotify_Single, Youtube_Video,Spotify_Album)


admin.site.register(Home)

class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 0

class SliderAboutInline(admin.TabularInline):
    model = Slider_About
    extra = 0

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
        SliderAboutInline,
    ]

class SliderServicesInline(admin.TabularInline):
    model = Slider_Services
    extra = 0
    
class SliderFacilityInline(admin.TabularInline):
    model = Slider_Facility
    extra = 0

class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0

class FacilityInline(admin.TabularInline):
    model = Facility
    extra = 0

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
        FacilityInline,
        SliderFacilityInline,
        SliderServicesInline,

    ]

class SpotySingleInline(admin.TabularInline):
    model = Spotify_Single
    extra = 0

class SpotyListInline(admin.TabularInline):
    model = Spotify_Playlist
    extra = 0

class SpotyAlbumInline(admin.TabularInline):
    model = Spotify_Album
    extra = 0

class YoutubeInline(admin.TabularInline):
    model = Youtube_Video
    extra = 0

class ContactCardInline(admin.TabularInline):
    model = ContactCard
    extra = 0
    
class AssociateCardInline(admin.TabularInline):
    model = AssociateCard
    extra = 0

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [
        ContactCardInline,
        AssociateCardInline
        ]

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [
        SpotyListInline,
        SpotySingleInline,
        SpotyAlbumInline,
        YoutubeInline,
    ]