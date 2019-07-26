from django.db import models 


class Contact(models.Model):

    first_name = models.CharField(max_length=255) 
    last_name = models.CharField(max_length=255) 
    email = models.CharField(max_length=255) 
    note = models.TextField() 

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self): 
        return f'{self.first_name} {self.last_name} {self.email} {self.note} '
    def __repr__(self): 
        return f'{self.first_name} {self.last_name} '
    