$(function() {
	$('a.screenshot-link').click(function() {
		pswp_id = 'pswp-' + $(this).data('pswp');
		idx = $(this).data('index');
		$('.screenshots#' + pswp_id + ' .screenshot img[data-index=' + idx + ']').click();
	});

	tag_filters = new Set();
	apply_filters = function() {
		if(tag_filters.size == 0) {
            $('.project-tags .label').removeClass('selected');
			$('.tag-filter').hide();
			$('.subpage').show();
        } else {
			$('.project-tags .label').each(function() {
				btn = $(this);
				btn.toggleClass('selected', tag_filters.has(btn.text()));
			});
			$('.tag-filter .tag-list').text(Array.from(tag_filters).sort().join(' '));
			$('.tag-filter').show();
			$('.subpage').each(function() {
				subpage = $(this);
				for(tag of tag_filters) {
					if($('.project-filters .label:contains(' + tag + ')', subpage).length == 0) {
						subpage.hide();
						return;
					}
                }
                subpage.show();
			});
		}
	};
	$('.stdout.project-tags .label').click(function() {
		tag = $(this).text();
		if(tag_filters.has(tag)) {
			tag_filters.delete(tag);
        } else {
            tag_filters.add(tag);
		}
		apply_filters();
	});
	$('#tag-filter-clear').click(function() {
		tag_filters.clear();
		apply_filters();
	});
});
