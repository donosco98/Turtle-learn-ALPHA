$(document).ready(function(){
    // Image block display function

    // $("#qimage").change(function () {
    //     if($("#qimage").val() == "yes"){
    //         $(".appearq").css("display", "block");
    //     }
    //     else{
    //         $(".appearq").css("display", "none");
    //     }
    // });

    // $("#questionimage1").change(function () {
    //     if($("#questionimage1").val() == "yes"){
    //         $(".appearop1").css("display", "block");
    //     }
    //     else{
    //         $(".appearop1").css("display", "none");
    //     }
    // });

    // $("#questionimage2").change(function () {
    //     if($("#questionimage2").val() == "yes"){
    //         $(".appearop2").css("display", "block");
    //     }
    //     else{
    //         $(".appearop2").css("display", "none");
    //     }
    // });

    // $("#questionimage3").change(function () {
    //     if($("#questionimage3").val() == "yes"){
    //         $(".appearop3").css("display", "block");
    //     }
    //     else{
    //         $(".appearop3").css("display", "none");
    //     }
    // });

    // $("#questionimage4").change(function () {
    //     if($("#questionimage4").val() == "yes"){
    //         $(".appearop4").css("display", "block");
    //     }
    //     else{
    //         $(".appearop4").css("display", "none");
    //     }
    // });

    // SUBJECT-CHAPTER DATABASE

    var Phys = ["Electromagnetic Induction","Newton's Law Of Motions","Optics","Semiconductors"];
    var Chem = ["Atoms and Molecules","Elements And Compounds","Quantum Chemistry"];
    var math = ["Set Theory", "Complex Numers"];

    // SUBTOPIC DATABSE

    var SetTheory = ["Complex Numbers as Ordered Pair Of Reals","Reprentation Of Complex Numbers In The Form a+ib","Argrand Diagram"];

    var emi = ['a','b','c'];
    var atm = ['d','e','f'];

    $("#subject").change(function(){
        //    var menu = document.createElement("option");
        if($("#subject").val()=="Physics"){
            $('#chapter').empty();
            $('#chapter').append("<option>Please Select The Appropiate Chapter</option>");
            for(var i = 0; i < Phys.length; i++){
                $("#chapter").append("<option>"+Phys[i]+"</option>");
            }
        }
        else if($("#subject").val()=="Chemistry"){
            $('#chapter').empty();
            $('#chapter').append("<option>Please Select The Appropiate Chapter</option>");
            for(var i = 0; i < Chem.length; i++){
                $("#chapter").append("<option>"+Chem[i]+"</option>");
            }
        }
        else if($("#subject").val()=="Mathematics"){
            $('#chapter').empty();
            $('#chapter').append("<option>Please Select The Appropiate Chapter</option>");
            for(var i = 0; i < math.length; i++){
                $("#chapter").append("<option>"+math[i]+"</option>");
            }
        }

    })

    $("#chapter").change(function(){
        $('#subtopic').empty();

        if(document.getElementById("chapter").value=="Set Theory"){
            $('#subtopic').empty();
            for(var i=0; i < SetTheory.length; i++)
            {
                $("#subtopic").append("<option>"+SetTheory[i]+"</option>");
            }
        }
        if(document.getElementById("chapter").value=="Electromagnetic Induction"){
            $('#subtopic').empty();
            for(var i=0; i < emi.length; i++)
            {
                $("#subtopic").append("<option>"+emi[i]+"</option>");
            }
        }
        if(document.getElementById("chapter").value=="Atoms and Molecules"){
            $('#subtopic').empty();
            for(var i=0; i < atm.length; i++)
            {
                $("#subtopic").append("<option>"+atm[i]+"</option>");
            }
        }

    })

});
