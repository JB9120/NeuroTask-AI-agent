
import { useEffect, useState } from "react"
import api from "../services/api"

export default function Todos() {
  const [todos,setTodos]=useState([])

  useEffect(()=>{
    api.get("/todos").then(res=>setTodos(res.data))
  },[])

  return (
    <div>
      <h2>Todos</h2>
      {todos.map(t=>(<div key={t.id}>{t.text}</div>))}
    </div>
  )
}
