from django.db import models

# Comment model
class Comment(models.Model):
    pageName = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField()

    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['create']

    def __str__(self):
        return self.body

    def get_comments(self):
        return Comment.objects.filter(parent=self).filter(active=True)

# Contact model
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    query_txt = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query_txt
    
    class Meta:
        ordering = ['add_time']