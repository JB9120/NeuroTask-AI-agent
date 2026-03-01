
import { Link } from "react-router-dom"
import { useAuthStore } from "../store/authStore"

export default function Navbar() {
  const logout = useAuthStore(state => state.logout)
  const token = useAuthStore(state => state.token)

  if (!token) return null

  return (
    <nav style={{padding:10, background:"#222", color:"#fff"}}>
      <Link to="/" style={{marginRight:10, color:"#fff"}}>Dashboard</Link>
      <Link to="/todos" style={{marginRight:10, color:"#fff"}}>Todos</Link>
      <Link to="/admin" style={{marginRight:10, color:"#fff"}}>Admin</Link>
      <button onClick={logout}>Logout</button>
    </nav>
  )
}
