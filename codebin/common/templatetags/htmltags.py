from django import template
import html.parser

register = template.Library()

def html_decode(value):
	parser = html.parser.HTMLParser()
	decodedString = parser.unescape(value)
	decodedString = decodedString.replace('"', '\\"')
	return decodedString

register.simple_tag(html_decode)
