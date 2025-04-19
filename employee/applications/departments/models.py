from xml.etree.ElementTree import tostring

from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField('Name',max_length=50,blank=True) #blank= True (campo vacio), null=True
    short_name = models.CharField('Short Name',max_length=20,unique=True)
    active = models.BooleanField('Active',default=True)
# blank=True
# null=True
# unique=True
# default=True
# editable=True
    class Meta:
        verbose_name = 'My department'
        verbose_name_plural = 'My departments'
        ordering = ['id']
        unique_together = ('name','short_name')

    def __str__(self):
        return str(self.id)  + '-' + self.name + '-' + self.short_name