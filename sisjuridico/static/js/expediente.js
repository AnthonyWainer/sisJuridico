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