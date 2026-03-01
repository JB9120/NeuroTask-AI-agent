
import { create } from "zustand"
import { authService } from "../services/auth"

export const useAuthStore = create(set => ({
  token: authService.getToken(),
  login: (token) => {
    authService.setToken(token)
    set({ token })
  },
  logout: () => {
    authService.logout()
    set({ token: null })
  }
}))
