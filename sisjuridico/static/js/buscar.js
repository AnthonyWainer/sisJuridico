function Buscar(url,n){
    $.post(url,$("#formulario"+n).serialize(), function(data){
        $("."+n).empty().html(data);
    });

}