from django.db import models
from django.conf import settings

def category_icon_upload(instance, filename):
    return f"category/{instance.id}/category_icon/{filename}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    icon = models.FileField(upload_to=category_icon_upload, null=True, blank=True)
    def __str__(self):
        return self.name
    

class Server(models.Model):
    name = models.CharField(max_length=100)
    #on_delete=models.CASCADE read documentation to find out what todo on delete:
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="server_owner")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="server_category")
    description = models.CharField(max_length = 255, blank=True, null=True)
    member = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True)

    def __str__(self):
        return self.name

class Channel(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="channel_owner")
    topic = models.CharField(max_length = 255)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name="channel_server")

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Channel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name