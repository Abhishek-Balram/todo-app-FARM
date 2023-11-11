import axios from 'axios'
import React from 'react'


function TodoItem(props){

    const deleteTodoHandler = async (title) => {
        const response = await axios.delete(`http://localhost:8000/api/todo/${title}`);
        console.log(response.data);
        await props.fetchTodoList();
    }

    return (
        <div className="card mb-3">
          <div className="card-body">
            <h5 className="card-title">{props.todo.title}</h5>
            <p className="card-text">{props.todo.description}</p>
            <button
              className="btn btn-danger"
              onClick={() => deleteTodoHandler(props.todo.title)}
            >
              Delete
            </button>
          </div>
        </div>
      );
}

export default TodoItem