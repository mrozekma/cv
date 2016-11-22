from json import dumps as toJS
import os
from PIL import Image
from uuid import uuid4 as uuid

from rorn.ResponseWriter import ResponseWriter

exts = ('png', 'gif')

class Photoswipe:
	def __init__(self, rootFolder, *paths):
		self.id = uuid()
		self.rootFolder = rootFolder
		self.imgs = [] # [(path, width, height, caption)]
		self += paths

	def __iadd__(self, path):
		if isinstance(path, tuple):
			for p in path:
				self += p
			return self

		self.add(path)
		return self

	def add(self, path, description = None):
		for ext in exts:
			fullPath = "%s.%s" % (os.path.join(self.rootFolder, path), ext)
			if os.path.isfile(fullPath):
				im = Image.open(fullPath)
				width, height = im.size
				self.imgs.append((fullPath, width, height, description))
				return
		raise IOError("Image not found: %s" % path)

	def getIndexByPath(self, seek):
		for i, (path, width, height, description) in enumerate(self.imgs):
			if any(path.endswith(os.path.sep + seek + '.' + ext) for ext in exts):
				return i
		raise ValueError("Path not found: %s" % seek)

	def __str__(self):
		w = ResponseWriter()
		try:
			id = "pswp-%s" % self.id
			print "<script type=\"text/javascript\">"
			print "$(document).ready(function() {"
			print "    var pswp = $('.pswp')[0];"
			print "    var items = %s;" % toJS([{'src': "/%s" % path, 'w': width, 'h': height, 'title': description} for (path, width, height, description) in self.imgs])
			print "    $('#%s img').click(function() {" % id
			print "        var options = {"
			print "            index: parseInt($(this).data('index'), 10),"
			print "            history: false,"
			print "        };"
			print "        new PhotoSwipe(pswp, PhotoSwipeUI_Default, items, options).init()"
			print "    });"
			print "});"
			print "</script>"
			print "<div id=\"%s\" class=\"screenshots\">" % id
			for i, (path, width, height, description) in enumerate(self.imgs):
				print "<div class=\"screenshot\"><img data-index=\"%d\" src=\"/%s\"></div>" % (i, path)
			print "</div>"
			print "<div class=\"clear\"></div>"
		finally:
			rtn = w.done()
		return rtn

	@staticmethod
	def fromSpec(specFilename):
		rtn = Photoswipe(os.path.dirname(specFilename))
		with open(specFilename) as f:
			while True:
				name = f.readline()
				if name == '':
					break
				if name == '\n' or name[0] == '#':
					continue
				description = f.readline()
				if description not in ('', '\n'):
					if f.readline() not in ('', '\n'):
						raise ValueError("Malformed spec file")
					if description[0] == '#':
						description = ''
				rtn.add(name.strip(), description.strip() or None)
		return rtn

	@staticmethod
	def getStatics():
		return ['third-party/photoswipe/photoswipe', 'third-party/photoswipe/photoswipe-ui-default', 'third-party/photoswipe/default-skin/default-skin']

	@staticmethod
	def getRootElement():
		# From http://photoswipe.com/documentation/getting-started.html
		return '''
<!-- Root element of PhotoSwipe. Must have class pswp. -->
<div class="pswp" tabindex="-1" role="dialog" aria-hidden="true">

    <!-- Background of PhotoSwipe. 
         It's a separate element as animating opacity is faster than rgba(). -->
    <div class="pswp__bg"></div>

    <!-- Slides wrapper with overflow:hidden. -->
    <div class="pswp__scroll-wrap">

        <!-- Container that holds slides. 
            PhotoSwipe keeps only 3 of them in the DOM to save memory.
            Don't modify these 3 pswp__item elements, data is added later on. -->
        <div class="pswp__container">
            <div class="pswp__item"></div>
            <div class="pswp__item"></div>
            <div class="pswp__item"></div>
        </div>

        <!-- Default (PhotoSwipeUI_Default) interface on top of sliding area. Can be changed. -->
        <div class="pswp__ui pswp__ui--hidden">

            <div class="pswp__top-bar">

                <!--  Controls are self-explanatory. Order can be changed. -->

                <div class="pswp__counter"></div>

                <button class="pswp__button pswp__button--close" title="Close (Esc)"></button>

                <button class="pswp__button pswp__button--share" title="Share"></button>

                <button class="pswp__button pswp__button--fs" title="Toggle fullscreen"></button>

                <button class="pswp__button pswp__button--zoom" title="Zoom in/out"></button>

                <!-- Preloader demo http://codepen.io/dimsemenov/pen/yyBWoR -->
                <!-- element will get class pswp__preloader--active when preloader is running -->
                <div class="pswp__preloader">
                    <div class="pswp__preloader__icn">
                      <div class="pswp__preloader__cut">
                        <div class="pswp__preloader__donut"></div>
                      </div>
                    </div>
                </div>
            </div>

            <div class="pswp__share-modal pswp__share-modal--hidden pswp__single-tap">
                <div class="pswp__share-tooltip"></div> 
            </div>

            <button class="pswp__button pswp__button--arrow--left" title="Previous (arrow left)">
            </button>

            <button class="pswp__button pswp__button--arrow--right" title="Next (arrow right)">
            </button>

            <div class="pswp__caption">
                <div class="pswp__caption__center"></div>
            </div>

        </div>

    </div>

</div>
'''
