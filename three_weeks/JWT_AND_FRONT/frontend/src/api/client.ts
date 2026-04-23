import { clearAuthStorage, loadStoredAuth, persistAuth } from "../lib/storage";
import type { TokenPayload } from "../types/auth";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000/api";

let refreshPromise: Promise<string | null> | null = null;

async function request<T>(path: string, init: RequestInit = {}, retry = true): Promise<T> {
  const { accessToken } = loadStoredAuth();
  const headers = new Headers(init.headers);
  headers.set("Content-Type", "application/json");
  if (accessToken) {
    headers.set("Authorization", `Bearer ${accessToken}`);
  }

  const response = await fetch(`${API_BASE_URL}${path}`, { ...init, headers });

  if (response.status === 401 && retry && !path.includes("/auth/login") && !path.includes("/auth/refresh")) {
    const nextToken = await refreshAccessToken();
    if (nextToken) {
      return request<T>(path, init, false);
    }
  }

  if (!response.ok) {
    const errorBody = await response.json().catch(() => ({ detail: "Unknown error" }));
    throw new Error(errorBody.detail ?? "Request failed");
  }

  if (response.status === 204) {
    return undefined as T;
  }

  return response.json() as Promise<T>;
}

export async function refreshAccessToken(): Promise<string | null> {
  if (!refreshPromise) {
    refreshPromise = (async () => {
      const { refreshToken } = loadStoredAuth();
      if (!refreshToken) {
        return null;
      }

      try {
        const response = await fetch(`${API_BASE_URL}/auth/refresh`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ refresh_token: refreshToken })
        });

        if (!response.ok) {
          clearAuthStorage();
          return null;
        }

        const payload = (await response.json()) as TokenPayload;
        persistAuth(payload);
        return payload.access_token;
      } finally {
        refreshPromise = null;
      }
    })();
  }

  return refreshPromise;
}

export const apiClient = {
  get: <T>(path: string) => request<T>(path, { method: "GET" }),
  post: <T>(path: string, body: unknown) => request<T>(path, { method: "POST", body: JSON.stringify(body) }),
  patch: <T>(path: string, body: unknown) => request<T>(path, { method: "PATCH", body: JSON.stringify(body) }),
  delete: <T>(path: string) => request<T>(path, { method: "DELETE" })
};
