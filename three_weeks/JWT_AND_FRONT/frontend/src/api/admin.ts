import { apiClient } from "./client";
import type { BlacklistItem, UserDetail, UserSummary } from "../types/auth";

export const adminApi = {
  getUsers: () => apiClient.get<UserSummary[]>("/users"),
  getUserDetail: (userId: number) => apiClient.get<UserDetail>(`/users/${userId}`),
  getBlacklist: () => apiClient.get<BlacklistItem[]>("/blacklist/access-tokens"),
  createBlacklist: (payload: { access_token: string; reason: string; note?: string }) =>
    apiClient.post<BlacklistItem>("/blacklist/access-tokens", payload),
  updateBlacklist: (id: number, payload: { reason?: string; note?: string }) =>
    apiClient.patch<BlacklistItem>(`/blacklist/access-tokens/${id}`, payload),
  deleteBlacklist: (id: number) => apiClient.delete<void>(`/blacklist/access-tokens/${id}`)
};
