from django.db import models

# Create your models here.

class Languages(models.Model):
    title=models.CharField(max_length=550)
    language_id=models.CharField(max_length=2, blank=True)

    def __str__(self):
        return self.title
    

class ImageGame(models.Model):
    language_preference=models.ForeignKey(Languages, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    input_field=models.CharField(max_length=550, blank=True)
    correct_answer_field=models.CharField(max_length=550)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.language_preference} - {self.created_at}"
    