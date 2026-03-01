import React,{useState} from "react"
import API from "../api/client"
export default function Login({onNavigate}){
const [email,setEmail]=useState("")
const [password,setPassword]=useState("")
const login=async()=>{
 try{
  const res=await API.post("/auth/login",{email,password})
  localStorage.setItem("token",res.data.access_token)
  onNavigate("dashboard")
 }catch{alert("Login failed")}
}
return(<div style={{padding:20}}>
<h2>Login</h2>
<input placeholder="Email" onChange={e=>setEmail(e.target.value)}/><br/><br/>
<input placeholder="Password" type="password" onChange={e=>setPassword(e.target.value)}/><br/><br/>
<button onClick={login}>Login</button>
<p style={{cursor:"pointer",color:"blue"}} onClick={()=>onNavigate("register")}>Register</p>
</div>)}