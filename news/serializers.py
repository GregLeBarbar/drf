from rest_framework import serializers
from django.contrib.auth.models import User, Group
from news.models import News


class NewsSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = News
        fields = ('id', 'title', 'owner')



class UserSerializer(serializers.ModelSerializer):

    news = serializers.HyperlinkedRelatedField(many=True, view_name='news-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'news')
