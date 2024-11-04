const sidebar = document.getElementById('sidebar');
const toggleButton = document.getElementById('label-check');
const mainContent = document.querySelector('.main-content');


toggleButton.addEventListener('click', () => {
  sidebar.classList.toggle('collapsed');
  mainContent.classList.toggle('collapsed');
  toggleButton.classList.toggle('collapsed');
});

