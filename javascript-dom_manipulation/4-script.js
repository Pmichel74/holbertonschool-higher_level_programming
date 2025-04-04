const listClass = document.querySelector('.my_list');

const setItem = document.querySelector('#add_item');
setItem.addEventListener('click', () => {
  const new = document.createElement('li');
  new.textContent = 'Item';
  listClass.appendChild(nuevo);
});
