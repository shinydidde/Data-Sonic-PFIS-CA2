$("#bookNow").click(function(e) {
    e.preventDefault();
    // Get the start and end dates from the form
    var startDate = sessionStorage.getItem('startDate');
    var endDate = sessionStorage.getItem('endDate');
    window.location.href = $(this).attr("href") + encodeURIComponent(startDate) + '&endDate=' + encodeURIComponent(endDate);;;
});
