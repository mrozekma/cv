$(function() {
    ident = function(b) { return b; };

    // All the following checkbox code is currently not recursive (i.e. it assumes every checkbox is either top-level or a leaf)

    setState = function(parent, children) {
        childrenChecks = children.map(function() { return this.checked; }).get();
        all = childrenChecks.every(ident);
        some = childrenChecks.some(ident);
        parent.prop('checked', all);
        parent.prop('indeterminate', some && !all);
    }

    setRootState = function() {
        setState($('.pdf-generator .title input'), $('.pdf-generator > form > ul > li > input'));
    }

    setStateByChildren = function() {
        parent = $(this);
        console.log(parent);
        children = $('li > input', parent.parent());
        if(children.length > 0) {
            setState(parent, children);
        }
    }

    // Set parent checkbox states based on their children
    $('.pdf-generator > form > ul > li > input').each(setStateByChildren);
    setRootState();

    // On child change, update parent
    $('.pdf-generator ul li ul li input').change(function() {
        setStateByChildren.call($('> input', $(this).parents('.pdf-generator > form > ul > li')));
        setRootState();
    });

    // On parent click, update parent and children
    // This is done in a change handler because click handlers are a nightmare when you're interfering with the click result
    $('.pdf-generator > form > ul > li > input').change(function() {
        unchecked = $('> ul > li > input:not(:checked)', $(this).parent());
        if(unchecked.length > 0) {
            // If any children are unchecked, check them all
            unchecked.prop('checked', true);
            this.checked = true;
        } else {
            // Otherwise uncheck everything
            $('input:checked', $(this).parent()).prop('checked', false);
        }
    });

    // On title click, check/uncheck everything
    $('.pdf-generator .title input').change(function() {
        $('.pdf-generator ul li input:not(:disabled)').prop('checked', this.checked).prop('indeterminate', false);
        setRootState();
    });

    /*
    $('#go-button').click(function() {
        choices = $('.option').map(function() {
            opt = $(this);
            console.log(opt);
            return opt.hasClass('disabled') ? null : opt.text().toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/-+$/, '');
        });
        //document.location = '/resume.pdf?' + choices.get().join('&');
    });
    */

    $('#cancel-button').click(function(e) {
        e.preventDefault();
        document.location = '/';
    });
});