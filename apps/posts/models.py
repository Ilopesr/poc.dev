from django.db import models
from django.db.models.functions import Now


class Post(models.Model):
    """Explanation why i db_default who was implemented on django 5.0,
    custom datas exist's in every project, so when we define in django
    one type of customization, and use a function provides from
    django.db.models.function, i dont need to,edit every time the
    custom type of a input of type time."""

    username = models.CharField("username", max_length=255, blank=False, null=False)
    created_datetime = models.DateTimeField(
        "created_datetime", db_default=Now(), blank=True, null=True
    )
    title = models.CharField("title", max_length=255, blank=False, null=False)
    content = models.TextField("content", blank=False, null=False)

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ["-created_datetime"]
