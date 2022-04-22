from django.urls import path
from newsletters import views
from .views import newsletter_signup, newsletter_unsubscribe

urlpatterns = [
	path('sign_up', views.newsletter_signup, name="newsletter_signup" ),
	path('unsubscribe', views.newsletter_unsubscribe, name="newsletter_unsubscribe"),
]