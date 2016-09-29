from __future__ import unicode_literals
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.db import models


class News(models.Model):
    """
    Model News
    """
    title = models.CharField(max_length=128)
    owner = models.ForeignKey('auth.User', related_name='news')

