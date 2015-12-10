$(document).ready(function () {
	'use strict';

	var old_items;

	var files = {
/*		'old': 'cyber-2015-old.php', 'new': 'cyber-2015.php'*/
/*		'old': 'cyber-us-2015-old.php', 'new': 'cyber-us-2015.php'*/
		'old': 'museum-dec-2015-old.php', 'new': 'museum-dec-2015.php'
/*		'old': 'museum-dec-us-2015-old.php', 'new': 'museum-dec-us-2015.php'*/
	};

	var off = 0;

	var title = 'Black Milk Cyber Sale 2015 items';
	var tag = 'Cyber_Sale_2015';

	var setup = function() {
		$('<title>').text(title).appendTo($('head'));
		$('<h1>').text(title).prependTo($('body'));
		$('#tag').text(tag);
	};

	var saveData = function(data, into) {
		switch(into) {
			case 'old':
				old_items = data;
				break;
		}
	};

	var get_keys_clean = function(data) {
		var keys, clean;
		keys = Object.keys(data).sort();
		// clean keys
		clean = keys.map(function(item) {
			return item.split(' - ')[0].trim();
		});
		return clean;
	};

	var show = function(items, id) {
		var target, list, li;

		target = $('#' + id);

		list = $('<ul>');
		for (var key in items) {
			li = $('<li>').text(items[key]);
			li.appendTo(list);
		}
		list.appendTo(target);
	};

	var compare = function(new_data, old_data) {
		var old_keys, new_keys,
				added = {}, removed = {};

		// get keys
		old_keys = get_keys_clean(old_data);
		new_keys = get_keys_clean(new_data);

		// Get diffs
		added = new_keys.filter(function(item) {
			return old_keys.indexOf(item) < 0;
		});
		removed = old_keys.filter(function(item) {
			return new_keys.indexOf(item) < 0;
		});

		// show diffs
		show(added, 'added');
		show(removed, 'removed');
	};

	var get_old = function(file) {
		$.ajax({
			url: file,
			dataType: 'json',
			success: function(data){
				saveData(data, 'old');
			}
		});
	};

	var get_new = function(file) {
		$.ajax({
			url: file,
			dataType: 'json',
			success: function(data){
				var ordered_keys = Object.keys(data).sort();
				for (var key in ordered_keys) {
					var item = data[ordered_keys[key]];
					var name = ordered_keys[key];
					var lim_class = "";
					var price = item.price * (1 - off);
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
					).append(
						$('<span>').text('$' + price.toFixed(2))
					)
					.addClass('item-img')
					.appendTo('main');
				}
				compare(data, old_items);
			}
		});
	};

	var run = function(files) {
		setup();
		get_old(files.old);
		get_new(files.new);
	};

	run(files);

});