from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    ユーザ
    """
    name   = models.CharField('ユーザ名', max_length=15)
    who_is = models.CharField('自己紹介',  max_length=63)
    mail   = models.CharField('メールアドレス', max_length=127)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "who_is"],
                name="user_unique"
            ),
        ]

    def __str__(self):
        return self.name

class Lonliness(models.Model):
    """
    さみしさ
    """
    user      = models.ForeignKey(User, verbose_name='誰か', related_name='lonliness', on_delete=models.CASCADE)
    content   = models.CharField('さみしさ',  max_length=255)

    def __str__(self):
        return self.content


class Reaction(models.Model):
    """
    リアクション
    """
    lonliness     = models.ForeignKey(Lonliness, verbose_name='さみしさ', related_name='reactions', on_delete=models.CASCADE)
    reaction_char = models.IntegerField('リアクション')

    def __str__(self):
        return str(self.reaction_char)
