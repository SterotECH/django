from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    label = models.CharField(max_length=255)

    # Generic RelationShip
    def __str__(self):
        return self.label


class TaggedItem(models.Model):
    # What tag is applied to What Object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # Type of Object
    # ID of the Object
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveSmallIntegerField()
    content_object = GenericForeignKey()
