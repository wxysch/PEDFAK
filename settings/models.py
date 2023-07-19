from django.db import models

# Create your models here.

class Contacts(models.Model):
    title = models.CharField(max_length=255)
    line = models.TextField()
    fontawesome = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

class Settings(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logo')
    contacts = models.TextField()
    press_service = models.TextField()
    selection_committee = models.TextField()
    vk = models.URLField(null=True,blank=True)
    twitter = models.URLField(null=True,blank=True)
    instagram = models.URLField(null=True,blank=True)
    facebook = models.URLField(null=True,blank=True)
    youtube = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

