from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    img_profile = models.ImageField(upload_to='member')
    relation = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='relation_user_set',
        through='Relationship',
    )
    
    def to_dict(self):
        return {
            'pk': self.pk,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
        }


class Relationship(models.Model):
    RELATIONSHIP_FOLLOWING = 1
    RELATIONSHIP_BLOCKED = 2
    RELATIONSHIP_TYPE = (
        (RELATIONSHIP_FOLLOWING, 'Follow'),
        (RELATIONSHIP_BLOCKED, 'Block'),
    )

    from_user = models.ForeignKey(MyUser, related_name='relations_from_user')
    to_user = models.ForeignKey(MyUser, related_name='relations_to_user')
    relation_type = models.IntegerField(choices=RELATIONSHIP_TYPE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('from_user', 'to_user')
        )

    def __str__(self):
        return 'Relation({}) From({}) To ({})'.format(
            self.get_relation_type_display(),
            self.from_user.username,
            self.to_user.username,
        )
