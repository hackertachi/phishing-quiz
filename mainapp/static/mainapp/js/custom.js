$("select[name=pcategory]").change(function () {
  var url = $("#itemForm").attr("data-brands-url");
  var pcategory = $(this).val();

  $.ajax({
    url: url,
    data: {
      'pcategory': pcategory
    },
    success: function (data) {
      $("#id_pbrand").html(data);
    }
  });
});

$("select[name=product_category]").change(function () {
  var url = $("#itemForm").attr("data-brands-url");
  var pcategory = $(this).val();

  $.ajax({
    url: url,
    data: {
      'pcategory': pcategory
    },
    success: function (data) {
      $("#id_product_brand").html(data);
    }
  });
});

$("select[name=product_brand]").change(function () {
  var url = $("#itemForm").attr("data-models-url");
  var pbrand = $(this).val();

  $.ajax({
    url: url,
    data: {
      'pbrand': pbrand
    },
    success: function (data) {
      $("#id_product_model").html(data);
    }
  });
});

$("select[name=product_model]").change(function () {
  var url = $("#itemForm").attr("data-price-url");
  var product_model_id = $(this).val();

  $.ajax({
    url: url,
    data: {
      'id': product_model_id
    },
    success: function (data) {
      $("input[name=price]").val(data);
    }
  });
});

$("button[name=search_button_products]").click(function () {
  var url = $("#id_search_products").attr("data-search-url");
  var search = $("input[name=search_products]").val();

  $.ajax({
    url: url,
    data: {
      'search': search
    },
    success: function (data) {
      $("tbody[name=product_list]").html(data);
    }
  });
});

$("button[name=search_button_sales]").click(function () {
  var url = $("#id_search_sales").attr("data-search-url");
  var search = $("input[name=search_sales]").val();

  $.ajax({
    url: url,
    data: {
      'search': search
    },
    success: function (data) {
      $("tbody[name=sales_list]").html(data);
    }
  });
});

$("button[name=search_button_logs]").click(function () {
  var url = $("#id_search_logs").attr("data-search-url");
  var search = $("input[name=search_logs]").val();

  $.ajax({
    url: url,
    data: {
      'search': search
    },
    success: function (data) {
      $("tbody[name=activity_list]").html(data);
    }
  });
});


// sales button form
$("button[id=salesbuttonmodal]").click(function () {
  var itempk = $(this).attr("name");

  $("input[name=sales_quantity_"+ itempk +"]").focusout(function () {
    var quantity = $("input[name=sales_quantity_"+ itempk +"]").val();
    var price = $("input[name=sales_price_"+ itempk +"]").val();
    var total_price = quantity * price;
  $("input[name=sales_totalprice_"+ itempk +"").val(total_price);
  });

});