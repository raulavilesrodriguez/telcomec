// graph the different data series

function grafico_sma(x, sma) {
        var ctx = document.getElementById('myChart').getContext('2d');
        console.log(x);
        console.log(sma);
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: x,
                datasets: [{
                    label: '# Subscribers mobile (SMA)',
                    data: sma,
                    backgroundColor: 'rgba(87, 0, 173, 0.5)',
                    borderColor: 'rgba(43, 2, 121, 1)',
                    pointColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 2
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
};

function grafico_fixed_phone(x, fixed_phone) {
        var ctx = document.getElementById('myFixed').getContext('2d');
        console.log(x);
        console.log(fixed_phone);
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: x,
                datasets: [{
                    label: '# Subscribers Fixed telephony',
                    data: fixed_phone,
                    backgroundColor: 'rgba(216, 71, 3, 0.5)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    pointColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 2
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
};

function grafico_fixed_internet(x, fixed_internet) {
        var ctx = document.getElementById('myFixedInternet').getContext('2d');
        console.log(x);
        console.log(fixed_internet);
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: x,
                datasets: [{
                    label: '# Subscribers Fixed Internet',
                    data: fixed_internet,
                    backgroundColor: 'rgba(38, 156, 2, 0.5)',
                    borderColor: 'rgba(17, 70, 1, 1)',
                    pointColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 2
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
};

function grafico_mobile_internet(x, mobile_internet) {
        var ctx = document.getElementById('myMobileInternet').getContext('2d');
        console.log(x);
        console.log(mobile_internet);
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: x,
                datasets: [{
                    label: '# Subscribers Mobile Internet',
                    data: mobile_internet,
                    backgroundColor: 'rgba(255, 15, 15, 0.6)',
                    borderColor: 'rgba(128, 0, 0, 1)',
                    pointColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 2
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
};

function grafico_portador_enlaces(x, portador_enlaces) {
        var ctx = document.getElementById('myTrunkingTerminales').getContext('2d');
        console.log(x);
        console.log(portador_enlaces);
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: x,
                datasets: [{
                    label: '# Portador Service',
                    data: portador_enlaces,
                    backgroundColor: 'rgba(0, 89, 214, 0.5)',
                    borderColor: 'rgba(0, 45, 107, 1)',
                    pointColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 2
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
};

function grafico_audio_video(x, audio_video) {
        var ctx = document.getElementById('myAVS').getContext('2d');
        console.log(x);
        console.log(audio_video);
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: x,
                datasets: [{
                    label: '# Subscribers Audio Video Service',
                    data: audio_video,
                    backgroundColor: 'rgba(255, 201, 26, 0.6)',
                    borderColor: 'rgba(204, 156, 0, 1)',
                    pointColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 2
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
};
