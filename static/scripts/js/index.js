/**
 * Sprawdza czy użytkownik zalogowany
 * @type {boolean}
 */
var isSignIn = false;
if (localStorage.getItem('userID') != null) {
    afterlogin();
    loginButton();
}

/**
 * Dane testowe do trybu offline
 */
var testID = "1234567890";
var testPic = "https://lh5.googleusercontent.com/-p-7kqdTngmk/AAAAAAAAAAI/AAAAAAAAAkA/LS9olK6iiME/s96-c/photo.jpg";
var testName = "Aleks S.";


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
    setSession('googleID', profile.getId());
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
    goTo('/');
}

/**
 * Zmiana w interfejsie po zalogowaniu
 * */
function afterlogin() {
    document.getElementById("userinfo").style.display = "initial";
    document.getElementById("userimg").src = localStorage.getItem('userPic');
    document.getElementById("username").innerHTML = localStorage.getItem('userName');
}

/**
 * Testowe logowanie
 * */
function loginTest() {
    localStorage.setItem('userID', testID);
    localStorage.setItem('userPic', testPic);
    localStorage.setItem('userName', testName);
    localStorage.setItem('loginTest', 'true');
    setSession('googleID', testID);
    closeLoginForm();
    afterlogin();
    loginButton();
}

/**
 *Edycja przycisku logowania i wylogowania
 * */
function loginButton() {
    if (isSignIn == false) {
        document.getElementById("isSignIn").innerText = "My Trashbox";
        let btn = document.createElement("BUTTON");
        btn.className = "alx-btn";
        btn.innerText = "Wyloguj";
        btn.addEventListener("click", logout);
        document.getElementById("func-btn").appendChild(btn);
        isSignIn = true;
    }
}

/**
 * Funkcja wylogowania
 * */
function logout() {
    window.localStorage.clear();
    isSignIn = false;
    signOut();
    goTo('/');
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
