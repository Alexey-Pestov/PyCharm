from django.db import models

class Advertisement(models.Model):
    title = models.CharField('заголовок', max_length=128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'advertisements'

    # для переименования прописываем код со странички https://django.fun/ru/docs/django-orm-cookbook/2.0/table_name/
    # затем python manage.py makemigrations
    # наконец, python manage.py migrate


    def __str__(self):
        return f'{__class__.__name__}(id={self.id}, title={self.title}, price={self.price})'

    # https://stackoverflow.com/questions/45483417/what-is-doing-str-function-in-django
    # from app_adv.models import Advertisement
    # queryset = Advertisement.objects.all()
    # queryset[0]


