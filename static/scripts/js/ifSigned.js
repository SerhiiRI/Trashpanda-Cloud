var back = true;

if (localStorage.getItem('loginTest')) {
    console.log(localStorage.getItem('loginTest'));
    console.log("Fake Login Active");
    back = false;
} else {
    onSignIn();
}

if (back == true) {
    console.log(back);
    window.localStorage.clear();
    window.location.href = ("/");
}

function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    var issetID = profile.getId();
    back = false;
    console.log("Logowanie przez Google");
}

