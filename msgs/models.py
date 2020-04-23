from django.db import models
from django.urls import reverse

class Msg(models.Model):
	timestamp = models.DateField(auto_now_add=True)
	sender_id = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	receiver_id = models.ForeignKey('conversations.Conversation', on_delete=models.CASCADE)
	content = models.TextField()