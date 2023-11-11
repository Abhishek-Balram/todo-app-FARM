import TodoItem from './TodoItem'

function TodoList(props) {
    const fetchTodoList = props.fetchTodoList;
    return(
        <div>
            <ul>
                {props.todolist.map(todo => <TodoItem todo={todo} fetchTodoList={fetchTodoList}/>)}
            </ul>
        </div>
    )
}

export default TodoList