// Skrypt animacji wysuwania paska nav i footer
var menu = {'nav': false, 'foo': false};

//console.log(menu['nav']);
function fooAct(what, where) {
    if (menu[what] == false) {
        if (what == 'nav') {
            document.getElementById(what).style = where + ": 0px";
            document.getElementById(what).style.height = "70px";
            document.getElementById('nav-inside').style.display = 'initial';
            document.getElementById('nav-inside').style.opacity = '1';
            menu[what] = true;
        } else if (what == 'foo') {
            document.getElementById(what).style = where + ": 0px";
            document.getElementById(what).style.height = "40px";
            document.getElementById('foo-inside').style.display = 'initial';
            document.getElementById('foo-inside').style.opacity = '1';
            menu[what] = true;
        }
    } else {
        if (what == 'nav') {
            document.getElementById(what).style = where + ": -75px";
            document.getElementById(what).style.height = "100px";
            document.getElementById('nav-inside').style.opacity = '0';
            setTimeout(function () {
                document.getElementById('nav-inside').style.display = 'none';
            }, 500);
            menu[what] = false;
        } else if (what == 'foo') {
            document.getElementById(what).style = where + ": -75px";
            document.getElementById(what).style.height = "100px";
            document.getElementById('foo-inside').style.opacity = '0';
            setTimeout(function () {
                document.getElementById('foo-inside').style.display = 'none';
            }, 500);
            menu[what] = false;
        }
    }
}
