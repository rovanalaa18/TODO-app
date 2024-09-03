from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class category(models.Model) :
    name = models.CharField(max_length=50 , unique=True)
    description = models.TextField(null = True , blank = True)
    user = models.ForeignKey(User , on_delete=models.CASCADE )

    def __str__(self) :
        return self.name
    

class task(models.Model) :
    status_choices = [
        ("pending" , "pending"),
        ("in progress" , "in progress"),
        ("completed" , "completed")
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField(null=True , blank=True)
    status = models.CharField(max_length=15 , choices=status_choices , default="pending")
    priority = models.IntegerField(validators=[MinValueValidator(1) , MaxValueValidator(10)] , null=True , blank = True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey (category , on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) :
        return self.title
    

class comment(models.Model) :

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    task = models.ForeignKey(task , on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')


