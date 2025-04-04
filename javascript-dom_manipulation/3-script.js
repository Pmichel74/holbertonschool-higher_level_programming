const headerElement = document.querySelector('header');
const toggleButton = document.querySelector('#toggle_header');

toggleButton.addEventListener('click', () => {
  if (headerElement.classList.length === 0) {
    headerElement.classList.add('green');
  } else if (headerElement.classList.contains('green')) {
    headerElement.classList.replace('green', 'red');
  } else if (headerElement.classList.contains('red')) {
    headerElement.classList.replace('red', 'green');
  }
});
