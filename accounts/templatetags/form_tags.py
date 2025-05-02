from django import template
from django.forms.boundfield import BoundField  # ⬅️ 이거 꼭 추가!

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css):
    if isinstance(field, BoundField):
        return field.as_widget(attrs={"class": css})
    return field  # ⬅️ str이면 그냥 그대로 반환
