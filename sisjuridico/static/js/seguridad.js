$(".perf").click(function(){
    $.get("registro_perfil",$('#formulario').serialize(), function(data) {
        $('#Modal').modal('hide');
        $('#Modal').on('hidden.bs.modal', function (e) {
            cargar(li);
        });
        
    });
});

function eliminarPerfil(id,u){
    $.get(u,{'id':id}, function(data) {
            cargar(li);       
    });
}