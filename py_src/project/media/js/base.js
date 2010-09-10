/**
 * @author		Firstname Lastname
 * @copyright	http://www.divio.ch
 */
var log;
// check if console.log is available and register log(msg) or $(el).log(msg)
if(window['console'] === undefined) {
	window.console = { log: function(){}, debug: function(){} }; } else {
	log = (window.ActiveXObject) ? function (msg) { console.debug(msg); } : console.log;
};

// allow jQuery to chain .log
if('jQuery' in window && log) jQuery.fn.log = function(msg) { log("%s: %o", msg, this); return this; };

// set namespace
var BASE = {};

/**
 * CUSTOM MODULES
 * ##################################################|
 */
(function ($) {
/* private scope - do it the moo way */

	BASE = {
		init: function() {
			// initiate ie6 fixes
			if(!window.XMLHttpRequest) this.ie6();
		},
		ie6: function () {
			// pseudo fixes
			$.fn.fix_pseudos = function(options) {
				this.filter(":first-child").addClass("first-child");
				this.filter(":last-child").addClass("last-child");
			};
		}
	};
	BASE.init();

/**
 * HELPER MODULES
 * ##################################################|
 */
	/**
	 * Target modifier
	 * @version: 0.3.0
	 * @param: property (target:blank)
	 * @example: <a href="#" rel="target:blank">Lorem Ipsum</a>
	 */
	$.fn.defineTarget = function (options) {
		var options = $.extend({ property: 'rel' }, options);
		return this.each(function () {
			$(this).attr('target', '_' + $(this).attr(options.property).split(':')[1]);
		});
	};
	$('a[rel*="target:"]').defineTarget();
	$('a[class*="target:"]').defineTarget({ property: 'class' });

	/**
	 * E-Mail encrypter
	 * @version: 0.3.0
	 * @param: autoConvert (converts innerhtml to match the email address)
	 * @example: <a href="#info" rel="divio.ch" class="mailcrypte">E-Mail</a>
	 */
	$.fn.mailcrypter = function (options) {
		var options = $.extend({
			autoConvert: true
		}, options);

		return this.each(function () {
			var mailto = 'mailto:' + $(this).attr('href').replace('#', '') + '@' + $(this).attr('rel');
			$(this).attr('href', mailto);
			if(options.autoConvert) $(this).html(mailto.replace('mailto:', ''));
		});
	};
	if($('a.mailcrypte').length) $('a.mailcrypte').mailcrypter({ autoConvert: false });

	/**
	 * Pop-Up Generator
	 * @version: 0.2.0
	 * @param: width (initial width)
	 * @param: height (initial height)
	 * @example: <a href="http://www.google.ch" class="popup">Open Pop-Up</a>
	 */
	$.fn.autopopup = function (options) {
		var options = $.extend({ width: 750, height: 500}, options);
		// set vars
		var url = this.attr('href');
		var size = { 'x': options.width, 'y': options.height };

		// attach event
		return this.bind('click', function (e) {
			e.preventDefault();
			window.open(url, '_blank', 'width=' + size.x + ',height=' + size.y + ',status=yes,scrollbars=yes,resizable=yes');
		});
	};
	$('.popup').autopopup();

	/**
	 * Auto input fill-in
	 * @version: 0.6.0
	 * @param: label (if true than labeltext on parent else rel attribut on this)
	 * @param: strip (replacement text)
	 * @param: add (add additional information)
	 */
	$.fn.fieldLabel = function (options) {
		var options = $.extend({
			label: true,
			strip: '',
			add: ''
		}, options);

		// show functionality
		function show(el, e, label) {
			if(el.attr('value') != '') return false;
			el.attr('value', label);
		};

		// hide functionality
		function hide(el, e, label) {
			if(e.type == 'blur' && el.attr('value') == label) return false;
			el.attr('value', '');
		};

		return this.each(function () {
			// store label element and use replacement
			var label = (options.label == true) ? $(this).parent().find('label').text() : label = $(this).attr('rel');
			label = label.replace(options.strip, '');
			label += options.add;

			// initialize
			if($(this).attr('value') == '') $(this).attr('value', label);

			// attach event
			$(this).bind('click', function (e) {
				if($(this).attr('value') == label) hide($(this), e, label)
			})
			$(this).bind('blur', function (e) {
				($(this).attr('value') == label) ? hide($(this), e, label) : show($(this), e, label);
			})
		})
		
	};
	//$('.fieldLabel').fieldLabel({ strip: ': ', add: '...' });

	/**
	 * Language Dropdown Generator
	 * @version: 0.2.1
	 * @param: fx (transition effect: fade, slide or toggle)
	 * @param: element (replacing anchor element - span required)
	 * @param: elementClass (replacing anchor element class for grabbing)
	 * @param: originClass (additional Class to mainnav)
	 * @param: activeClass (mainnav active element class)
	 * @param: conainerClass (wrapping element class)
	 */
	$.fn.droplet = function (options) {
		var options = $.extend({
			fx: 'fade',
			element: '<div class="droplet-item"><span></span></div>',
			elementClass: 'droplet-item',
			originClass: 'droplet-nav',
			activeClass: 'active',
			containerClass: 'droplet-container'
		}, options);

		// prepare container
		var container = $(this);
			container.hide()
				.addClass(options.originClass)
				.wrap('<div class="' + options.containerClass + '"></div>')
				.before($(options.element))
				.parent().find('.' + options.elementClass + ' span').html($(this).find('li.' + options.activeClass).text());

		// add events
		container.parent().bind('mouseenter mouseleave', function (e) {
			e.preventDefault();
			if(options.fx == 'toggle') container.toggle();
			if(options.fx == 'slide') {
				if(e.type == 'mouseenter') container.stop().slideDown();
				if(e.type == 'mouseleave') container.stop().css('height', 'auto').slideUp();
			}
			if(options.fx == 'fade') {
				if(e.type == 'mouseenter') container.stop().fadeIn();
				if(e.type == 'mouseleave') container.stop().css('opacity', 1).fadeOut();
			}
		}).end()
		// remove selected item
		.find('li').each(function () {
			if($(this).hasClass('active')) $(this).empty();
		});
	};
	//$('#langnav').droplet();

	/**
	 * Horizontal dropdown menu
	 * @version: 0.2.0
	 * @param: fx (transition effect: fade, slide or toggle)
	 * @example: $(element).dropdown();
	 */
	$.fn.dropDownMenu = function (options) {
		var $this = this;
		var timer;
		var options = $.extend({
			fx: 'toggle',
			delay: 0
		}, options);

		// autohide subtree
		$this.find('ul').hide();

		// mouseenter event
		$this.find('li').bind('mouseenter', function (e) {
			if($(this).find('ul').length) show($(this), $(this).find('ul'));
		});

		// mouseleave event
		$this.find('li').bind('mouseleave', function (e) {
			var el = $(this);
			if(el.find('ul').length) {
				timer = setTimeout(function () {
					hide(el, el.find('ul'));
					el.removeClass('hover');
				}, options.delay);
				el.find('ul').bind('mouseenter', function () {
					clearTimeout(timer);
				});
			}
		});

		// show menu
		function show(parent, child) {
			parent.addClass('hover');
			if(options.fx == 'toggle') child.css('display', 'block').stop().show();
			if(options.fx == 'slide') child.css('height', 'auto').stop().slideDown();
			if(options.fx == 'fade') child.css('opacity', 1).stop().fadeIn();
		}

		//hide menu
		function hide(parent, child) {
			if(options.fx == 'toggle') child.stop().hide();
			if(options.fx == 'slide') child.stop().slideUp();
			if(options.fx == 'fade') child.stop().fadeOut();
		}

		// keep chaining
		return this;
	};
	$('#mainnav').dropDownMenu();

	/**
	 * Reverse a jquery collection (last first)
	 * @version: 0.1.0
	 * @example: $("div").reverse().each(function(){ //reverse order each() });
	 */
	$.fn.reverse = [].reverse;

	/**
	 * Equal Height Columns
	 * @version: 0.1.0
	 * @example: $(element).equalHeight();
	 */
	$.fn.equalHeight = function(px) {
		$(this).each(function(){
			var currentTallest = 0;
			$(this).children().each(function(i){
				if ($(this).height() > currentTallest) { currentTallest = $(this).height(); }
			});
			if (!px || !Number.prototype.pxToEm) currentTallest = currentTallest.pxToEm(); //use ems unless px is specified
			// for ie6, set height since min-height isn't supported
			if ($.browser.msie && $.browser.version == 6.0) { $(this).children().css({'height': currentTallest}); }
			$(this).children().css({'min-height': currentTallest});
		});
		return this;
	};
})(jQuery);
//jQuery(document).ready(function ($) { });