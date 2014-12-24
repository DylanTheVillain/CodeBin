from django import template
import HTMLParser

register = template.Library()

def html_decode(text):
