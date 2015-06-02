//csrf_token = $("input[name='csrfmiddlewaretoken']").val();
function guardar(url,n,u){
    $.post(url,$('#formulario'+n).serialize()+'&id='+$(".guar").attr('id'), function(data) {
        $('#Modal'+n).modal('hide');
        $('#Modal'+n).on('hidden.bs.modal', function (e) {
            $("table ."+u).empty().html(data);
            AlSave("guardado con éxito");  
        });
        
    });
}
function actualizar(id,u,n){
    $.get(u,{'id':id}, function(data) {
        $(".modalP").empty().html(data);
        $(".guar").attr('id',id)
        $('#Modal'+n).modal('show');
    });
}
function eliminar(id,u,n){
    $.get(u,{'id':id}, function(data) {
       $("table ."+n).empty().html(data);    
       AlDelete("Eliminado");  
    });
}

function AlSave(msm){
    setTimeout(function() {
        toastr.options = {
         showMethod: 'slideDown',
         timeOut: 2000
        };
        toastr.success(msm);
    }, 300);
}
function AlDelete(msm){
    setTimeout(function() {
        toastr.options = {
         showMethod: 'slideDown',
         timeOut: 2000
        };
        toastr.error(msm);
    }, 300);
}

function mod(id){
    $("#"+id+" input").prop( "checked", true );
    $.get('registro_submodulo',{'id':id}, function(data) {
       $("table .SubModuloU").empty().html(data);    
    });
}

