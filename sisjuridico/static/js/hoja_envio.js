function sel(id){
    $.post('registro_hoja_envio/','csrfmiddlewaretoken='+$("[name='csrfmiddlewaretoken']").val()+'&idc='+id, function(data) {
        $(".hoja_envioU").empty().html(data);
    });
}

$(".selEx").change(function(){
    sel($(this).val());
});

