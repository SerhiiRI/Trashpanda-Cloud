/* Usunięcie przezroczystości stony (animacja pojawiania się strony) */
window.onload = function () {
    this.document.body.style.opacity = "1";
};

/**
 * Funkcja przekierowuje na inną stronę,
 * dodatkowo zmniejszając opacity do 0
 * przed przekierowaniem (animacja)
 * @type {string}
 */
function goTo(where) {
    this.document.body.style.opacity = "0";
    setTimeout(function () {
        window.location.href = where;
    }, 500);
}
