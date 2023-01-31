$(document).ready(function(){

    $("#dist").change(function(){
        var seldist=$(this).children("option:selected").val()
        $.ajax({
            url:'get_branch',
            type:'get',
            data:{
                district:seldist
            },
            success: function(data){
                    $("#brc").html(data);
                    $("#brc").selectedIndex(0);
            }

        });

    });
});