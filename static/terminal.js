Array.prototype.peek = function() {
	return this[this.length - 1];
};

// milliseconds to wait between characters when printing
PRINT_INTERVAL = 50;

Terminal = function(id) {
	this.id = id;
};

Terminal.prototype.show = function() {
	$('#' + this.id).css('display', 'inline');
}

// 'text' is a pseudo-markdown that must be valid (no error checking here).
// We return a list of tuples that will be executed in order each tick.
// The first element is the action for the caller to take; the rest are arguments.
//
//   * ('print', text to append)
//   * ('startnode', HTML to append, HTML attributes). The node created by that HTML becomes the active node edited by future actions)
//   * ('endnode'). Stop editing the current node and go to the previous
//
// This should hopefully look similar to markdown, but worries more about parsing easily and looking right for the cases I care about, not on being spec-compliant.
Terminal.prototype.parse = function(text) {
	var rtn = [];
	var state = ['text']; // 'text', 'list', 'emph', 'link'
	var line_start = true;
	for(var i = 0; i < text.length; i++) {
		var c = text.charAt(i);
		var n = (i+1 < text.length) ? text.charAt(i+1) : '\0';
		if(line_start) {
			if(c == ' ' || c == '\t' || c == '\n') { // Ignore leading spaces
				continue;
			}
			if(state.peek() == 'list' && c != '*') { // End list
				state.pop();
				rtn.push(['endnode']);
			}
		}
		switch(c) {
		case '\\': // Escape next character
			rtn.push(['print', text.charAt(++i)]);
			break;
		case '*': // Either emph, strong, or list
			if(line_start && n == ' ') { // List
				if(state.peek() != 'list') { // New list
					state.push('list');
					rtn.push(['startnode', '<ul/>']);
				}
				rtn.push(['startnode', '<li/>']); // Whether new or not, this is an item in it
				i++;
			} else if(state.peek() == 'emph') { // End emph
				state.pop();
				rtn.push(['endnode']);
			} else if(state.peek() == 'strong' && n == '*') { // End strong
				state.pop();
				rtn.push(['endnode']);
				i++;
			} else if(n == '*') { // Start strong
				state.push('strong');
				rtn.push(['startnode', '<strong/>']);
				i++;
			} else { // Start emph
				state.push('emph');
				rtn.push(['startnode', '<em/>']);
			}
			break;
		case '[': // Link (maybe)
			// Search for the ']'
			var end = text.indexOf(']', i + 1);
			if(end == -1) { // Treat this as normal text
				rtn.push(['print', c]);
				break;
			}
			// The URL should follow
			if(text.charAt(end + 1) != '(') {
				rtn.push(['print', c]);
				break;
			}
			var url = undefined;
			search:
			for(var j = end + 2; j < text.length; j++) {
				switch(text.charAt(j)) {
				case '\\':
					j++;
					continue;
				case ')':
					url = text.substring(end + 2, j);
					break search;
				}
			}
			if(url === undefined) {
				rtn.push(['print', c]);
				break;
			}
			// After all that, we do have a link
			state.push('link');
			rtn.push(['startnode', '<a/>', {'href': url}]);
			break;
		case ']': // End link (maybe)
			if(state.peek() != 'link') {
				rtn.push(['print', c]);
				break;
			}
			// Scan for the end of the URL
			i++; // '('
			search:
			for(i++; i < text.length; i++) {
				switch(text.charAt(i)) {
				case '\\':
					i++;
					continue;
				case ')':
					break search;
				}
			}
			state.pop();
			rtn.push(['endnode']);
			break;
		case '\n':
			if(state.peek() == 'list') { // End list item
				rtn.push(['endnode']);
			} else {
				rtn.push(['print', '<br/>']);
			}
			line_start = true;
			continue;
		case '<':
			rtn.push(['print', '&lt;']);
			break;
		case '>':
			rtn.push(['print', '&gt;']);
			break;
		case '&': //TODO more entities
			rtn.push(['print', '&amp;']);
			break;
		default:
			rtn.push(['print', c]);
			break;
		}
		line_start = false;
	}
	return rtn;
};

Terminal.prototype.hideCursor = function() {
	$('.terminal.cursor', $('#' + this.id)).detach();
	return this;
}

Terminal.prototype.print = function(text, on_finish) {
	var term = this;
	var box = $('#' + this.id);
	var cursor = $('.terminal.cursor', box);
	var off = 0;
	var nodes = [box];
	var tree = this.parse(text);
	var timer = setInterval(function() {
		while(tree.length > 0) {
			step = tree.shift();
			switch(step[0]) {
			case 'startnode':
				new_node = $(step[1]);
				if(step[2] !== undefined) {
					new_node.attr(step[2]);
				}
				nodes.peek().append(new_node);
				nodes.push(new_node);
				break;
			case 'endnode':
				nodes.pop();
				break;
			case 'print':
				nodes.peek().append(step[1]);
				cursor.detach().appendTo(nodes.peek());
				return; // The only action that stops this tick
			}
		}

		cursor.addClass('blink');
		clearInterval(timer);
		if(on_finish !== undefined) {
			on_finish(term);
		}
	}, PRINT_INTERVAL);
	cursor.removeClass('blink');
	return this;
}
