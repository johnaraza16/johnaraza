
from django.conf.urls import url,include
from malnutrition.views import UserView, FoodView, QuestionView, FoodlogView
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('User', UserView)
router.register('Food', FoodView)
router.register('Foodlog', FoodlogView)
router.register('Question', QuestionView)

urlpatterns = [
        url(r'^api/', include(router.urls)),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    

   