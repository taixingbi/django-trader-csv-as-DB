from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from mysite.core import views

from django.views.generic import TemplateView

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('update/', views.update_view, name='update'),
    path('sell/', views.sell_view, name='sell'),

    #test
    path('version/', views.Demo.version, name='version'),
    path('s3/', views.Demo.s3, name='s3'),
    path('db/', views.Demo.db, name='db'),
    path('ses/', views.Demo.ses, name='ses'),

    #api
    path('api/', include([
        path('ticker/<key>', views.Demo.ticker, name='ticker'),
 
        #path('<key>', views.Demo.demo, name='demo'),
        path('demo/', views.Demo.demo, name='demo'),
    ])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
