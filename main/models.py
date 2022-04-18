from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q
from django.urls import reverse

from accounts.models import CustomUser


class RoomManager(models.Manager):
    use_for_related_fields = True

    def search(self, query=None):
        qs = self.get_queryset()
        if query:
            or_lookup = (Q(title__icontains=query) | Q(adres__icontains=query))
            qs = qs.filter(or_lookup)

        return qs



class Room(models.Model):
    title = models.CharField('Название', max_length=50)
    adres = models.CharField('Адрес', max_length=100)
    usphone =models.CharField('Телефон', max_length=20)
    discript = models.TextField('Описание')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    objects = RoomManager()

    def get_absolute_url(self):
        return reverse('room_details', args=[str(self.id)])


class Image(models.Model):
    condo = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(upload_to="images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)




