import React,{useState} from "react"
import API from "../api/client"
export default function Register({onNavigate}){
const [email,setEmail]=useState("")
const [password,setPassword]=useState("")
const register=async()=>{
 try{
  await API.post("/auth/register",{email,password})
  alert("Registered")
  onNavigate("login")
 }catch{alert("Register failed")}
}
return(<div style={{padding:20}}>
<h2>Register</h2>
<input placeholder="Email" onChange={e=>setEmail(e.target.value)}/><br/><br/>
<input placeholder="Password" type="password" onChange={e=>setPassword(e.target.value)}/><br/><br/>
<button onClick={register}>Register</button>
</div>)}