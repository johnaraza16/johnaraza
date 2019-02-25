
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from malnutrition.views import AlgoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('algo', AlgoViewSet, base_name='algo')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('malnutrition.urls')),
    url(r'^test/', view=include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),

]
