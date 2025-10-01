from django import template
register = template.Library()

def first5(val):
    res = val[:3].upper()+ val[3:].lower()
    return res

register.filter('first5',first5)