/**
 * Sprawdza czy użytkownik zalogowany
 * @type {boolean}
 */
var isSignIn = false;
if (localStorage.getItem('userID') != null) {
    afterlogin();
    isSignIn = true;
}

/**
 * Dane testowe do trybu offline
 */
var testID = "1234567890";
var testPic = "https://lh5.googleusercontent.com/-p-7kqdTngmk/AAAAAAAAAAI/AAAAAAAAAkA/LS9olK6iiME/s96-c/photo.jpg";
var testName = "Aleks S.";
var testEmail = "aleks@wp.pl";
var testToken = "102938xcvb47565xb6478bxcvb349021b";


/**
 * Google SignIn / funkcja wywołana po zalogowaniu
 * @param googleUser
 */
function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    token = googleUser.getAuthResponse().id_token;
    // Wywołanie zmian po zalogowaniu
    localStorage.setItem('userID', profile.getId());
    localStorage.setItem('userPic', profile.getImageUrl());
    let x = profile.getFamilyName();
    localStorage.setItem('userName', profile.getGivenName() + " " + x[0] + ".");
    isSignIn = true;
    closeLoginForm();
    afterlogin();
    loginButton();
}

/**
 * Google wylogowania
 * */
function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
        console.log('User signed out.');
    });
    window.localStorage.clear();
    goTo('/');
}

/**
 * Zmiana w interfejsie po zalogowaniu
 * */
function afterlogin() {
    document.getElementById("userinfo").style.display = "initial";
    document.getElementById("userimg").src = localStorage.getItem('userPic');
    document.getElementById("username").innerHTML = localStorage.getItem('userName');
    localStorage.setItem('signed', 'true');
}

/**
 * Testowe logowanie
 * */
function loginTest() {
    var gid = testID;
    var name = testName;
    var email = testEmail;
    var token = testToken;
    $.ajax({
            method: 'POST',
            url: 'registry',
            async: false,
            data: {
                'action': 'auth',
                'gid': gid,
            },
            success: function (response) {
                console.log("Auth: " + response.auth)
                if (response.auth == true) {
                    localStorage.setItem('userID', testID);
                    localStorage.setItem('userPic', testPic);
                    localStorage.setItem('userName', testName);
                    closeLoginForm();
                    afterlogin();
                    loginButton();
                } else {
                    if (confirm("Nie widzieliśmy Cię tu wcześniej drogi szopie. Chcesz do nas dołączyć?")) {
                        $.ajax({
                            method: 'POST',
                            url: 'registry',
                            async: false,
                            data: {
                                'action': 'registry',
                                'gid': gid,
                                'name': name,
                                'email': email,
                                'token': token,
                            },
                            success: function (response) {
                                txt = response.res;
                                closeLoginForm();
                            },
                            error: function (error) {
                                txt = "Niestety coś poszło nie tak, spróbuj innym razem ; - ;";
                                console.log("Błąd przy rejestracji!")
                            }
                        });
                    } else {
                        txt = "No to może innym razem. Trzym się <(^ u ^)/";
                    }
                    alert(txt);
                }
            }
            ,
            error: function (error) {
                console.log("Nie autoryzowano.")
            }
        }
    );
}

/**
 *Edycja przycisku logowania i wylogowania
 * */
function loginButton() {
    document.getElementById("isSignIn").innerText = "My Trashbox";
    let btn = document.createElement("BUTTON");
    btn.className = "alx-btn";
    btn.innerText = "Wyloguj";
    btn.addEventListener("click", logout);
    document.getElementById("func-btn").appendChild(btn);
    isSignIn = true;
}

/**
 * Funkcja wylogowania
 * */
function logout() {
    isSignIn = false;
    signOut();
}

/**
 * Otwórz okno logowania
 * */
var glogin = document.getElementById("alx-gbtn");

function openLoginForm() {
    if (isSignIn) {
        goTo('mytrashbox')
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
