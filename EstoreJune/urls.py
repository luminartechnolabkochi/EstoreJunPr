"""EstoreJune URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# url: localhost:8000/products
# method:get

# url: localhost:8000/products
# method post
# data={book_name:"randamoozham",author:"mt",price:450,publisher:"abc"}


from django.contrib import admin
from django.urls import path
# from api.views import ProductsView,MorningView,EveningView,AddView,SubtractionView
# localhost:8000/products
from api.views import CubeView,NumberChkView,WordCountView,\
    ProductsView,ProductDetailsView,ReviewsView,ReviewDetailsView
urlpatterns = [
    path('superuser/', admin.site.urls),
    path("cube",CubeView.as_view()),
    path("numchk",NumberChkView.as_view()),
    path("wordcount",WordCountView.as_view()),
    path("products",ProductsView.as_view()),
    path("products/<int:id>",ProductDetailsView.as_view()),
    path("reviews",ReviewsView.as_view()),
    path("reviews/<int:id>",ReviewDetailsView.as_view())
    # path("products",ProductsView.as_view()),
    # path("morning",MorningView.as_view()),
    # path("evening",EveningView.as_view()),
    # path("add",AddView.as_view()),
    # path("sub",SubtractionView.as_view())

]
