$(".Bct").keyup(function(){
    $.get('busq_ajax_ct',{'datos':$(this).val().toLowerCase()}, function(data){
        $(".categoriaU").empty().html(data);
    });
});