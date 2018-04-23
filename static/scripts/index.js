
    /**
     * Przekierowanie na inny adres podany w where
     * */
    function goTo(where) {
        window.location.replace(where);
    }

    /**
     * Zmienne testowe
    //  * */
    var isSignIn = false;
    // var userID = 1234567890;
    // var userPic = "https://lh5.googleusercontent.com/-p-7kqdTngmk/AAAAAAAAAAI/AAAAAAAAAkA/LS9olK6iiME/s96-c/photo.jpg";
    // var userName = "Aleks";

    /**
     * Google SignIn / funkcja wywołana po zalogowaniu
     * */
    function onSignIn(googleUser) {
        // Useful data for your client-side scripts:
        var profile = googleUser.getBasicProfile();
        console.log("ID: " + profile.getId()); // Don't send this directly to your server!
        console.log('Full Name: ' + profile.getName());
        console.log('Given Name: ' + profile.getGivenName());
        console.log('Family Name: ' + profile.getFamilyName());
        console.log("Image URL: " + profile.getImageUrl());
        console.log("Email: " + profile.getEmail());

        // The ID token you need to pass to your backend:
        var id_token = googleUser.getAuthResponse().id_token;
        console.log("ID Token: " + id_token);

        // Wywołanie zmian po zalogowaniu
        userID = profile.getId();
        userPic = profile.getImageUrl();
        let x = profile.getFamilyName();
        userName = profile.getGivenName() + " " + x[0] + ".";
        isSignIn = true;
        closeLoginForm();
        afterlogin();
        loginButton();
    };

    /**
     * Google wylogowania
     * */
    function signOut() {
        var auth2 = gapi.auth2.getAuthInstance();
        auth2.signOut().then(function () {
            console.log('User signed out.');
        });
    }

    /**
    * Zmiana w interfejsie po zalogowaniu
    * */
    function afterlogin() {
        document.getElementById("userinfo").style.display = "initial";
        document.getElementById("userimg").src = userPic;
        document.getElementById("username").innerHTML = userName;
    }

    /**
    * Testowe logowanie
    // * */
    // function loginTest() {
    //     afterlogin();
    //     isSignIn = true;
    //     loginButton();
    //     closeLoginForm();
    // }

    /**
    *Edycja przycisku logowania i wylogowania
    * */
    function loginButton() {
        if (isSignIn) {
            document.getElementById("isSignIn").innerText = "My Trashbox";
            let btn = document.createElement("BUTTON");
            btn.className = "alx-btn";
            btn.innerText = "Wyloguj";
            btn.addEventListener("click", logout);
            document.getElementById("func-btn").appendChild(btn);
        } else {
            document.getElementById("isSignIn").innerText = "Zaloguj się";
        }
    }

    /**
     * Funkcja wylogowania
     * */
    function logout() {
        signOut();
        isSignIn = false;
        location.reload();
    }

    /**
     * Otwórz okno logowania
     * */
    var glogin = document.getElementById("alx-gbtn");
    function openLoginForm() {
        if (isSignIn) {
            alert("My Trashbox will be able soon!");
        } else {
            glogin.style.transition = "all 200ms";
            glogin.style.opacity = "1";
            glogin.style.zIndex = "10";
        }
    }

    /**
     * Zamknij okno logowania
     * */
    function closeLoginForm() {
        glogin.style.opacity = "0";
        glogin.style.zIndex = "-10";
    }
