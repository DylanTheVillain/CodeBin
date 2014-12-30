from django import template
import html

register = template.Library()

def html_decode(value):
	decodedString = html.unescape(value)
	decodedString = decodedString.replace('"', '\\"')
	decodedString = decodedString.replace("'", "\\'")
	decodedString = decodedString.replace('\n','\\n')
	return decodedString

register.simple_tag(html_decode)
