from django.utils.html import format_html
from django.contrib.admin.widgets import AdminFileWidget


class InlineImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = ''
        if value and getattr(value, 'url', None):
            image_url = value.url
            output += '<img style="height: 200px; width: 200px; object-fit: cover" src="{}" />'.format(image_url)
        output += super(AdminFileWidget, self).render(name, value, attrs)
        return format_html('{}'.format(output))