from django.test import TestCase
from portfolio.threadly.models import Project, Comment, Contact

class ProjectTest(TestCase):

    def create_project(self, name="Whitespace", description="Whitespace interpreter"):
        return Project.objects.create(name=name, description=description)
    
    def test_project_creation(self):
        project = self.create_project()
        self.assertTrue(isinstance(project, Project))
        self.assertEqual(str(project), project.name)

class CommentTest(TestCase):

    def setUp(self):
        self.parent_comment = Comment.objects.create(
            pageName='Test Page',
            name='John Doe',
            email='johndoe@example.com',
            body='Parent Comment',
        )
        self.child_comment = Comment.objects.create(
            pageName='Test Page',
            name='Jane Doe',
            email='janedoe@example.com',
            parent=self.parent_comment,
            body='Child Comment',
        )
    
    def create_comment(self, pageName="sports", name="John Doe", email="john_doe@aol.com", body="Sports keeps you healthy."):
        return Comment.objects.create(pageName=pageName, name=name, email=email, body=body)

    def test_get_comments_returns_child_comments(self):
        comments = self.parent_comment.get_comments()
        self.assertEqual(comments.count(), 1)
        self.assertEqual(comments.first(), self.child_comment)

    def test_get_comments_does_not_return_inactive_comments(self):
        self.child_comment.active = False
        self.child_comment.save()

        comments = self.parent_comment.get_comments()
        self.assertEqual(comments.count(), 0)

    def test_get_comments_does_not_return_comments_without_parent(self):
        comments = self.child_comment.get_comments()
        self.assertEqual(comments.count(), 0)
    
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