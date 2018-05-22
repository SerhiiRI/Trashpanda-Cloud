/**
 * Wyświetl menu opcji dla wybranego z listy elementu
 */

var pop = document.getElementById("popmenu");

/* Wyświetla mneu opcji dla elementu z listy w trashbox */
function openmenu() {
    var eventy = (event.clientY - 17) + 'px';
    pop.style.top = eventy;
    anim;
    var anim = setInterval(function () {
        pop.style.right = '10px';
        clearInterval(anim);
    }, 150);
}

/* Zamknięcie menu opcji */
function closemenu() {
    pop.style.right = -450 + 'px';
    console.log('close');
}

/* Przekazanie parametru odnośnie katalogu, po którym wyświetlone zostaną dane wybranego katalogu */
function openfile(link) {
    window.location.href = '/trash/' + link;
}
