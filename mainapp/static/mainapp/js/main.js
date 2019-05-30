$("#fade").hide().fadeIn(1000);

$("#content").hide().fadeIn(1000);

$("#page2").click(function () {
  var url = $(".training").attr("data-url");
  var body = $(this).val();

  $.ajax({
    url: url,
    data: {
      'body': body
    },
    success: function (data) {
      $(".training").html(data);
    }
  });
});