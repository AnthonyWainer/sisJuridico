function repor(a){
    $.post("reportes_consolidados/", {'fecha_ter':$(a).val(),'fecha_ini':$("#fecha_ini").val(),'csrfmiddlewaretoken':$("[name='csrfmiddlewaretoken']").val()}, function(data){
        $(".rep").empty().html(data);
    });    
}
