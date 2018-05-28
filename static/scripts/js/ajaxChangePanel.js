/**
 * Animacja przejścia między rejestracją, a logowaniem
 * @param where
 */
function showPanel(what) {
    console.log('Include: ' + what);
    console.log('Animation: 0%');
    $("#include").animate({
            opacity: 0,
        }, {
            duration: 500,
            complete: function () {
                console.log('Animation: 50%');
                $("#include").load("/include/include_"+what, function () {
                    $("#include").animate({
                        opacity: '1'
                    }, 500);
                });
                console.log('Animation: 100%');
            }
        }
    );
}
