  function userBlock(id,ni){
    $.post('user_block/','csrfmiddlewaretoken='+$("[name='csrfmiddlewaretoken']").val()+'&id='+id+'&ni='+ni, function(data) {
      $("table .ublock").empty().html(data);
      if(ni != 5){
        AlSave("usuario desbloqueado");
      }else{
        AlDelete("usuario bloqueado");
      }
       
    });
      
  }
  $(".Bo").keyup(function(){
    $.get('busq_ajax_us/',{'datos':$(this).val().toLowerCase(),'d':'v'}, function(data){
        $(".ublock").empty().html(data);
    });
  });
  $(".selus").change(function(){
    $.get('busq_ajax_us/',{'datos':$(this).val().toLowerCase(),'d':'b'}, function(data){
        $(".ublock").empty().html(data);
    });
  });