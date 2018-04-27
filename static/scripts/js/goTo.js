/**
 * Funkcja przekierowuje na inną stronę,
 * dodatkowo zmniejszając opacity do 0
 * przed przekierowaniem (animacja)
 * @type {string}
 */
this.document.body.style.transition = "all 500ms";

function goTo(where) {
    this.document.body.style.opacity = "0";
    setTimeout(function () {
        window.location.replace(where);
    }, 500);
}
