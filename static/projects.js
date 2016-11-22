$(document).ready(function() {
	$('a.screenshot-link').click(function() {
		pswp_id = 'pswp-' + $(this).data('pswp');
		idx = $(this).data('index');
		$('.screenshots#' + pswp_id + ' .screenshot img[data-index=' + idx + ']').click();
	});
});
