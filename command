# Блок команд для быстрой проверки, это если shell перезапустить придется)
from news.models import *
author_1 = Author.objects.get(pk=1)
author_2 = Author.objects.get(pk=2)
author_1.update_rating()
author_2.update_rating()

# Создаем юзеров
User.objects.create_user('Batman')
User.objects.create_user('Jocker')
User.objects.create_user('John Smith')
User.objects.create_user('Jack London')
User.objects.create_user('Ernest Hamingway')

u_1 = User.objects.get(pk=1)
u_2 = User.objects.get(pk=2)
u_3 = User.objects.get(pk=3)
u_4 = User.objects.get(pk=4)
u_5 = User.objects.get(pk=5)

# Передаем авторам свои пременные
author_1 = Author.objects.create(user=u_4)
author_2 = Author(user=u_5)
author_2.save()

# Создаем категории
category_1 = Category.objects.create(name='crypto')
category_2 = Category.objects.create(name='celebrities')
category_3 = Category.objects.create(name='politic')
category_4 = Category.objects.create(name='sport')
category_5 = Category.objects.create(name = 'news')

# Создаем посты, по дефолту type=NW (news), все кроме автора по дефолту, почему-то я назвал статьи - 'PT'
post_1 = Post.objects.create(author=author_1)
post_2 = Post.objects.create(author=author_1)
post_3 = Post.objects.create(author=author_2, type='PT')
post_4 = Post.objects.create(author=author_2, type='PT')

# Присваиваем переменные категориям и постам
category_1 = Category.objects.get(pk=1)
category_2 = Category.objects.get(pk=2)
category_3 = Category.objects.get(pk=3)
category_4 = Category.objects.get(pk=4)
category_5 = Category.objects.get(pk=5)
post_1 = Post.objects.get(pk=1)
post_2 = Post.objects.get(pk=2)
post_3 = Post.objects.get(pk=3)
post_4 = Post.objects.get(pk=4)

# Присваиваем постам категории
PostCategory.objects.create(posts=post_1, categories=category_1)
PostCategory.objects.create(posts=post_1, categories=category_2)
PostCategory.objects.create(posts=post_2, categories=category_3)
PostCategory.objects.create(posts=post_3, categories=category_4)
PostCategory.objects.create(posts=post_3, categories=category_5)
PostCategory.objects.create(posts=post_4, categories=category_3)

# Создаем комментарии
c_1 = Comment.objects.create(post = post_1, user=u_1)
c_2 = Comment.objects.create(post = post_1, user=u_2)
c_3 = Comment.objects.create(post = post_2, user=u_2)
c_4 = Comment.objects.create(post = post_3, user=u_3)
c_5 = Comment.objects.create(post = post_1, user=u_4) #коммент автора
c_6 = Comment.objects.create(post = post_4, user=u_5)

# Ставим лайи/дизлайки для комментов и постов
c_1.like()
c_2.like()
c_2.like()
c_3.like()
c_3.like()
c_3.like()
c_4.like()
c_4.like()
c_4.like()
c_4.like()
c_5.like()
c_5.like()
c_5.like()
c_5.like()
c_5.like()
c_6.like()
c_6.like()
c_6.like()
c_6.like()
c_6.like()
c_6.like()
post_1.like()
post_2.like()
post_2.like()
post_3.like()
post_3.like()
post_3.like()
post_4.like()
post_4.like()
post_4.like()
post_4.like()

# Обновляем рейтинг авторов
author_1.update_rating()
author_2.update_rating()

# Выводим username и рейтинг лучшего пользователя
username = Author.objects.all().order_by('-rating').values('user__username', 'rating')[0]

# Вывести дату добавления, username автора, рейтинг,
# заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
post = Post.objects.all().order_by('-post_rating').values('date_time_in', 'author__user__username', 'post_rating', 'article_text')[0]


Есть проблема: Комментарии автора считаются дважды, как отдельно комментарии автора
и как часть всех комментариев к статьям автора. Они идут в общую сумму.
Но поскольку не было каких либо уточнений по этому поводу я не стал усложнять.




