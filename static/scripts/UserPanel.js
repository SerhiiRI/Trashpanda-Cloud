
    // var userPic = "https://lh5.googleusercontent.com/-p-7kqdTngmk/AAAAAAAAAAI/AAAAAAAAAkA/LS9olK6iiME/s96-c/photo.jpg";
    // var userName = "Aleks";
    // afterlogin();

function onSignIn(googleUser) {
        // Useful data for your client-side scripts:
        var profile = googleUser.getBasicProfile();
        // The ID token you need to pass to your backend:
        var id_token = googleUser.getAuthResponse().id_token;
        // Uzupełnienei panelu użytkownika
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
