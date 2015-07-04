function sel(id){
    $.post('registro_hoja_envio/','csrfmiddlewaretoken='+$("[name='csrfmiddlewaretoken']").val()+'&idc='+id, function(data) {
        $(".hoja_envioU").empty().html(data);
    });
}
$(".chosen-select").chosen(); 
$(".chosen-container").css("width","100%");

$(".selEx").change(function(){
    sel($(this).val());
});

