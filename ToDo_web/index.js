const todoForm = document.getElementById('todobox');
const todoInput = document.getElementById('todo-txt');
const todoList = document.getElementById('todo-list');
const todoTemplate = document.getElementById('todo-items')

const formSubmit = (event) => {
    event.preventDefault();
    const inputValue = todoInput.value.trim();
    if(inputValue==='') return;
    const todoItem = todoTemplate.content.cloneNode(true).querySelector('.todo-item');

    todoItem.querySelector('.item-title').textContent = inputValue;
    todoList.appendChild(todoItem);
    todoInput.value='';
};
todoForm.addEventListener('submit', formSubmit);