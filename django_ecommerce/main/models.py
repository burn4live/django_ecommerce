from django.db import models


class MarketingItem(models.Model):
	img = models.CharField(max_length=255)
	heading = models.CharField(max_length=300)
	caption = models.TextField()
	button_link = models.URLField(null=True, default="register")
	button_title = models.CharField(max_length=20, default="View details")

class StatusReport(models.Model):
	user = models.ForeignKey('payments.User')
	when = models.DateTimeField(blank=True)
	status = models.CharField(max_length=200)

	def save(self, *args, **kwargs):
		from datetime import datetime
		if self.when is None:
			self.when = datetime.now()
		super(StatusReport, self).save(*args, **kwargs)

class Announcement(models.Model):
	when = models.DateTimeField(auto_now=True)
	img = models.CharField(max_length=255, null=True)
	vid = models.URLField(null=True)
	info = models.TextField()

class Badge(models.Model):
	img = models.CharField(max_length=255)
	name = models.CharField(max_length=100)
	desc = models.TextField()

	class Meta:
		ordering = ('name',)