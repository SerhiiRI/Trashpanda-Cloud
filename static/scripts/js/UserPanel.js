/**
 *  Włączenie panelu użytkownika
 *  */
afterlogin();
function afterlogin() {
    //Zmiana widoczności panelu użytkownika
    document.getElementById("userinfo").style.display = "flex";
    document.getElementById("userimg").src = localStorage.getItem('userPic');
    document.getElementById("username").innerHTML = localStorage.getItem('userName');
}

/**
 * Google wylogowanie
 * */
function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
        console.log('User signed out.');
    });
    window.localStorage.clear();
    goTo('/');
}