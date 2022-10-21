// URL that queries graph data
const url = '/api/TickerClass';
console.log(url);

const backgroundColor_red = 'rgb(236, 171, 161)'
const backgroundColor_green = 'rgb(177, 218, 178)'
const chart_type = 'line';

const x_name = 'DateTime';
const y_name_1 = 'AAPL';
const y_name_2 = 'MSFT';
const y_name_3 = 'TEAM';
const y_name_4 = 'TSLA';


fetch(url, {method: 'GET', headers: {'Content-Type': 'application/json'}}
).then(response => response.json()
).then(data => {
    const x_label_date = data.map(function(d){ return d[x_name]})
    const y_data_1 = data.map(function(d){ return d[y_name_1]})
    const y_data_2 = data.map(function(d){ return d[y_name_2]})
    const y_data_3 = data.map(function(d){ return d[y_name_3]})
    const y_data_4 = data.map(function(d){ return d[y_name_4]})


    let bgc_1 = backgroundColor_green;
    let bgc_2 = backgroundColor_green;
    let bgc_3 = backgroundColor_green;
    let bgc_4 = backgroundColor_green;

    if (y_data_1[0] > y_data_1[y_data_1.length-1]) {
        bgc_1 = backgroundColor_red
    }

    if (y_data_2[0] > y_data_2[y_data_2.length-1]) {
        bgc_2 = backgroundColor_red
    }

    if (y_data_3[0] > y_data_3[y_data_3.length-1]) {
        bgc_3 = backgroundColor_red
    }

    if (y_data_4[0] > y_data_4[y_data_4.length-1]) {
        bgc_4 = backgroundColor_red
    }

    const chart_data_1 = {
        labels: x_label_date,
        datasets: [{
            label: y_name_1,
            backgroundColor: bgc_1,
            borderColor: bgc_1,
            data: y_data_1
        }]
    };

    const chart_data_2 = {
        labels: x_label_date,
        datasets: [{
            label: y_name_2,
            backgroundColor: bgc_2,
            borderColor: bgc_2,
            data: y_data_2
        }]
    };

    const chart_data_3 = {
        labels: x_label_date,
        datasets: [{
            label: y_name_3,
            backgroundColor: bgc_3,
            borderColor: bgc_3,
            data: y_data_3
        }]
    };

    const chart_data_4 = {
        labels: x_label_date,
        datasets: [{
            label: y_name_4,
            backgroundColor: bgc_4,
            borderColor: bgc_4,
            data: y_data_4
        }]
    };


    const cfg_1 = {
        type: chart_type,
        data: chart_data_1
    };

    const cfg_2 = {
        type: chart_type,
        data: chart_data_2
    };

    const cfg_3 = {
        type: chart_type,
        data: chart_data_3
    };

    const cfg_4 = {
        type: chart_type,
        data: chart_data_4
    };

    const line_chart_1 = new Chart (
        document.getElementById('AppChart1'),
        cfg_1
    )

    const line_chart_2 = new Chart (
        document.getElementById('AppChart2'),
        cfg_2
    )

    const line_chart_3 = new Chart (
        document.getElementById('AppChart3'),
        cfg_3
    )

    const line_chart_4 = new Chart (
        document.getElementById('AppChart4'),
        cfg_4
    )



});

setInterval( function () {
    line_chart_1.update(cfg_1);
    console.log('Update')
}, 10000)

