export type Role = "ADMIN" | "USER";

export interface UserSummary {
  id: number;
  email: string;
  name: string;
  role: Role;
}

export interface UserDetail extends UserSummary {
  created_at: string;
  updated_at: string;
}

export interface TokenPayload {
  access_token: string;
  refresh_token: string;
  token_type: string;
  access_token_expires_in: number;
  refresh_token_expires_in: number;
  user: UserSummary;
}

export interface BlacklistItem {
  id: number;
  token_hash: string;
  jti: string | null;
  expires_at: string;
  reason: string;
  note: string | null;
  created_at: string;
}
