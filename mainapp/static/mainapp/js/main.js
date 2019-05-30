$(".training").hide().fadeIn(1000);

$('a[name=test-left').hide();

$('#training').on('slid.bs.carousel', function () {
	if ($('.carousel-item:first').hasClass('active')) {
        $('a[name=test-left').hide();
	} else if ($('.carousel-item:last').hasClass('active')) {
		$('a[name=test-right').hide();
	} else if ($('.carousel-item').hasClass('active')) {
		$('a[name=test-left').show();
		$('a[name=test-right').show();
	}
});
