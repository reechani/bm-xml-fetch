/**
 * Place your JS-code here.
 */
$(document).ready(function () {
	'use strict';

	$.ajax({
		url: 'bm-cyber-sale-2015.php',
		dataType: 'json',
		success: function(data){
			var ordered_keys = Object.keys(data).sort();
			for (var key in ordered_keys) {
				var item = data[ordered_keys[key]];
				var name = ordered_keys[key];
				var lim_class = "";
				if(name.indexOf("LIMITED") > -1) {
					lim_class = "limited";
				}
				$('<div>').append(
					$('<a>').attr('href', item.url).append(
						$('<img>').attr('src', item.img)
					)
				).append(
					$('<a>').attr('href', item.url).text(name)
					.addClass('link ' + lim_class)
				)
				.addClass('item-img')
				.appendTo('main');
			}  
		}
	});

	console.log('Everything is ready.');
});