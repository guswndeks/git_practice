import { apiClient } from "./client";
import type { TokenPayload, UserDetail } from "../types/auth";

export const authApi = {
  signup: (payload: { email: string; name: string; password: string }) =>
    apiClient.post<TokenPayload>("/auth/signup", payload),
  login: (payload: { email: string; password: string }) => apiClient.post<TokenPayload>("/auth/login", payload),
  logout: (refreshToken: string) => apiClient.post<{ message: string }>("/auth/logout", { refresh_token: refreshToken }),
  getMe: () => apiClient.get<UserDetail>("/users/me"),
  updateMe: (payload: { name?: string; password?: string }) => apiClient.patch<UserDetail>("/users/me", payload)
};
