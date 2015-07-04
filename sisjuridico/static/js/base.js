function vali(data,n,u){
                    $('.modalP').append("<div id='h' ></div>");
                $("#h").css("display","none");
                $("#h").empty().html(data);
                if($('#h ul').hasClass('errorlist')){
                    $("#h").empty();
                    $('#formulario'+n).empty().html(data);
                    $('.errorlist').css("display","none");
                    $('[data-toggle="popover"]').popover('show');
                    $('.popover').css('border','1px dashed red');
                    $('.popover-content').css('padding','2px 4px');
                    AlDelete("error al guardar");
        $(".chosen-select").chosen(); 
        $(".chosen-container").css("width","100%");                    
                }else{
                    $('#Modal'+n).modal('hide');
                    $('#Modal'+n).on('hidden.bs.modal', function (e) {
                        $("table ."+u).empty().html(data);
                        AlSave("guardado con éxito");  
                    });
                }  
}

function guardar(url,n,u){
    $.post(url,$('#formulario'+n).serialize()+'&id='+$(".guar").attr('id'), function(data) {
        vali(data,n,u);
    });
}


function actualizar(id,u,n){
    $.get(u,{'id':id}, function(data) {
        $(".modalP").empty().html(data);
        $(".guar").attr('id',id)
        $('#Modal'+n).modal('show');
        $(".chosen-select").chosen(); 
        $(".chosen-container").css("width","100%");
    });
}
function eliminar(id,u,n){
    $.get(u,{'id':id}, function(data) {
       $("table ."+n).empty().html(data);    
       AlDelete("Eliminado");  
    });
}


function mod(id){
    $("#"+id+" input").prop( "checked", true );
    $.get('registro_submodulo',{'id':id}, function(data) {
       $("table .SubModuloU").empty().html(data);    
    });
}


function passDefault(id) {
    $.get('passDefault/',{'id':id}, function(data) {
       $("table .UserU").empty().html(data);    
       AlSave("Contraseña Cambiada por Defecto");
    });
}

//para subir archivos con ajax
function guardarF(url,n,u){
    formData = new FormData($('#formulario'+n)[0]);
    formData.append('id', $(".guar").attr('id'));
        $.ajax({
            url: url,  
            type: 'POST',
            data: formData,
            //necesario para subir archivos via ajax
            cache: false,
            contentType: false,
            processData: false,

            success: function(data){
                vali(data,n,u);
            }

        });

}

function paginacion(url,nro){
    pag=$('#selP').val();
    $.get(url,{'page':nro,'pag':pag}, function(data){
        $( '#result' ).empty().html(data);
    });
}
function pag(a,url){
    paginacion(url,$(a).val());
}

function nroPag(a,url){
    $.get(url,{'pag':$(a).val()}, function(data){
        $( '#result' ).empty().html(data);
    });
}