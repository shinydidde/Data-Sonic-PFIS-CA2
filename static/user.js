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
    $("#startDate").change(function () {
        var startDate = $('#startDate').val();
        sessionStorage.setItem('startDate', startDate)
        console.log(startDate)
    })
    $("#endDate").change(function () {
        var endDate = $('#endDate').val();
        sessionStorage.setItem('endDate', endDate)
        console.log(endDate)
    })
});
