const links = document.querySelectorAll('.nav-link');
const currentPath = window.location.pathname.split('/').pop();

links.forEach(link => {
  if (link.getAttribute('href') === currentPath) {
    link.classList.add('active');
  }
});