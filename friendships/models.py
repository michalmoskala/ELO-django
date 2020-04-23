from django.db import models
from django.urls import reverse

class Friendship(models.Model):
	user_id	= models.ForeignKey('auth.User',related_name='friends_user_id',on_delete=models.CASCADE)
	friend_id = models.ForeignKey('auth.User',related_name='friend_id',on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse("friendships:friendship-detail", kwargs={"id":self.id})