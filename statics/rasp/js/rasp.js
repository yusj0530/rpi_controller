/*
alert jQuery plugin
*/
(function($){
	
	$.fn.alert = function( duration ) {
		var $alertbar = $( this ); 
			
		if( $alertbar.hasClass( "arduino-alert-bar" ) == false ) {
			return;
		}

		var interval = setInterval(function() {
			if( $alertbar.hasClass( "label-default" ) == true ) {
				$alertbar.removeClass( "label-default" );
				$alertbar.addClass( "label-danger" );
			} else {
				$alertbar.removeClass( "label-danger" );
				$alertbar.addClass( "label-default" );				
			}
		}, duration );
		
		$alertbar.attr( "data-interval", interval );
	}

	$.fn.stopAlert = function() {
		var $alertbar = $( this );
		
		if( $alertbar.hasClass( "arduino-alert-bar" ) == false ) {
			return;
		}
		
		var interval = $alertbar.attr( "data-interval" );

		clearInterval( interval );
		$alertbar.removeClass( "label-danger" );
		$alertbar.addClass( "label-default" );		
	}
	
})(jQuery);	

// ( function(a){ console.log("aa") })(호출); 익명함수 사용법, 형식. 두 번 사용 안할것들은 이렇게 만들어도 된다.
// 위에 $가 (function) 역할
