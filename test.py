from django.contrib.auth.models import User
from twinkle.models import Twinkle
user = User.objects.get(username='root')
twinkle = Twinkle.objects.create(title='One more post',
    slug='one-more-post',
    body='Post body.',
    author=user)
twinkle.save()