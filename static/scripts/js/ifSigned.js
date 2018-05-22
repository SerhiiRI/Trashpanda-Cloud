var redirectPlease = true;
if (localStorage.getItem('loginTest')) {
    console.log(localStorage.getItem('loginTest'));
    console.log("Fake Login Active");
    redirectPlease = false;
} else {
    function onSignIn(googleUser) {
        var profile = googleUser.getBasicProfile();
        var issetID = profile.getId();
        if (issetID) {
            redirectPlease = false;
        }
        console.log("Logowanie przez Google");
    }
}
if (redirectPlease) {
    window.localStorage.clear();
    window.location.href = ("/");
}