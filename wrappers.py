from json import dumps as toJS

def header(handler):
	print "<!DOCTYPE html>"
	print "<html>"
	print "<head>"
	print "<title>%s</title>" % handler.pageTitle
	# print "<link rel=\"stylesheet\" type=\"text/css\" href=\"/static/syntax-highlighting.css\">"
	print "<link rel=\"shortcut icon\" href=\"/static/images/favicon.ico\">"

	# jQuery
	print "<script src=\"//ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js\"></script>"
	print "<link rel=\"stylesheet\" href=\"//ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/themes/smoothness/jquery-ui.css\" />"
	print "<script src=\"//ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/jquery-ui.min.js\"></script>"

	# Less
	print "<link rel=\"stylesheet/less\" type=\"text/css\" href=\"/static/style.less\">"
	print "<script type=\"text/javascript\">"
	print "less = %s;" % toJS({'env': 'production', 'async': False, 'dumpLineNumbers': 'comments'})
	print "</script>"
	print "<script src=\"/static/less.js\" type=\"text/javascript\"></script>"

	print "</head>"
	print "<body>"
	print "<div class=\"titlebar\">"
	# print "<div class=\"icon\"><img src=\"/static/images/terminal.png\"></div>"
	print "<div class=\"title\">%s</div>" % handler.pageSubtitle
	print "</div>"
	print "<div class=\"content\">"

def footer(handler):
	print "</div>"
	print "</body>"
	print "</html>"