$(document).ready(function(){
    $(".update-room").click(function(){
        $(".change-title").text('Edit Room');
        $("#roomtype").attr('style','display:none');
        var roomtype = $(this).data('roomtype');
        var occupancy = $(this).data('occupancy');
        var roomprice = $(this).data('roomprice');
        var available = $(this).data('available');
        var roomimage = $(this).data('roomimage');
        var roomtitle = $(this).data('roomtitle');
        var roomdesc = $(this).data('roomdesc');

        $("#roomtype").val(roomtype);
        $("#occupancy").val(occupancy);
        $("#roomprice").val(roomprice);
        $("#available").val(available);
        $("#roomimage").val(roomimage);
        $("#roomtitle").val(roomtitle);
        $("#roomdesc").val(roomdesc);
        $("#type").val('update');
        $("#data-form").show();
    });
    $(".delete-room").click(function(){
        var roomtype = $(this).data('roomtype');
        $("#roomtype").val(roomtype);
        $("#type").val('remove');
        $("#data-form").submit();
    });
    $(".add-room").click(function(){
        $(".change-title").text('Add Room');
        $("#roomtype").removeAttr('disabled');
        $('#data-form')[0].reset();
        $("#type").val('add');
    });
});
