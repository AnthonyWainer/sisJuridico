function guardarExp(t,url,n,u){
    var f = $(t);
    var formData = new FormData(document.getElementById("formul"));
    formData.append("dato", "valor");

    console.log(formData);
    /*$.post(url,$('#formulario'+n).serialize()+formData, function(data) {
        $('#Modal'+n).modal('hide');
        $('#Modal'+n).on('hidden.bs.modal', function (e) {
            $("table ."+u).empty().html(data);
            AlSave("guardado con éxito");  
        });
    });*/
}

$(".gg").click(function(){
    var formData = new FormData($("#formul")[0]);
    console.log(formData);

    $.ajax({
            url: 'registro_expediente/',  
            type: 'POST',
            // Form data
            //datos del formulario
            data: formData,
            //necesario para subir archivos via ajax
            cache: false,
            contentType: false,
            processData: false,

            success: function(data){
                $('#Modal').modal('hide');
                $('#Modal').on('hidden.bs.modal', function (e) {
                    $("table .expedienteU").empty().html(data);
                    AlSave("guardado con éxito");  
                });
            }

        });

});