from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('main_app.urls'))
]