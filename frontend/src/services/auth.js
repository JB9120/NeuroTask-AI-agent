
export const authService = {
  getToken() {
    return localStorage.getItem("access_token")
  },
  setToken(token) {
    localStorage.setItem("access_token", token)
  },
  logout() {
    localStorage.removeItem("access_token")
  }
}
