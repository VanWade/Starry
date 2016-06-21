from django.contrib.sitemaps import Sitemap
from twinkle.models import Twinkle

class TwinkleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Twinkle.published.all()

    def lastmod(self, obj):
        return obj.publish


