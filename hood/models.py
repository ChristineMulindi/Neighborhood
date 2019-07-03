from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True)
    posted_by =  models.CharField(max_length=100, null=True)
    count = models.CharField(max_length=100)
    police = models.CharField(max_length=100)
    police_department_address = models.CharField(max_length=100)
    health = models.CharField(max_length=100)
    health_department_address = models.CharField(max_length=100)


    def __str__(self):
        return f' {self.name} Neighborhood'
    
    @classmethod
    def find_neigborhood(cls,search_term):
        search_result = cls.objects.filter(business_name__icontains=search_term)
        return search_result   

    @classmethod
    def create_neigborhood(cls):
        cls.save()

    @classmethod
    def delete_neigborhood(cls, id):
        delete = cls.objects.filter(id=id).delete()
                   
    @classmethod
    def update_occupants(cls,id):
        occupants = cls.objects.filter(id=id).update()
        return occupants


    class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'images/',default='images/christine.jpg')
    bio = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    neighborhood = models.ForeignKey(Neighbourhood,null=True, related_name='population')

    def __str__(self):
        return f'{self.user.username} Profile'

    @property
    def image(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url

    @classmethod
    def search_by_username(cls,search_term):
        search_result = cls.objects.filter(user__username__icontains=search_term)
        return search_result

    def save_profile(self):
        self.save()