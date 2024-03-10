from django.db import models

# Category model
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

# Post model
class Post(models.Model):
    postName = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField()
    isPlainText = models.BooleanField(default=True)

    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    mainFeatured = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)

    class Meta:
        ordering = ['create']

    def __str__(self):
        return f"[{self.create}] {self.name} {self.body}"

    def get_posts(self):
        return Post.objects.filter(parent=self).filter(active=True)