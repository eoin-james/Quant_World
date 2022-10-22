// URL that queries graph data
const url = '/api/TickerClass';
console.log(url);

// Chart setup
const Color_Red = 'rgb(236, 171, 161)'
const Color_Green = 'rgb(177, 218, 178)'
const chart_type = 'line';

// Try fetch these values from Flask API
const names = ['DateTime', 'AAPL', 'MSFT', 'TEAM', 'TSLA']

// If Open value is greater than Close value line is green else red
function colour_decider(y_data) {
    if (y_data[0] > y_data[y_data.length - 1]) {
        return Color_Red;
    }
    return Color_Green;
}

// fetch data from the server
fetch(url, {method: 'GET', headers: {'Content-Type': 'application/json'}}
).then(response => response.json()
).then(data => {

    // Parse the response data
    const x_label_date = data.map(function(d){ return d[names[0]]});
    const y_data_1 = data.map(function(d){ return d[names[1]]});
    const y_data_2 = data.map(function(d){ return d[names[2]]});
    const y_data_3 = data.map(function(d){ return d[names[3]]});
    const y_data_4 = data.map(function(d){ return d[names[4]]});

    // Get colour of each ticker value
    let bgc_1 = colour_decider(y_data_1);
    let bgc_2 = colour_decider(y_data_2);
    let bgc_3 = colour_decider(y_data_3);
    let bgc_4 = colour_decider(y_data_4);


    const chart_data_1 = {
        labels: x_label_date,
        datasets: [{
            label: names[1],
            backgroundColor: bgc_1,
            borderColor: bgc_1,
            data: y_data_1
        }]
    };

    const chart_data_2 = {
        labels: x_label_date,
        datasets: [{
            label: names[2],
            backgroundColor: bgc_2,
            borderColor: bgc_2,
            data: y_data_2
        }]
    };

    const chart_data_3 = {
        labels: x_label_date,
        datasets: [{
            label: names[3],
            backgroundColor: bgc_3,
            borderColor: bgc_3,
            data: y_data_3
        }]
    };

    const chart_data_4 = {
        labels: x_label_date,
        datasets: [{
            label: names[4],
            backgroundColor: bgc_4,
            borderColor: bgc_4,
            data: y_data_4
        }]
    };


    const cfg_1 = {
        type: chart_type,
        data: chart_data_1,
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

