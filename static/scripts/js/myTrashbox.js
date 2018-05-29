/**
 * Open pop menu
 * @param tag
 * @param path
 */
function openmenu(tag, path) {
    console.log(tag)
    console.log(path)
    $('#' + tag).css({
        'display': 'flex',
        'top': (event.clientY - 17) + 'px',
        'left': (event.clientX - 100) + 'px',
        'width': '200px'
    });
    $('#' + tag).animate({
        opacity: 1,
        left: (event.clientX - 150) + 'px',
    }, {duration: 500});
    console.log('pop open');
}

/* Zamknięcie menu opcji */
function closemenu(tag) {
    $('#' + tag).css({
        'display': 'none',
        'opacity': '0'
    });
    console.log('pop close');
}
