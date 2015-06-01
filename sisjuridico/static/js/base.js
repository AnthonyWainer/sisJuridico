//csrf_token = $("input[name='csrfmiddlewaretoken']").val();
function guardar(url,n){
    $.post(url,$('#formulario'+n).serialize()+'&id='+$(".guar").attr('id'), function(data) {
        $('#Modal'+n).modal('hide');
        $('#Modal'+n).on('hidden.bs.modal', function (e) {
            $("table tbody").empty().html(data);
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
function eliminar(id,u){
    $.get(u,{'id':id}, function(data) {
       $("table tbody").empty().html(data);    
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