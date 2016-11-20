from json import dumps as toJS

def header(handler, includes):
	print "<!DOCTYPE html>"
	print "<html>"
	print "<head>"
	print "<title>%s</title>" % handler.pageTitle
	# print "<link rel=\"stylesheet\" type=\"text/css\" href=\"/static/third-party/syntax-highlighting.css\">"
	print "<link rel=\"shortcut icon\" href=\"/static/images/favicon.ico\">"

	print "<link rel=\"stylesheet\" href=\"/static/third-party/font-awesome/css/font-awesome.min.css\">"

	# jQuery
	print "<script src=\"//ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js\"></script>"
	print "<link rel=\"stylesheet\" href=\"//ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/themes/smoothness/jquery-ui.css\" />"
	print "<script src=\"//ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/jquery-ui.min.js\"></script>"

	print "<script type=\"text/javascript\">"
	print "$(document).ready(function() {"
	# If there's a terminal on the screen, focus it by default so keyboard scrolling works
	# http://stackoverflow.com/a/11928222/309308
	print "    $('.terminal').attr('tabindex', -1).focus();"
	# Have the titlebar link to the root
	print "    $('.titlebar').css('cursor', 'pointer').click(function() {document.location = '/';});"
	if handler.wrapperData['jsOnReady']:
		for js in handler.wrapperData['jsOnReady']:
			print "    %s" % js
	print "});"
	print "</script>"

	for filename in includes['less']:
		print "<link rel=\"stylesheet/less\" type=\"text/css\" href=\"%s\" />" % filename
	for filename in includes['css']:
		print "<link rel=\"stylesheet\" type=\"text/css\" href=\"%s\" />" % filename
	for filename in includes['js']:
		print "<script src=\"%s\" type=\"text/javascript\"></script>" % filename

	# Less
	print "<link rel=\"stylesheet/less\" type=\"text/css\" href=\"/static/style.less\">"
	print "<script type=\"text/javascript\">"
	print "less = %s;" % toJS({'env': 'production', 'async': False, 'dumpLineNumbers': 'comments'})
	print "</script>"
	print "<script src=\"/static/third-party/less.js\" type=\"text/javascript\"></script>"

	print "</head>"
	print "<body>"
	print "<div class=\"titlebar\">"
	print "<div class=\"title\">%s</div>" % handler.pagePath
	print "</div>"
	print "<div class=\"content\">"

def footer(handler):
	print "</div>"
	print "</body>"
	print "</html>"
