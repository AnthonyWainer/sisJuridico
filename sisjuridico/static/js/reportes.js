function repor(){
    $.post("reportes_consolidados/", {'fecha_ter':$("#fecha_ter").val(),'fecha_ini':$("#fecha_ini").val(),'csrfmiddlewaretoken':$("[name='csrfmiddlewaretoken']").val(),'v':'c'}, function(data){
        $(".rep").empty().html(data);
    }); 
    $.post("reportes_consolidados/", {'fecha_ter':$("#fecha_ter").val(),'fecha_ini':$("#fecha_ini").val(),'csrfmiddlewaretoken':$("[name='csrfmiddlewaretoken']").val(),'v':'v'}, function(data){
        var plotObj = $.plot($("#flot-pie-chart"), data, {
            series: {
                pie: {
                    show: true
                }
            },
            grid: {
                hoverable: true
            },
            tooltip: true,
            tooltipOpts: {
                content: "%p.0%, %s", // show percentages, rounding to 2 decimal places
                shifts: {
                    x: 20,
                    y: 0
                },
                defaultTheme: false
            }
        });
    });    
}

//Flot Pie Chart

 /*   var data = [{
        label: "Aprobado",
        data: 21,
        color: "#d3d3d3",
    }, {
        label: "No Aprobado",
        data: 15,
        color: "#79d2c0",
    }, {
        label: "En Proceso",
        data: 52,
        color: "#1ab394",
    }];*/



