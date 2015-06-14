function sel(id){
    $.post('registro_permisos/','csrfmiddlewaretoken='+$("[name='csrfmiddlewaretoken']").val()+'&id='+id, function(data) {
        $(".PermisosU").empty().html(data);
    });
}

$(".selPer").change(function(){
    sel($(this).val());
});


function cambiar(u,es,url,id){
    $.get(u,'e='+es+'&url='+url+'&id='+id);
    AlSave("actualizado correctamente");
}