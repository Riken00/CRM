from django.db import models
from django.db.models.enums import Choices


from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    pass
                            # we can also add some Field like ie.
                            # phone_No = models.IntegerField()

                            # this will allow us to add inbuilded user authentication systems and also help up in to build login systems
                            #  to set up to work need to say django that we are using AUTH_USER_MODEL in setting

class Leads(models.Model):
    first_name=  models.CharField(max_length=15)
    last_name=  models.CharField(max_length=15)
    age = models.IntegerField()
    agent = models.ForeignKey("Agents",on_delete=models.CASCADE)
    def __str__(self) :
        return f"{self.first_name}  {self.last_name}  "


class Agents(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self) :
        return self.User.email
    



#  ---------------------------------------------------------------------------

# class For_just_demo(models.Model):
#     Source_choice = (
#         ('0','Youtube'),
#         ('1','Google'),
#         ('2','Face Book'),
#     )

#     f_name = models.CharField(max_length=50)
#     l_name = models.CharField(max_length=50)
#     age = models.IntegerField(default = 0)

#     phone = models.BooleanField(default = False)
#     source = models.CharField(Choices= Source_choice , default=0,null=False)

#     profile_pic =   models.ImageField(blank=True,null=False)
#     special_files = models.FileField(blank=True,null=False)

