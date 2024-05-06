document.addEventListener('DOMContentLoaded', function () {
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
});


$(document).ready(function () {

    $("#inner1").hide(0);
    $("#inner2").hide(0);
    $("#inner3").hide(0);

    $("#btn1").mouseenter(function () {
        $("#tlt1").hide(500);
    });
    $("#btn1").mouseleave(function () {
        $("#tlt1").show(500);
    });

    $("#btn2").mouseenter(function () {
        $("#tlt2").hide(500);
    });
    $("#btn2").mouseleave(function () {
        $("#tlt2").show(500);
    });

    $("#btn3").mouseenter(function () {
        $("#tlt3").hide(1000);
    });
    $("#btn3").mouseleave(function () {
        $("#tlt3").show(1000);
    });

    $("#btn4").mouseenter(function () {
        $("#tlt4").hide(1000);
    });
    $("#btn4").mouseleave(function () {
        $("#tlt4").show(1000);
    });

    $("#img1").mouseenter(function () {
        $("#inner1").show(500);
    });
    $("#img1").mouseleave(function () {
        $("#inner1").hide(500);
    });

    $("#img2").mouseenter(function () {
        $("#inner2").show(500);
    });
    $("#img2").mouseleave(function () {
        $("#inner2").hide(500);
    });

    $("#img3").mouseenter(function () {
        $("#inner3").show(500);
    });
    $("#img3").mouseleave(function () {
        $("#inner3").hide(500);
    });

});

$(document).ready(function () {
    $(function () {
        $("#contenidoHeader").load("header.html");
    });
});

$(document).ready(function () {
    $(function () {
        $("#contenidoFooter").load("footer.html");
    });
    });