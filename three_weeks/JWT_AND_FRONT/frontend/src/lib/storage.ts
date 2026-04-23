import type { TokenPayload, UserSummary } from "../types/auth";

const ACCESS_TOKEN_KEY = "jwt_member_access_token";
const REFRESH_TOKEN_KEY = "jwt_member_refresh_token";
const USER_KEY = "jwt_member_user";

export function persistAuth(payload: TokenPayload) {
  localStorage.setItem(ACCESS_TOKEN_KEY, payload.access_token);
  localStorage.setItem(REFRESH_TOKEN_KEY, payload.refresh_token);
  localStorage.setItem(USER_KEY, JSON.stringify(payload.user));
}

export function clearAuthStorage() {
  localStorage.removeItem(ACCESS_TOKEN_KEY);
  localStorage.removeItem(REFRESH_TOKEN_KEY);
  localStorage.removeItem(USER_KEY);
}

export function loadStoredAuth() {
  const accessToken = localStorage.getItem(ACCESS_TOKEN_KEY);
  const refreshToken = localStorage.getItem(REFRESH_TOKEN_KEY);
  const rawUser = localStorage.getItem(USER_KEY);
  const user = rawUser ? (JSON.parse(rawUser) as UserSummary) : null;

  return { accessToken, refreshToken, user };
}
