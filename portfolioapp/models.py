from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = MarkdownxField()
    tech = models.CharField(max_length=50)
    image = models.URLField(max_length=500)

    def formatted_markdown(self):
        return markdownify(self.description)

    def body_summary(self):
        return markdownify(self.description[:100] + "...")

    def desc_summary(self):
        return markdownify(self.description[:250] + "..")

    