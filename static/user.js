document.addEventListener('DOMContentLoaded', function() {
    flatpickr('#startdate', {
        minDate: 'today',
        onChange: function(selectedDates, dateStr) {
            var minEndDate = new Date(selectedDates[0].getTime() + (24 * 60 * 60 * 1000));
            flatpickr('#enddate', {
                minDate: minEndDate,
                defaultDate: minEndDate,
            });
        }
    });

    flatpickr('#enddate', {
        minDate: 'today',
    });

    // Get the start and end dates from the form
    $("#startdate").change(function () {
        var startDate = $('#startdate').val();
        sessionStorage.setItem('startDate', startDate)
    })
    $("#enddate").change(function () {
        var endDate = $('#enddate').val();
        sessionStorage.setItem('endDate', endDate)
    })

    $('#viewDetails').click(function(event) {
        event.preventDefault(); // Prevent form submission

        // Get the start and end dates from the form
        var startDate = sessionStorage.getItem('startDate');
        var endDate = sessionStorage.getItem('endDate');

        // Append the dates as query parameters to the action URL of the form
        var actionUrl = $(this).attr('href') + '?startDate=' + encodeURIComponent(startDate) + '&endDate=' + encodeURIComponent(endDate);

        // Redirect to the next page with the dates as query parameters
        window.location.href = actionUrl;
    });
});
