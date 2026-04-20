// js/main.js
document.addEventListener('DOMContentLoaded', () => {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.sidebar-nav .nav-item').forEach(link => {
    const href = link.getAttribute('href');
    if (href && (currentPath === href || (currentPath === 'index.html' && href === 'index.html'))) {
      link.classList.add('active');
    } else if (currentPath === '' && href === 'index.html') {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
});