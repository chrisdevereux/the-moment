from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, BlockField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class Article(Page):
    intro = models.TextField('Introduction', blank=True)
    body = RichTextField('Article', blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.PROTECT, null=True
    )

    content_panels = [
        FieldPanel('title', classname='full title'),
        FieldPanel('intro', classname='full intro'),
        FieldPanel('body', classname='full body'),
        ImageChooserPanel('image'),
    ]

class HomePage(Page):
    headline_article = models.ForeignKey(Article, null=True, on_delete=models.PROTECT)

    content_panels = Page.content_panels + [
        PageChooserPanel('headline_article', 'themoment.Article'),
    ]

    def main_image(self):
        print(self.headline_article.image)

    def secondary_articles(self):
        articles = Article.objects.exclude(id=self.headline_article.id).order_by('-first_published_at')

        return articles[:2]

