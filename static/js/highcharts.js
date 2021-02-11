var chart;

        function requestData()
        {
            // Ajax call to get the Data from Flask
            var requests = $.get('/live-data');


            var tm = requests.done(function (result)
            {
                var series = chart.series[0],
                    shift = series.data.length > 20;

                // add the point
                chart.series[0].addPoint(result, true, shift);

                // call it again after one second
                setTimeout(requestData, 2000);
            });
        }

        $(document).ready(function() {
            chart = new Highcharts.Chart({
                chart: {
                    renderTo: 'data-container',
                    defaultSeriesType: 'spline',
                    events: {
                        load: requestData
                    }
                },
                title: {
                    text: 'Live temperature data'
                },
                xAxis: {
                    type: 'datetime',
                    tickPixelInterval: 150,
                    maxZoom: 20 * 1000
                },
                yAxis: {
                    minPadding: 0.2,
                    maxPadding: 0.2,
                    title: {
                        text: 'Value',
                        margin: 80
                    }
                },
                series: [{
                    name: 'Random data',
                    data: []
                }]
            });

        });