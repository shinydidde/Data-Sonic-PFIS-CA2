document.addEventListener('DOMContentLoaded', function() {
    flatpickr('#startdate', {
        minDate: 'today',
        onChange: function(selectedDates, dateStr) {
            var minEndDate = new Date(selectedDates[0].getTime() + (24 * 60 * 60 * 1000));
            flatpickr('#enddate', {
                minDate: minEndDate,
                // defaultDate: minEndDate,
            });
        }
    });

    flatpickr('#enddate', {
        minDate: 'today',
    });

    $('#availability-form').submit(function (event) {
        if ($('#startdate').val() && $('#enddate').val()) {
            // If the form is not valid, prevent default form submission
            event.preventDefault();
            alert('Please fill the check in and heck out dates')
        } else {
            // If the form is valid, you can proceed with form submission
            console.log('Form submitted successfully!');
            $(this).unbind('submit').submit();
        }

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

    $('a.details-button').each(function() {
        var href = this.href;
         // Get the start and end dates from the form
         var startDate = sessionStorage.getItem('startDate');
         var endDate = sessionStorage.getItem('endDate');
         href = href + '&startDate=' + encodeURIComponent(startDate) + '&endDate=' + encodeURIComponent(endDate);;
        $(this).attr('href', href);
      });
});
