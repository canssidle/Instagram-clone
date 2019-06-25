from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import  Profile,Comment




class ProfileTestClass(TestCase):
    '''
    test class for Profile model
    '''
    def setUp(self):
        self.user = User.objects.create_user("testuser", "secret")
        self.profile_test = Profile(bio="my bio",
                                    user=self.user)
        self.profile_test.save()

    def test_instance_true(self):
        self.profile_test.save()
        self.assertTrue(isinstance(self.profile_test, Profile))




class CommentTestClass(TestCase):

    """Test class for Comment Model"""

    def setUp(self):
        self.new_user = User.objects.create_user("testuser", "secret")

        
        self.new_image.save()

        self.new_comment = Comment(
            image=self.new_image, comment_owner=self.new_profile, comment="comment ")

    def test_instance_true(self):
        self.new_comment.save()
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_save_comment(self):
        self.new_comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) == 1)

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()
        Comment.objects.all().delete()