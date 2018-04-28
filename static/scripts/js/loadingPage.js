
function loadingPage(googleID) {
    $.ajax({
        data: {
            gid: googleID
        },
        type: 'POST',
        url: "/loadingTrashbox",
    }).done(function (data) {
        var page = data.load;
        console.log(page);
        document.getElementById('loadContent').innerHTML = page;
    });
}