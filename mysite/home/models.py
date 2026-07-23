from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from modelcluster.fields import ParentalKey
from wagtail.models import Orderable


class Enterprises(Orderable):
    page = ParentalKey(
        'HomePage',
        on_delete=models.CASCADE,
        related_name='enterprises'
    )

    enterprise_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('enterprise_img'),
    ]

class HomePage(Page):
    # HERO
    hero_title = RichTextField(
        blank=True,
        features=["bold", "italic"]
    )

    hero_subtitle = RichTextField(
        blank=True,
        features=["bold", "italic"]
    )

    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    hero_text = RichTextField(
         blank=True,
        features=["bold", "italic"]
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_subtitle"),
        FieldPanel("hero_image"),
        FieldPanel("hero_text"),
        InlinePanel("enterprises", label="Enterprises"),
    ]