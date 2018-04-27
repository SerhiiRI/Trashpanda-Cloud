function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    var id_token = googleUser.getAuthResponse().id_token;
    userID = profile.getId();
    userPic = profile.getImageUrl();
    let x = profile.getFamilyName();
    userName = profile.getGivenName() + " " + x[0] + ".";
    afterlogin();
}

function afterlogin() {
    //Zmiana widoczności panelu użytkownika
    document.getElementById("userinfo").style.display = "flex";
    document.getElementById("userimg").src = userPic;
    document.getElementById("username").innerHTML = userName;
}

/**
 * Google wylogowania
 * */
function signOut() {
    function signOut() {
        var auth2 = gapi.auth2.getAuthInstance();
-           auth2.signOut().then(function () {
-           console.log('User signed out.');
-    });
-    goTo('/')
        //window.location.replace('https://www.google.com/accounts/Logout?continue=https://appengine.google.com/_ah/logout?continue=http://trashpanda.pwsz.nysa.pl');
    }
}

loginTest();

function loginTest() {
    userID = 123456789;
    userPic = '/static/pic/testpic.jpg';
    let x = 'Kowalski';
    userName = "Jan" + " " + x[0] + ".";
    afterlogin();
}
