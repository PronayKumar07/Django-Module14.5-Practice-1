from django.db import models

# Create your models here.
class PracticeModel(models.Model):
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    float_field = models.FloatField()
    generic_ip_address_field = models.GenericIPAddressField()
    integer_field = models.IntegerField()
    json_field = models.JSONField()
    slug_field = models.SlugField()
    text_field = models.TextField()
    time_field = models.TimeField()
    url_field = models.URLField()
    uuid_field = models.UUIDField()
