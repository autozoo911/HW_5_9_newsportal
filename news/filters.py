from django_filters import FilterSet
from NP_project.news.models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'author': ['icontains'],
            'article_text': ['icontains'],
            'date_time_in': ['gt', 'lt'],
            'rating': ['gt', 'lt'],
        }
