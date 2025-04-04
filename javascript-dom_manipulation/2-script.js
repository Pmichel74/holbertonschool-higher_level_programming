const headerElement = document.querySelector('header');
const redHeaderButton = document.querySelector('#red_header');

redHeaderButton.addEventListener('click', () => {
  headerElement.classList.add('red');
});
