var listener = null;

Array.prototype.peek = function() {
	return this[this.length - 1];
};

// milliseconds to wait between characters when printing
PRINT_INTERVAL = 50;

function cursor_move_to(target) {
	if(target.length > 0) {
		cursor = $('.terminal .cursor');
		if(cursor[0] != target[0]) {
			target.addClass('cursor').toggleClass('blink', cursor.hasClass('blink'));
			cursor.removeClass('cursor blink');
		}
	}
}

function cursor_move_backward() {
	cursor_move_to($('.terminal .prompt .cursor').prev('.user-input'));
}

function cursor_move_forward() {
	cursor_move_to($('.terminal .prompt .cursor').next('.user-input'));
}

function cursor_move_beginning() {
	cursor_move_to($('.terminal .prompt .user-input:first'));
}

function cursor_move_end() {
	cursor_move_to($('.terminal .prompt .user-input:last'));
}

function bind(hotkeys, fn) {
	if(typeof(hotkeys) == 'string') {
		hotkeys = [hotkeys];
	}
	$.each(hotkeys, function(_, hotkey) {
		listener.simple_combo(hotkey, fn);
	});
}

function bind_all() {
	if(listener != null) {
		listener.listen();
		return;
	}

	// Ideally we want is_solitary, but it has the annoying side-effect that you can't press one key
	// while holding another, which happens quite a lot when typing fast. Not using it means the handlers
	// have to check for modifier keys manually, but that's how it goes
	listener = new window.keypress.Listener(null, {is_solitary: false});

	// Printable characters
	var printable = '`1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?';
	$.each(printable.split(''), function(_, c) {
		bind(c, function(e) {
			if(e.altKey || e.ctrlKey || e.metaKey) {
				return true;
			}
			$('.terminal .cursor').before($('<div/>').addClass('user-input').text(c));
		});
	});

	// Let's see how many readline hotkeys I can remember
	// On second thought, readline(3) it is
	bind('backspace', function() {
		$('.terminal .cursor').prev('.user-input').remove();
	});
	bind(['delete', 'meta d'], function() {
		cursor = $('.terminal .cursor');
		if(cursor.hasClass('user-input') && !cursor.hasClass('end')) {
			cursor_move_forward();
			cursor.remove();
		}
	});
	bind(['left', 'meta b'], cursor_move_backward);  // backward-char
	bind(['right', 'meta f'], cursor_move_forward);  // forward-char
	bind(['home', 'meta a'], cursor_move_beginning); // beginning-of-line
	bind(['end', 'meta e'], cursor_move_end);        // end-of-line
	bind('meta l', function() {                      // clear-screen
		$('.terminal .cursor').parents('.prompt').prevAll().remove();
	});

	bind('enter', function() {
		console.error('Unimplemented'); //TODO
	});
}

function unbind_all() {
	if(listener != null) {
		listener.stop_listening();
	}
}

Terminal = function(id) {
	this.id = id;
	$(document).ready(function() {
		if($('.terminal .cursor').parents('.terminal .prompt').length > 0) {
			bind_all();
		}
	});
};

// 'text' is a pseudo-markdown that must be valid (no error checking here).
// We return a list of tuples that will be executed in order each tick.
// The first element is the action for the caller to take; the rest are arguments.
//
//   * ('print', text to append)
//   * ('startnode', HTML to append, HTML attributes). The node created by that HTML becomes the active node edited by future actions)
//   * ('endnode'). Stop editing the current node and go to the previous
//
// This should hopefully look similar to markdown, but worries more about parsing easily and looking right for the cases I care about, not on being spec-compliant.
function parse(text) {
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

Terminal.prototype.print = function(text, on_finish) {
	var term = this;
	var box = $('<div/>').addClass('text');
	box.appendTo($('#' + this.id));
	var off = 0;
	var nodes = [box];
	var tree = parse(text);
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
				Terminal.scrollCursor(nodes.peek(), false);
				return; // The only action that stops this tick
			}
		}

		Terminal.scrollCursor(undefined, true);
		clearInterval(timer);
		if(on_finish !== undefined) {
			on_finish(term);
		}
	}, PRINT_INTERVAL);
	return this;
}

Terminal.prototype.prompt = function(after) {
	var box = $('<div/>').addClass('prompt');
	box.appendTo($('#' + this.id));
	cursor = Terminal.scrollCursor(box, true);
	cursor.addClass('user-input end').html('&nbsp;'); // Prompts end in a fake space for the cursor to occupy if it's after all the real user input
	bind_all();
}

// This moves the cursor after 'new_target', and makes it blink if 'blink' is true
// If 'new_target' is unspecified, it moves it to the end of the last prompt on the page
// This is only meant for scrolling text onto the screen; prompts handle the cursor differently
Terminal.scrollCursor = function(new_target, blink) {
	cursor = $('.terminal .cursor');
	if(cursor.length == 0) {
		cursor = $('<div/>').addClass('cursor');
	}
	if(new_target === undefined) {
		new_target = $('.terminal :not(.cursor):last');
	}
	cursor.detach().appendTo(new_target);
	if(blink === true || blink === false) {
		cursor.toggleClass('blink', blink);
	}
	return cursor;
}
