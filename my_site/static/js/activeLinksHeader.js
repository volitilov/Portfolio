var j = jQuery.noConflict();

j(function() {
	var url_pathname = document.location.pathname;

	j('#navbar a').each(function() {
		if (j(this).attr('href') === url_pathname) {
			j(this).css({
				color: '#02a8f3'
			})
			j(this).removeAttr('href');
		}
	});

});