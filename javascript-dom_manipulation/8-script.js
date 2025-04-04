document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then((response) => response.json())
    .then((data) => {
      const helloContent = document.getElementById('hello');
      helloContent.textContent = data.hello;
    });
});
