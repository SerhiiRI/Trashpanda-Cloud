if (localStorage.getItem('signed') != null) {
    console.log("Login Active");
} else {
    window.localStorage.clear();
    window.location.href = ("/");
}
