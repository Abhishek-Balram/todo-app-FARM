import './App.css';
import React, {useState, useEffect} from 'react';
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css'

import TodoList from './components/TodoList'

function App() {
  const [todoList, setTodoList] = useState([{}]);
  const [title, setTitle] = useState('');
  const [desc, setDesc] = useState('');


  // Function to handle adding a new task
  const addTodoHandler = async () => {
    try {
      const newTask = {
        'title': title,
        'description': desc,
        'completed': false
      };

      // Send a POST request with the new task to API endpoint
      const response = await axios.post('http://localhost:8000/api/todo', newTask);
      console.log(response)

      // Clear the input fields and fetch updated todo list
      setTitle('');
      setDesc('');
      fetchTodoList();
    } catch (error) {
      console.error('Error adding task:', error);
      if (error.response) {
        console.error('Response data:', error.response.data);
        console.error('Status code:', error.response.status);
      }
    }
  };


  // Fetch todo items from API endpoint
  const fetchTodoList = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/todo');
      setTodoList(response.data); // Assuming the API response is an array of todo items
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  useEffect(() => {
    fetchTodoList();
  }, [])

  

  return (
      <div
        className='App list-group-item justify-content-center align-items-center mx-auto' 
        style={{"width":"400px", "backgroundColor":"white", "marginTop":"15px" }}
      >
        <h1
          className='card text-white bg-primary mb-1'
          styleName='max-width: 20rem;'
        >
          Task Manager
        </h1>
        <h6 className='card text-white bg-primary mb-3'>
          FASTAPI - React - MongoDB
        </h6>
        <div className='card-body'>
          <h5 className='card text-white bg-dark mb-3'>Add Your Task</h5>

          <span className='card-text'>
            <input 
              className='mb-2 form-control titleIn' 
              placeholder='Title'
              onChange = {(event) => setTitle(event.target.value)}
            />
            <input 
              className='mb-2 form-control desIn' 
              placeholder='Description'
              onChange = {(event) => setDesc(event.target.value)}
            />
            <button
              className='btn btn-outline-primary mx-2 mb-2'
              stle={{'borderRadius':'100px', 'font-weight':'bold'}}
              onClick={addTodoHandler}
            >
              Add Task
            </button>
          </span>

          <h5 className='card text-white bg-dark mb-3'>Your Tasks</h5>
          <div>
            <TodoList todolist={todoList} fetchTodoList={fetchTodoList}/>
          </div>
        </div>

      </div>
  );
}

export default App;
