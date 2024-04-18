$(document).ready(function () {
    $("#bookNow").click(function (e) {
        e.preventDefault();
        // Get the start and end dates from the form
        var startDate = sessionStorage.getItem('startDate');
        var endDate = sessionStorage.getItem('endDate');
        let id = searchParams.get('id')
        window.location.href = $(this).attr("href") + '?id=' + id + '&startDate=' + encodeURIComponent(startDate) + '&endDate=' + encodeURIComponent(endDate);;;
    });
});
