from haystack import indexes
from twinkle.models import Twinkle
class TwinkleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    publish = indexes.DateTimeField(model_attr='publish')
    def get_model(self):
        return Twinkle

    def index_queryset(self, using=None):
        return self.get_model().published.all()
