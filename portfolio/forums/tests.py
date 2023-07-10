from django.test import TestCase
from portfolio.forums.models import Category, Post

# Create your tests here.
class CategoryTest(TestCase):

    def create_category(self, name="Sports", description="Things you do to stay active"):
        return Category.objects.create(name=name, description=description)
    
    def test_category_creation(self):
        category = self.create_category()
        self.assertTrue(isinstance(category, Category))
        self.assertEqual(str(category), category.name)

class PostTest(TestCase):

    def setUp(self):
        self.parent_post = Post.objects.create(
            category='scategory',
            postName='Test Page',
            name='John Doe',
            email='johndoe@example.com',
            body='Parent Post',
        )
        self.child_post = Post.objects.create(
            category='scategory',
            postName='Test Page',
            name='Jane Doe',
            email='janedoe@example.com',
            parent=self.parent_post,
            body='Child Post',
        )
    
    def create_post(self, category="airplanes", postName="sports", name="John Doe", email="john_doe@aol.com", body="Sports keeps you healthy."):
        return Post.objects.create(category=category, postName=postName, name=name, email=email, body=body)

    def test_get_posts_returns_child_posts(self):
        posts = self.parent_post.get_posts()
        self.assertEqual(posts.count(), 1)
        self.assertEqual(posts.first(), self.child_post)

    def test_get_posts_does_not_return_inactive_posts(self):
        self.child_post.active = False
        self.child_post.save()

        posts = self.parent_post.get_posts()
        self.assertEqual(posts.count(), 0)

    def test_get_posts_does_not_return_posts_without_parent(self):
        posts = self.child_post.get_posts()
        self.assertEqual(posts.count(), 0)
    
    def test_post_creation(self):
        post = self.create_post()
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(str(post), post.body)