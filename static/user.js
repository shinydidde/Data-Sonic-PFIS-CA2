$(document).ready(function(){
    $("#startdate").datepicker({
        dateFormat: 'yy-mm-dd',
        onSelect: function(selectedDate) {
            var endDate = $('#endDate');
            var startDate = $(this).datepicker('getDate');
            endDate.datepicker('option', 'minDate', startDate);
        }
    });

    $("#enddate").datepicker({
        dateFormat: 'yy-mm-dd',
        onSelect: function(selectedDate) {
            var startDate = $('#startDate');
            var endDate = $(this).datepicker('getDate');
            startDate.datepicker('option', 'maxDate', endDate);
        }
    });
});
