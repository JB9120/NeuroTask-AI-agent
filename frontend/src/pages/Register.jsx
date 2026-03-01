
import { useState } from "react"
import api from "../services/api"

export default function Register() {
  const [email,setEmail]=useState("")
  const [password,setPassword]=useState("")

  const register = async () => {

  await api.post("/auth/register", {
    email: email,
    password: password
  })

  window.location = "/login"
}

  return (
    <div>
      <h2>Register</h2>
      <input placeholder="email" onChange={e=>setEmail(e.target.value)}/>
      <input placeholder="password" type="password" onChange={e=>setPassword(e.target.value)}/>
      <button onClick={register}>Register</button>
    </div>
  )
}
