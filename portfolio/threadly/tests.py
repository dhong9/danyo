from django.test import TestCase
from portfolio.threadly.models import Comment, Contact

class CommentTest(TestCase):

    def create_comment(self, pageName="sports", name="John Doe", email="john_doe@aol.com", body="Sports keeps you healthy."):
        return Comment.objects.create(pageName=pageName, name=name, email=email, body=body)
    
    def test_comment_creation(self):
        comment = self.create_comment()
        self.assertTrue(isinstance(comment, Comment))
        self.assertEqual(str(comment), comment.body)

class ContactTest(TestCase):

    def create_contact(self, full_name="Gabe Real", email="gabriel@hotmail.com", subject="Things Are Real", query_txt="Yup, things just got real."):
        return Contact.objects.create(full_name=full_name, email=email, subject=subject, query_txt=query_txt)
    
    def test_contact_creation(self):
        contact = self.create_contact()
        self.assertTrue(isinstance(contact, Contact))
        self.assertEqual(str(contact), contact.query_txt)