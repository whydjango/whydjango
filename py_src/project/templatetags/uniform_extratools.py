from django import template

register = template.Library()

@register.filter
def get_widget_class(field):
    return field.field.widget.__class__.__name__.lower()

@register.filter
def get_widget_classes(field):
    class_name = field.field.widget.__class__.__name__.lower()
    if 'class' in field.field.widget.attrs:
        classes = " ".join(field.field.widget.attrs['class'].split(' ') + [class_name] )
    else:
        classes = class_name
    return classes

@register.filter
def has_required_fields(form):
    for field in form:
        if field.field.required and field.field.label:
            return True
    return False

@register.filter
def simple_uni_form(form, helper=None):
    if not helper:
        return uni_form_tags.as_uni_form(form)
    node = uni_form_tags.BasicNode('form', 'helper')
    context = template.Context({'form': form, 'helper': helper})
    realcontext = node.get_render(context)
    tpl = get_template('uni_form/simple_uni_form.html')
    return tpl.render(realcontext)