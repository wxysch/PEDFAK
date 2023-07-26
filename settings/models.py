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

class News(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news_image')
    description = models.TextField()
    created = models.DateTimeField()
    
    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Slider(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='slider')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='announcement_image')
    description = models.TextField()
    created = models.DateTimeField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'ОБЪЯВЛЕНИЕ'
        verbose_name_plural = 'ОБЪЯВЛЕНИЯ'

class Video(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='poster/')
    video = models.FileField(upload_to='video/')
    created = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

class Albums(models.Model):
    title = models.CharField(max_length=255)
    album = models.ImageField(upload_to='album/')
    created = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

class Appeal(models.Model):
    fio = models.CharField(max_length=255)
    email = models.EmailField(null=True,blank=True)
    description = models.TextField()

    def __str__(self):
        return self.fio
    
    class Meta:
        verbose_name = 'ОБРАЩЕНИЕ'
        verbose_name_plural = 'ОБРАЩЕНИЯ'