$(document).ready(function() {
	$('.page_entry').hover(function(e) {
		$(this).toggleClass('hover', e.type == 'mouseenter');
	});
});
