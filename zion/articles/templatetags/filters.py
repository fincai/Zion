# Calculate a comment's index
from django import template
register = template.Library()

def comment_index(value, arg):
    return value + (arg - 1) * 20

register.filter('comment_index', comment_index)
