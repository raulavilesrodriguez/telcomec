// graph the two data series to compare

function comparacion_grafico (label_x, datos1, datos2, label1, label2) {
    var ctx = document.getElementById('myChart2').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
                    data: {
                        labels: label_x,
                        datasets: [{
                            label: label1,
                            data: datos1,
                            backgroundColor: 'rgba(255, 82, 0, 0.6)',
                            borderColor: 'rgba(255, 82, 0, 1)',
                            pointColor: 'rgba(54, 162, 235, 1)',
                            borderWidth: 3
                        },
                        {
                            label: label2,
                            data: datos2,
                            backgroundColor: 'rgba(129, 178, 20, 0.6)',
                            borderColor: 'rgba(31, 99, 9, 1)',
                            pointColor: 'rgba(54, 162, 235, 1)',
                            borderWidth: 3
                        }

                        ]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                          legend: {
                            position: 'top',
                          },
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                }
                });
            };


function density (label_x, historic_density1, historic_density2, label1, label2) {
    var ctx = document.getElementById('historic_density').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'line',
                    data: {
                        labels: label_x,
                        datasets: [{
                            label: label1,
                            data: historic_density1,
                            backgroundColor: 'rgba(255, 82, 0, 0.6)',
                            borderColor: 'rgba(255, 82, 0, 1)',
                            pointColor: 'rgba(54, 162, 235, 1)',
                            borderWidth: 3
                        },
                        {
                            label: label2,
                            data: historic_density2,
                            backgroundColor: 'rgba(129, 178, 20, 0.6)',
                            borderColor: 'rgba(31, 99, 9, 1)',
                            pointColor: 'rgba(54, 162, 235, 1)',
                            borderWidth: 3
                        }

                        ]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                          legend: {
                            position: 'top',
                          },
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                }
                });
            };