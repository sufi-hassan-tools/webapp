document.querySelector('.toggle-theme').addEventListener('click', () => {
  document.body.classList.toggle('dark-theme');
});

const ctx = document.getElementById('salesChart').getContext('2d');
new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    datasets: [{
      label: 'Sales (PKR)',
      data: [0, 0, 0, 0, 0, 0],
      backgroundColor: 'rgba(0,255,198,0.2)',
      borderColor: '#00ffc6',
      borderWidth: 2
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: { display: true }
    },
    scales: {
      y: { beginAtZero: true }
    }
  }
});
