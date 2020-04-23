from django.db import models
from django.urls import reverse

class Conversation(models.Model):
	name = models.CharField(max_length=120)
	owner_id = models.ForeignKey('auth.User',on_delete=models.CASCADE) #talk

	def get_absolute_url(self):
		return reverse("conversations:converation-detail", kwargs={"id":self.id})