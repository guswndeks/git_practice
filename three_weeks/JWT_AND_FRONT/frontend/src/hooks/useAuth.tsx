import { createContext, useContext, useEffect, useState } from "react";

import { authApi } from "../api/auth";
import { clearAuthStorage, loadStoredAuth, persistAuth } from "../lib/storage";
import type { TokenPayload, UserDetail, UserSummary } from "../types/auth";

interface AuthContextValue {
  user: UserSummary | null;
  loading: boolean;
  login: (payload: { email: string; password: string }) => Promise<void>;
  signup: (payload: { email: string; name: string; password: string }) => Promise<void>;
  logout: () => Promise<void>;
  refreshMe: () => Promise<void>;
  updateMe: (payload: { name?: string; password?: string }) => Promise<UserDetail>;
}

const AuthContext = createContext<AuthContextValue | null>(null);

function applyAuth(payload: TokenPayload, setUser: (user: UserSummary | null) => void) {
  persistAuth(payload);
  setUser(payload.user);
}

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<UserSummary | null>(loadStoredAuth().user);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    authApi
      .getMe()
      .then((profile) => setUser(profile))
      .catch(() => {
        clearAuthStorage();
        setUser(null);
      })
      .finally(() => setLoading(false));
  }, []);

  const value: AuthContextValue = {
    user,
    loading,
    login: async (payload) => {
      const result = await authApi.login(payload);
      applyAuth(result, setUser);
    },
    signup: async (payload) => {
      const result = await authApi.signup(payload);
      applyAuth(result, setUser);
    },
    logout: async () => {
      const { refreshToken } = loadStoredAuth();
      if (refreshToken) {
        await authApi.logout(refreshToken).catch(() => undefined);
      }
      clearAuthStorage();
      setUser(null);
    },
    refreshMe: async () => {
      const profile = await authApi.getMe();
      setUser(profile);
    },
    updateMe: async (payload) => {
      const profile = await authApi.updateMe(payload);
      const current = loadStoredAuth();
      if (current.user && current.accessToken && current.refreshToken) {
        localStorage.setItem("jwt_member_user", JSON.stringify(profile));
      }
      setUser(profile);
      return profile;
    }
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within AuthProvider");
  }
  return context;
}
