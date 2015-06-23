function sel(id){
    $.post('registro_expediente/','csrfmiddlewaretoken='+$("[name='csrfmiddlewaretoken']").val()+'&idc='+id, function(data) {
        $(".expedienteU").empty().html(data);
    });
}

$(".selEx").change(function(){
    sel($(this).val());
});

