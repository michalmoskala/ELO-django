from django.db import models
from django.urls import reverse

class Membership(models.Model):
	conversation_id = models.ForeignKey('conversations.Conversation', on_delete=models.CASCADE)
	user_id = models.ForeignKey('auth.User',on_delete=models.CASCADE)