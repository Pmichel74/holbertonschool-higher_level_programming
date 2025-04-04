const headerElement = document.querySelector('header');

const updateButton = document.querySelector('#update_header');
updateButton.addEventListener('click', () => {
  headerElement.textContent = 'New Header!!!';
});
