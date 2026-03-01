
import { useState } from "react"
import api from "../services/api"
import { useAuthStore } from "../store/authStore"

export default function Login() {
  const loginStore = useAuthStore(state => state.login)
  const [email,setEmail]=useState("")
  const [password,setPassword]=useState("")

  const login = async () => {

  try {

    setLoading(true)
    setError("")

    const formData = new URLSearchParams()

    formData.append("username", email)
    formData.append("password", password)

    const res = await api.post(
      "/auth/login",
      formData,
      {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        }
      }
    )

    loginStore(res.data.access_token)

    window.location = "/"

  }
  catch(err){

    setError(
      err.response?.data?.detail ||
      "Login failed"
    )
  }
  finally{
    setLoading(false)
  }
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
