document.getElementById('body').style.transition = "all 500ms";

function goTo(where) {
    document.getElementById('body').style.opacity = "0";
    setTimeout(function () {
        window.location.replace(where);
    }, 500);
}