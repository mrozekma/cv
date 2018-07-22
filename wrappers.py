from json import dumps as toJS

def header(handler, includes):
	print("<!DOCTYPE html>")
	print("<html>")
	print("<head>")
	print("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
	print(f"<title>{handler.pageTitle}</title>")
	print("<link rel=\"shortcut icon\" href=\"/static/images/favicon.ico\">")

	print("<link rel=\"stylesheet\" href=\"/static/third-party/font-awesome/css/font-awesome.min.css\">")
	print("<link rel=\"stylesheet\" href=\"/static/third-party/qtip/jquery.qtip.min.css\">")

	# jQuery
	print("<script src=\"//ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js\"></script>")
	print("<link rel=\"stylesheet\" href=\"//ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/themes/smoothness/jquery-ui.css\" />")
	print("<script src=\"//ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/jquery-ui.min.js\"></script>")
	print("<script type=\"text/javascript\" src=\"/static/third-party/qtip/jquery.qtip.min.js\"></script>")

	print("<script type=\"text/javascript\">")
	print("$(function() {")
	# Have the titlebar link to the root
	print("    $('.titlebar').css('cursor', 'pointer').click(function() {document.location = '/';});")
	if handler.wrapperData['jsOnReady']:
		for js in handler.wrapperData['jsOnReady']:
			print(f"    {js}")
	print("});")
	print("</script>")

	for filename in includes['less']:
		print(f"<link rel=\"stylesheet/less\" type=\"text/css\" href=\"{filename}\" />")
	for filename in includes['css']:
		print(f"<link rel=\"stylesheet\" type=\"text/css\" href=\"{filename}\" />")
	for filename in includes['js']:
		print(f"<script src=\"{filename}\" type=\"text/javascript\"></script>")

	# Less
	print("<link rel=\"stylesheet/less\" type=\"text/css\" href=\"/static/style.less\">")
	print("<script type=\"text/javascript\">")
	print("less = %s;" % toJS({'env': 'production', 'async': False, 'dumpLineNumbers': 'comments'}))
	print("</script>")
	print("<script src=\"/static/third-party/less.js\" type=\"text/javascript\"></script>")

	print("</head>")
	print("<body>")
	print("<div class=\"titlebar\">")
	print(f"<div class=\"title\">{handler.pagePath}</div>")
	print("</div>")
	print("<div class=\"content\">")

def footer(handler):
	print("</div>")
	print("</body>")
	print("</html>")
