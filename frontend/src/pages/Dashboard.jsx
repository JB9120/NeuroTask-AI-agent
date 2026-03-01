import React from "react"
export default function Dashboard({onNavigate}){
return(<div style={{padding:20}}>
<h1>NeuroTask Dashboard</h1>
<button onClick={()=>{localStorage.removeItem("token");onNavigate("login")}}>Logout</button>
</div>)}