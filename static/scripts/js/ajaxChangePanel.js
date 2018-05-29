/**
 * Animacja przejścia między rejestracją, a logowaniem
 * @param where
 */
function showPanel(what) {
    console.log('Include: ' + what);
    console.log('Animation: 0%');
    if (document.getElementById('btnAction')) {
        document.getElementById('btnAction').innerHTML = '<img src="../static/pic/spinner.gif" style="width: 75px">';
    }
    if (document.getElementById('loading_screen')) {
        document.getElementById('loading_screen').style.display = 'block';
    }
    $("#include").animate({
            opacity: 0,
        }, {
            duration: 500,
            complete: function () {
                console.log('Animation: 50%');
                $("#include").load("/include/include_" + what, function () {
                    $("#include").animate({
                        opacity: '1'
                    }, 500);
                });
                console.log('Animation: 100%');
            }
        }
    );
}

/**
 * Animacja przejścia między rejestracją, a logowaniem
 * @param where
 */
function showPanelPost(what, item1) {
    console.log('Include: ' + what + '_with: ' + item1);
    console.log('Animation: 0%');
    if (document.getElementById('btnAction')) {
        document.getElementById('btnAction').innerHTML = '<img src="../static/pic/spinner.gif" style="width: 75px">';
    }
    if (document.getElementById('loading_screen')) {
        document.getElementById('loading_screen').style.display = 'block';
    }
    $("#include").animate({
            opacity: 0,
        }, {
            duration: 500,
            complete: function () {
                console.log('Animation: 50%');
                $("#include").load("/include/include_" + what, {'attr1': item1}, function () {
                    $("#include").animate({
                        opacity: '1'
                    }, 500);
                });
                console.log('Animation: 100%');
            }
        }
    );
}

function redirectIF() {
    if (document.getElementById('include')) {
        console.log('Stop redirect.')
        if (document.getElementById('loading_screen')) {
            document.getElementById('loading_screen').style.display = 'none';
        }
    } else {
        window.location.href = '/';
    }
}
