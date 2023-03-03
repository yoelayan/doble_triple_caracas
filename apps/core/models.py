from django.db import models

# Create your models here.

class CommonModel(models.Model):
      description = models.CharField(max_length=150)
      
      class Meta:
            abstract = True
            
      def __str__(self) -> str:
            return self.description