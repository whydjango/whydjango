/**
 * plugins.twitter.js
 * @author: Angelo Dini - divio.ch
 * @version: 0.1.0
 */
(function($) {
	// tweet meme plugin
	$.fn.twitter = function(options) {
		return this.each(function () {
			// save options
			var options = $.extend({
				url: $(this).text(),
				source: 'username',
				style: 'normal',
				service: 'retwt.me',
				width: 50,
				height: 61
			}, options);
			// create start url
			var url = 'http://api.tweetmeme.com/button.js?';
			// serialize options
			$.each(options, function (key, value) {
				url += key + '=' + value + '&';
			});
			// save iframe
			var iframe = '<iframe src="' + url + '" width="' + options.width + '" height="' + options.height + '" scrolling="no" frameborder="0"></iframe>';
			// add iframe
			$(this).html(iframe);
		});
	};
})(jQuery);
/**
 * jquery.tweet.js
 * @author: http://github.com/seaofclouds/tweet
 * @version: 0.1 -  (04.08.2010)
 * Licensed under the MIT http://www.opensource.org/licenses/mit-license.php
 */
(function(a){a.fn.tweet=function(f){var e={username:["seaofclouds"],list:null,avatar_size:null,count:3,intro_text:null,outro_text:null,join_text:null,auto_join_text_default:"i said,",auto_join_text_ed:"i",auto_join_text_ing:"i am",auto_join_text_reply:"i replied to",auto_join_text_url:"i was looking at",loading_text:null,query:null};if(f){a.extend(e,f)}a.fn.extend({linkUrl:function(){var g=[];var h=/((ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?)/gi;this.each(function(){g.push(this.replace(h,'<a href="$1">$1</a>'))});return a(g)},linkUser:function(){var g=[];var h=/[\@]+([A-Za-z0-9-_]+)/gi;this.each(function(){g.push(this.replace(h,'<a href="http://twitter.com/$1">@$1</a>'))});return a(g)},linkHash:function(){var g=[];var h=/(?:^| )[\#]+([A-Za-z0-9-_]+)/gi;this.each(function(){g.push(this.replace(h,' <a href="http://search.twitter.com/search?q=&tag=$1&lang=all&from='+e.username.join("%2BOR%2B")+'">#$1</a>'))});return a(g)},capAwesome:function(){var g=[];this.each(function(){g.push(this.replace(/\b(awesome)\b/gi,'<span class="awesome">$1</span>'))});return a(g)},capEpic:function(){var g=[];this.each(function(){g.push(this.replace(/\b(epic)\b/gi,'<span class="epic">$1</span>'))});return a(g)},makeHeart:function(){var g=[];this.each(function(){g.push(this.replace(/(&lt;)+[3]/gi,"<tt class='heart'>&#x2665;</tt>"))});return a(g)}});function b(g){return Date.parse(g.replace(/^([a-z]{3})( [a-z]{3} \d\d?)(.*)( \d{4})$/i,"$1,$2$4$3"))}function d(i){var g=b(i);var j=(arguments.length>1)?arguments[1]:new Date();var k=parseInt((j.getTime()-g)/1000);var h=function(l,m){return""+m+" "+l+(m==1?"":"s")};if(k<60){return"less than a minute ago"}else{if(k<(60*60)){return"about "+h("minute",parseInt(k/60))+" ago"}else{if(k<(24*60*60)){return"about "+h("hour",parseInt(k/3600))+" ago"}else{return"about "+h("day",parseInt(k/86400))+" ago"}}}}function c(){var g=("https:"==document.location.protocol?"https:":"http:");if(e.list){return g+"//api.twitter.com/1/"+e.username[0]+"/lists/"+e.list+"/statuses.json?per_page="+e.count+"&callback=?"}else{if(e.query==null&&e.username.length==1){return g+"//api.twitter.com/1/statuses/user_timeline.json?screen_name="+e.username[0]+"&count="+e.count+"&callback=?"}else{var h=(e.query||"from:"+e.username.join(" OR from:"));return g+"//search.twitter.com/search.json?&q="+encodeURIComponent(h)+"&rpp="+e.count+"&callback=?"}}}return this.each(function(h,l){var k=a('<ul class="tweet_list">').appendTo(l);var j='<p class="tweet_intro">'+e.intro_text+"</p>";var g='<p class="tweet_outro">'+e.outro_text+"</p>";var m=a('<p class="loading">'+e.loading_text+"</p>");if(typeof(e.username)=="string"){e.username=[e.username]}if(e.loading_text){a(l).append(m)}a.getJSON(c(),function(i){if(e.loading_text){m.remove()}if(e.intro_text){k.before(j)}var n=(i.results||i);a.each(n,function(r,y){if(e.join_text=="auto"){if(y.text.match(/^(@([A-Za-z0-9-_]+)) .*/i)){var p=e.auto_join_text_reply}else{if(y.text.match(/(^\w+:\/\/[A-Za-z0-9-_]+\.[A-Za-z0-9-_:%&\?\/.=]+) .*/i)){var p=e.auto_join_text_url}else{if(y.text.match(/^((\w+ed)|just) .*/im)){var p=e.auto_join_text_ed}else{if(y.text.match(/^(\w*ing) .*/i)){var p=e.auto_join_text_ing}else{var p=e.auto_join_text_default}}}}}else{var p=e.join_text}var s=y.from_user||y.user.screen_name;var u=y.profile_image_url||y.user.profile_image_url;var w='<span class="tweet_join"> '+p+" </span>";var o=((e.join_text)?w:" ");var t='<a class="tweet_avatar" href="http://twitter.com/'+s+'"><img src="'+u+'" height="'+e.avatar_size+'" width="'+e.avatar_size+'" alt="'+s+'\'s avatar" title="'+s+'\'s avatar" border="0"/></a>';var v=(e.avatar_size?t:"");var q='<span class="tweet_time"><a href="http://twitter.com/'+s+"/statuses/"+y.id+'" title="view tweet on twitter">'+d(y.created_at)+"</a></span>";var x='<span class="tweet_text">'+a([y.text]).linkUrl().linkUser().linkHash().makeHeart().capAwesome().capEpic()[0]+"</span>";k.append("<li>"+v+q+o+x+"</li>");k.children("li:first").addClass("tweet_first");k.children("li:odd").addClass("tweet_even");k.children("li:even").addClass("tweet_odd")});if(e.outro_text){k.after(g)}a(l).trigger("loaded").trigger((n.length==0?"empty":"full"))})})}})(jQuery);