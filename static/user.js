$(document).ready(function() {
    $("#startdate").change(function () {
        // Get the start and end dates from the form
        var startDate = $('#startDate').val();
        var endDate = $('#endDate').val();
        sessionStorage.setItem('startDate', startDate)
        sessionStorage.setItem('endDate', endDate)
        console.log(startDate,endDate)
    })
    $("#enddate").change(function () {

    })
});

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
});
