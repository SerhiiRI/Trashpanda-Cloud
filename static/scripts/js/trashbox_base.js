    // Skrypt animacji wysuwania paska nav i footer
    var menu = {'nav' : false, 'foo' : false};
    //console.log(menu['nav']);
    function fooAct(what, where) {
        if(menu[what] == false) {
            if(what == 'nav') {
            document.getElementById(what).style = where + ": 0px";
            menu[what] = true;
            }else if(what == 'foo') {
                document.getElementById(what).style = where + ": 0px";
                document.getElementById(what).style.height = "40px";
                menu[what] = true;
            }
        }else{
            if(what == 'nav') {
                document.getElementById(what).style = where + ": -45px";
                menu[what] = false;
            }else if(what == 'foo'){
                document.getElementById(what).style = where + ": -45px";
                document.getElementById(what).style.height = "60px";
                menu[what] = false;
            }
        }
    }