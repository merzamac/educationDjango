from django.db import models
from ..departments.models import Department

# Create your models here.
class Skill(models.Model):
    skills = models.CharField('Skill',max_length=50)
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Employee skill'

    def __str__(self):
        return str(self.id) + '-' + self.skills

class Employee(models.Model):
    """
    modelo para tabla empleados
    """
    JOB_CHOICES=[
        ('0','Contador'),
        ('1','Administrador'),
        ('2','Economista'),
        ('3','Otro')
    ]
    first_name = models.CharField('First Name', max_length=20)
    second_name = models.CharField('Second Name',max_length=20)
    job = models.CharField('Job',max_length=1,choices=JOB_CHOICES)
    department = models.ForeignKey(Department,on_delete=models.CASCADE) #1-->N
    #avatar = models.ImageField(upload_to='employee',blank=True,null=True)
    skills = models.ManyToManyField(Skill)


    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.second_name
