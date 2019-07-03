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

class Business(models.Model):
    business_name = models.CharField(max_length=100, unique= True)
    business_user = models.ForeignKey(User,on_delete=models.CASCADE)
    business_neighborhood = models.ForeignKey(Neighborhood, null=True)
    business_email = models.EmailField(max_length=100, unique= True) 
    
    @classmethod
    def search_by_business(cls,search_term):
        search_result = cls.objects.filter(business_name__icontains=search_term)
        return search_result   

    @classmethod
    def create_business(cls, **kwargs):
        business_location = Neighborhood.objects.get(id=request.user.profile.neighborhood.id)  
        new_business = Business(business_name=business_name,business_user=request.user,business_neighborhood=business_location,business_email=email)
        new_business.save()
    @classmethod
    def delete_business(cls, id):
        delete = cls.objects.filter(id=id).delete()
                   
    @classmethod
    def update_business(cls,id):
        business = cls.objects.filter(id=id).update()
        return business


class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'images/',default='images/christine.jpg')
    bio = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    neighborhood = models.ForeignKey(Neighborhood,null=True, related_name='population')

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


class Post(models.Model):
    description =  models.CharField(max_length=70)
    post_image = models.ImageField(upload_to='images/', null=True,blank=True)
    categories = models.CharField(max_length=70)
    time_created =  models.DateTimeField(auto_now=True, null =True)
    location=models.ForeignKey(Neighborhood)
    user = models.ForeignKey(User, null=True)
    user_profile = models.ForeignKey(Profile)
    
    def __str__(self):
        return self.description
        


