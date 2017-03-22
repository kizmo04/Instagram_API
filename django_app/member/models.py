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

    def follow(self, user):
        self.relations_from_user.create(
            to_user=user,
            relation_type=Relationship.RELATIONSHIP_FOLLOWING
        )

    def block(self, user):
        pass

    @property
    def following(self):
        relations = self.relations_from_user.filter(
            relation_type=Relationship.RELATIONSHIP_FOLLOWING
        )
        return MyUser.objects.filter(id__in=relations.values('to_user_id'))

    def followers(self):
        pass

    def block_users(self):
        pass


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
