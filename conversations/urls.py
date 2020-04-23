from django.urls import path
from .views import ConversationDetailView

app_name = 'conversations'
urlpatterns = [
	path('<int:id>/',ConversationDetailView,name='convo'),
	path('aaa/<int:id>/',ConversationDetailView,name='convo')
	]