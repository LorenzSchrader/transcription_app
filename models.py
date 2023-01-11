from django.db import models
from django.utils import timezone

# we import the user model, which will have a relationship with the Post class.
from django.contrib.auth.models import User

# The file is used to access our database. We can represent our database structure as models.

#the class Post defines our database:
class Post(models.Model):
    # each attribute in our class will represent a field in our database:
    title = models.CharField(max_length=100)

    content = models.TextField()

    date_posted = models.DateTimeField(default = timezone.now)
    # you can use the auto_now = True argument (problem -> you cant update the value)
    # we choose the default value to be defined by the timezone.now funciton (however we dont call the function {this is why there are now ()})

    author = models.ForeignKey(User, on_delete = models.CASCADE)
    # here we define the author to be the value of the User class.
    # further we define, whether or not the data of each user should be deleted, when the User gets deleted.
    # we defined the logic to be: User deleted -> posts deleted

    # this function defines how each post will be displayed, once we call it.
    def __str__(self):
        return self.title
