
function loadingPage(googleID, path) {
    $.ajax({
        data: {
            gid: googleID,
            path: path
        },
        type: 'POST',
        url: "/loadingTrashbox",
    }).done(function (data) {
        var page = data.load;
        console.log(page);
        document.getElementById('loadContent').innerHTML = page;
    });
}