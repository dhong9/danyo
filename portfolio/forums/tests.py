from django.test import TestCase
from portfolio.forums.models import Category

# Create your tests here.
class CategoryTest(TestCase):

    def create_category(self, name="Sports", description="Things you do to stay active"):
        return Category.objects.create(name=name, description=description)
    
    def test_category_creation(self):
        category = self.create_category()
        self.assertTrue(isinstance(category, Category))
        self.assertEqual(str(category), category.name)