import React, { useState } from "react"
import Login from "./pages/Login.jsx"
import Register from "./pages/Register.jsx"
import Dashboard from "./pages/Dashboard.jsx"

export default function App(){
  const [page, setPage] = useState("login")
  if(page==="login") return <Login onNavigate={setPage}/>
  if(page==="register") return <Register onNavigate={setPage}/>
  if(page==="dashboard") return <Dashboard onNavigate={setPage}/>
}