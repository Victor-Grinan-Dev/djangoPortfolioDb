from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from .validations import validate_icon_image_size, validate_image_file_extensions

def server_icon_upload(instance, filename):
    return f"server/{instance.id}/server_icon/{filename}"

def server_banner_upload(instance, filename):
    return f"server/{instance.id}/server_banner/{filename}"

def category_icon_upload(instance, filename):
    return f"category/{instance.id}/category_icon/{filename}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    icon = models.FileField(
        upload_to=category_icon_upload, 
        null=True, 
        blank=True,
        # validators=[
        #     validate_icon_image_size
        #     ]
        )
    
    def save(self, *args, **kwargs):
        """keep only one icon per category"""
        if self.id:
            existing = get_object_or_404(Category, id=self.id)
            if existing.icon != self.icon:
                existing.icon.delete(save=False)
        super(Category, self).save(*args, **kwargs)

    @receiver(models.signals.pre_delete, sender="chat_server.Category")
    def category_delete_files(sender, instance, **kwargs):
        """if the category gets deleted will also the icon"""
        for field in instance._meta.fields:
            if field.name == "icon":
                file = getattr(instance, field.name)
                if file:
                    file.delete(save=False) 

    def __str__(self):
        return self.name
    

class Server(models.Model):
    name = models.CharField(max_length=100)
    #on_delete=models.CASCADE read documentation to find out what todo on delete:
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="server_owner")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="server_category")
    description = models.CharField(max_length = 255, blank=True, null=True)
    member = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name

class Channel(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="channel_owner")
    topic = models.CharField(max_length = 255)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name="channel_server")

    banner = models.ImageField(
        upload_to=server_banner_upload, 
        null=True, 
        blank=True, 
        validators=[
            validate_image_file_extensions
            ]
        )
    icon = models.ImageField(
        upload_to=server_icon_upload, 
        null=True, 
        blank=True, 
        validators=[
            validate_icon_image_size, 
            validate_image_file_extensions
            ]
        )

    def save(self, *args, **kwargs):
        """keep only one icon per channel"""
        if self.id:
            existing = get_object_or_404(Channel, id=self.id)
            if existing.icon != self.icon:
                existing.icon.delete(save=False)
            if existing.banner != self.banner:
                existing.banner.delete(save=False)
        # super(Channel, self).save(*args, **kwargs)
        super(Channel, self).save(*args, **kwargs)

    @receiver(models.signals.pre_delete, sender="chat_server.Server")
    def category_delete_files(sender, instance, **kwargs):
        """if the category gets deleted will also the icon"""
        for field in instance._meta.fields:
            if field.name == "icon" or field.name == "banner":
                file = getattr(instance, field.name)
                if file:
                    file.delete(save=False) 

    def __str__(self):
        return self.name