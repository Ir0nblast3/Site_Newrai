from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    intro = RichTextField(
        blank=True,
        help_text="Texto principal da página"
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]
