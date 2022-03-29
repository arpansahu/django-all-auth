from django.contrib import admin
from django.urls import path, include

from .views import (
    HomeClassView,
    account_view,
)

from cruddjangoform.views import (
    home_views,
    delete_item,
    update_item,

)

from error.views import (
    error_404,
    error_400,
    error_500,
    error_403,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeClassView.as_view(), name='home'),

    path('crudformHome', home_views, name="crudformhome"),
    path('crudformdelete/<int:id>/', delete_item, name="curdformdelete"),
    path('crudformupdate/<int:id>/', update_item, name="curdformupdate"),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile', account_view, name='accounts_profile'),


]

handler404 = 'error.views.error_404'
handler500 = 'error.views.error_500'
handler403 = 'error.views.error_403'
handler400 = 'error.views.error_400'
