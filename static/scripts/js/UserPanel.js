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
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
        console.log('User signed out.');
        clearListCookies();
    });
    goTo('/')
    //window.location.replace('https://www.google.com/accounts/Logout?continue=https://appengine.google.com/_ah/logout?continue=http://trashpanda.pwsz.nysa.pl');
}

function clearListCookies()
{
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++)
    {
        var spcook =  cookies[i].split("=");
        deleteCookie(spcook[0]);
    }
    function deleteCookie(cookiename)
    {
        var d = new Date();
        d.setDate(d.getDate() - 1);
        var expires = ";expires="+d;
        var name=cookiename;
        //alert(name);
        var value="";
        document.cookie = name + "=" + value + expires + "; path=/acc/html";
    }
    window.location = ""; // TO REFRESH THE PAGE
}

loginTest();

function loginTest() {
    userID = 123456789;
    userPic = '/static/pic/testpic.jpg';
    let x = 'Kowalski';
    userName = "Jan" + " " + x[0] + ".";
    afterlogin();
}
