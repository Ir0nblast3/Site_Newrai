from django.db import models
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.admin.panels import FieldPanel


@register_setting
class NavigationSettings(BaseGenericSetting):

    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel("logo"),
    ]

@register_setting
class FooterSettings(BaseGenericSetting):
    
    newRai_icon=models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    developed_by = models.CharField("Developed by",max_length=255,blank=True)

    finaciamento_icon=models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    panels = [
        FieldPanel("newRai_icon"),
        FieldPanel("developed_by"),
        FieldPanel("finaciamento_icon"),
    ]
