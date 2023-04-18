from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('<int:id>',views.details,name='details'),
    path('load/',views.load_more,name='load'),
    path('sports/',views.load_Sports,name='sports'),
    path('politics/',views.load_Politics,name='politics'),
    path('business/',views.load_Business,name='business'),
    path('crime/',views.load_Crime,name='crime'),
    path('entertainment/',views.load_Entertainment,name='entertainment'),
    path('international/',views.load_International,name='international'),

    path('help/',views.help,name='help'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),

    path('loadSearch/',views.loadSearch,name='loadSearch'),
    
]
