"""PurchaseSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
# Используйте include() чтобы добавлять URL из каталога приложения
from django.urls import include
from django.urls import path
# Добавьте URL соотношения, чтобы перенаправить запросы с корневового URL, на URL приложения
from django.views.generic import RedirectView
# Используйте static() чтобы добавить соотношения для статических файлов
# Только на период разработки
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('purchase/', include('purchase.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/purchase/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    prefix_default_language=False
)

admin.site.index_title = _('АдминПанель. Закупки')
admin.site.site_header = _('Поддержка электронных закупок')
admin.site.site_title = _('Управление сайтом')
