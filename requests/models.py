from django.db import models
from django.urls import reverse

class Request(models.Model):
	friend_id = models.ForeignKey('auth.User',related_name='requested_friend_id',on_delete=models.CASCADE)
	sender_id = models.ForeignKey('auth.User',related_name='sender_id',on_delete=models.CASCADE)
	status = models.BooleanField(default=False)
	timestamp = models.DateField(auto_now_add=True)
