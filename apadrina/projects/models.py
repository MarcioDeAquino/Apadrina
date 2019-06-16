from django.db import models



# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50)
    local = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name

    


class Vacancy(models.Model):
    name = models.CharField(max_length=30)
    project = models.ForeignKey(Project, related_name='vagas', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    colab =  models.ForeignKey('users.User',  on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    
