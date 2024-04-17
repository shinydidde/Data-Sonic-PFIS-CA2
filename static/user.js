// $(document).ready(function() {
//     $('#startdate').on('change', function() {
//         var startDate = new Date($(this).val());
//         var minEndDate = new Date(startDate.getTime() + (24 * 60 * 60 * 1000)); // Add 1 day to start date
//         $('#enddate').attr('min', minEndDate.toISOString().split('T')[0]); // Set min date for end date
//     });

//     // Prevent user from selecting previous dates for start date
//     var today = new Date().toISOString().split('T')[0];
//     $('#startdate').attr('min', today);
// });

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
