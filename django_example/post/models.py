from django.db import models


class Post(models.Model):
    post_heading = models.CharField(max_length=200)
    post_text = models.TextField()

    def __unicode__(self):  # If python2 use __str__ if python3
        return unicode(self.post_heading)

class Like(models.Model):
        post = models.ForeignKey(Post, on_delete=models.CASCADE)