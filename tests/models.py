from django.db import models


class NavSampleArticle(models.Model):
    title = models.CharField(max_length=300)

    class Meta:
        app_label = "tests"

    def __str__(self) -> str:
        return self.title


class NewsletterSubscription(models.Model):
    email = models.EmailField()
    source = models.CharField(max_length=64, blank=True, default="")

    class Meta:
        app_label = "tests"
