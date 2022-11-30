from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        self.rating = 0
        for author_post in Post.objects.filter(author=self.pk):
            self.rating += author_post.post_rating * 3
            for user_comments in Comment.objects.filter(post=author_post):
                self.rating += user_comments.comment_rating
        for author_comments in Comment.objects.filter(user=self.user):
            self.rating += author_comments.comment_rating

        self.save()

    def __str__(self):
        return f'{self.user}, рейтинг: {self.rating}'


class Category(models.Model):
    sport = 'sport'
    politics = 'politics'
    education = 'education'

    CATEGORIES = [(sport, 'спорт'),
                  (politics, 'политика'),
                  (education, 'образование'),
                  ]

    name = models.CharField(max_length=20, choices=CATEGORIES, unique=True)

    # def __str__(self):
    #     return self.name.title


class Post(models.Model):
    news = 'NW'
    article = 'AT'

    ARTICLES = [(news, 'Новость'), (article, 'Статья')]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=ARTICLES, default=news)
    date_time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64, default='Unnamed')
    article_text = models.TextField(max_length=10000, default='Text')
    post_rating = models.IntegerField(default=0, db_column='rating')

    categories = models.ManyToManyField(Category, through='PostCategory', related_name='post')

    @property
    def rating(self):
        return self.post_rating

    @rating.setter
    def rating(self, value):
        if value >= 0 and isinstance(value, int):
            self.post_rating = value
        else:
            self.post_rating = 0
        self.save()

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return f'{self.article_text[0:124]}...'

    def __str__(self):
        return f'{self.title} : {self.article_text[:120]}, рейтинг:{self.post_rating}'


class PostCategory(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=10000, default='text')
    date_time_in = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0, db_column='rating')

    @property
    def rating(self):
        return self.comment_rating

    @rating.setter
    def rating(self, value):
        if value >= 0 and isinstance(value, int):
            self.comment_rating = value
        else:
            self.comment_rating = 0
        self.save()

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()

    def __str__(self):
        return f'{self.text} : {self.comment_rating}'
