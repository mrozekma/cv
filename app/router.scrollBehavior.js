// Scrolling is contained to the terminal element, not the whole page, so this handles scrolling that element
//TODO Figure out how to restore the terminal scroll position (savedPosition will always be (0, 0))
export default function(to, from, savedPosition) {
	const process = function() {
		if(to.hash) {
			document.getElementById(to.hash.substring(1)).scrollIntoView();
		} else {
			document.getElementById('terminal').scrollTo(0, 0);
		}
	};

	if(from.name == to.name) {
		process();
	} else {
		// Need to wait until after the transition to invoke process(). The transition's afterEnter hook looks for this variable on the Vue instance
		this.app.afterRouteFn = process;
	}
	return false;
};
