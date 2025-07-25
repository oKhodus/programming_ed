import { useState } from 'react'

const HEADER = () => <h1>Welcome to TODOLS!</h1>
const TASKS = (props) => <div><br /><h2>Your current tasks for today:</h2>{
props.arr.map(task => <h3 key={task.id}>TASK: {task.name} - Category: {task.category}</h3>)}</div>

const INPUT = (props) => <form onSubmit={props.addtask}>
Enter new task: <br />
<input value={props.v} onChange={props.handletask}/><br />
Enter task's category: <br />
<input value={props.v2} onChange={props.handleCAT}/><br />
<button type="submit">Add task to list</button></form>

const App = () => {
  const [tasks, setTasks] = useState([
    {name: "End this project", category: "Coding", id: 1},
  ])

  const [newtask, setnewtask] = useState('')
  const handleINP = (event) => setnewtask(event.target.value)

  const [newtaskCat, setCAT] = useState('')
  const handleINPCAT = (event) => setCAT(event.target.value)

  const addNewtask = (event) => {
    event.preventDefault()

    const taskOBJ = {
        name: newtask,
        category: newtaskCat,
        id: tasks.length + 1
      }

    const taskEXISTS = tasks.some(task => task.name === newtask)

    taskEXISTS ? 
      alert(`${newtask} was already added to list`)

    : 
      (
        setTasks(tasks.concat(taskOBJ)),
        setnewtask(''),
        setCAT('')
      )

  }

  return(
  <>
    <HEADER/>
    <INPUT handletask={handleINP} handleCAT={handleINPCAT} addtask={addNewtask} v={newtask} v2={newtaskCat}/>
    <TASKS arr={tasks}/>
  </>
  )
}

export default App
