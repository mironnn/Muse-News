    function load_chart() {
        $.get('/load_chart', {
            'region': $('#region_select').val()
        }).done(function (data) {

        var chart = AmCharts.makeChart("chartdiv", {
    "type": "serial",
    "theme": "none",
    "dataProvider": data,
    "valueAxes": [{
        "gridColor":"#FFFFFF",
		"gridAlpha": 0.2,
		"dashLength": 0
    }],
    "gridAboveGraphs": true,
    "startDuration": 1,
    "graphs": [{
        "balloonText": "[[category]]: <b>[[value]]</b>",
        "fillAlphas": 0.8,
        "lineAlpha": 0.2,
        "type": "column",
        "valueField": "area"
    }],
    "chartCursor": {
        "categoryBalloonEnabled": false,
        "cursorAlpha": 0,
        "zoomable": false
    },
    "categoryField": "name",
    "categoryAxis": {
        "gridPosition": "start",
        "gridAlpha": 0,
         "tickPosition":"start",
         "tickLength":20
    },
	"exportConfig":{
	  "menuTop": 0,
	  "menuItems": [{
      "icon": '/lib/3/images/export.png',
      "format": 'png'
      }]
	}
});
        });
    }