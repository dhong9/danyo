from django.db import models
from django.contrib.auth.models import User
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail, EmailMessage
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(default='default_profile.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed

    # Override the save method if the model
    def save(self):
        super().save()

        img = Image.open(self.image.path) # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    # the below like concatinates your websites reset password url and the reset email token which will be required at a later stage
    email_plaintext_message = "Open the link to reset your password" + " " + "{}{}".format(instance.request.build_absolute_uri("http://localhost:3000/login#/reset-password-form/"), reset_password_token.key)
    
    """
        this below line is the django default sending email function, 
        takes up some parameter (title(email title), message(email body), from(email sender), to(recipient(s))
    """
    send_mail(
        # title:
        "Password Reset for {title}".format(title="Crediation portal account"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@danyo.tech",
        # to:
        [reset_password_token.user.email],
        fail_silently=False,
    )

User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False