from django.db import models



# Create your models here.

class Project(models.Model):
    nome = models.CharField(max_length=50)
    local = models.CharField(max_length=100)
    escopo = models.CharField(max_length=300)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.nome

    
    
class Vacancy(models.Model):
    nome = models.CharField(max_length=30)
    project = models.ForeignKey(Project, related_name='vagas', on_delete=models.CASCADE)
    how_can_help = models.CharField(max_length=100)
    colab =  models.ForeignKey('users.User',  on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nome

    
