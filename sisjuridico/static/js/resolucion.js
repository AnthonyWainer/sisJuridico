$(".Bre").keyup(function(){
    $.get('busq_ajax_re',{'datos':$(this).val().toLowerCase()}, function(data){
        $(".resolucionU").empty().html(data);
    });
});