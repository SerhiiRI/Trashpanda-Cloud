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
        document.getElementById("userinfo").style.display = "initial";
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
            location.reload();
        });
    }