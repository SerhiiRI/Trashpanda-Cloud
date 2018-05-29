/**
 * Sprawdza czy użytkownik zalogowany
 * @type {boolean}
 */
var isSignIn = false;
if (localStorage.getItem('userID') != null) {
    if (getSession('googleID') == '') {
        window.localStorage.clear();
        clearSession();
        isSignIn = false;
    } else {
        localStorage.setItem('userPanel', 'open');
        isSignIn = true;
    }
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
    var token = googleUser.getAuthResponse().id_token;
    // Wywołanie zmian po zalogowaniu
    localStorage.setItem('userID', profile.getId());
    localStorage.setItem('userPic', profile.getImageUrl());
    let x = profile.getFamilyName();
    localStorage.setItem('userName', profile.getGivenName() + " " + x[0] + ".");
    isSignIn = true;
    knockknock(profile.getId(), localStorage.getItem('userName'), profile.getEmail(), token, profile.getImageUrl());
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
    clearSession();
    goTo('/');
}

/**
 * Zmiana w interfejsie po zalogowaniu
 * */
function afterlogin() {
    if (localStorage.getItem('userPanel') == 'open') {
        console.log('Update user panel.')
        document.getElementById("userinfo").style.display = "initial";
        document.getElementById("userimg").src = localStorage.getItem('userPic');
        document.getElementById("username").innerHTML = localStorage.getItem('userName');
        localStorage.setItem('signed', 'true');
    }
}

/**
 * Testowe logowanie
 * */
function loginTest() {
    knockknock(testID, testName, testEmail, testToken, testPic);
}

/**
 * Sprawdź czy użytkownik istnieje
 * Zaloguj lub zarejestruj
 * @param ID
 * @param Name
 * @param Email
 * @param Token
 * @param Pic
 */
function knockknock(gid, name, email, token, pic) {
    console.log("Run Auth.");
    $.ajax({
            method: 'POST',
            url: 'registry',
            data: {
                'action': 'auth',
                'gid': gid,
            },
            success: function (response) {
                console.log("Auth: " + response.auth)
                if (response.auth == true) {
                    localStorage.setItem('userID', gid);
                    localStorage.setItem('userPic', pic);
                    localStorage.setItem('userName', name);
                    if (localStorage.getItem('userPanel') != 'open') {
                        closeLoginForm();
                    }
                } else {
                    if (confirm("Nie widzieliśmy Cię tu wcześniej drogi szopie. Chcesz do nas dołączyć?")) {
                        $.ajax({
                            method: 'POST',
                            url: 'registry',
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
                        localStorage.clear();
                        txt = "No to może innym razem. Trzym się <(^ u ^)/";
                        closeLoginForm();
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
    if (localStorage.getItem('userPanel') == 'open') {
        document.getElementById("isSignIn").innerText = "My Trashbox";
        var LBTN = document.getElementById("logoutBTN");
        if (LBTN == null) {
            let btn = document.createElement("BUTTON");
            btn.id = "logoutBTN";
            btn.className = "alx-btn";
            btn.innerText = "Wyloguj";
            btn.addEventListener("click", logout);
            document.getElementById("func-btn").appendChild(btn);
        }
        isSignIn = true;
    }
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
    if (localStorage.getItem('userPanel') == 'open') {
        goTo('mytrashbox');
    } else {
        showPanel('googleID');
    }
}

/**
 * Zamknij okno logowania
 * */
function closeLoginForm() {
    goTo('/');
}
