
import { useState } from "react"
import api from "../services/api"
import { useAuthStore } from "../store/authStore"

export default function Login() {
  const loginStore = useAuthStore(state => state.login)
  const [email,setEmail]=useState("")
  const [password,setPassword]=useState("")

  const login = async () => {
    const res = await api.post("/auth/login",{email,password})
    loginStore(res.data.access_token)
    window.location="/"
  }

  return (
    <div>
      <h2>Login</h2>
      <input placeholder="email" onChange={e=>setEmail(e.target.value)}/>
      <input placeholder="password" type="password" onChange={e=>setPassword(e.target.value)}/>
      <button onClick={login}>Login</button>
    </div>
  )
}
