import { FormEvent, useEffect, useState } from "react";

import { Button } from "../components/Button";
import { Card } from "../components/Card";
import { InputField } from "../components/InputField";
import { Label } from "../components/Label";
import { authApi } from "../api/auth";
import { useAuth } from "../hooks/useAuth";
import type { UserDetail } from "../types/auth";

export function MyProfilePage() {
  const { updateMe } = useAuth();
  const [profile, setProfile] = useState<UserDetail | null>(null);
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    authApi
      .getMe()
      .then((data) => {
        setProfile(data);
        setName(data.name);
      })
      .catch((loadError) => setError(loadError instanceof Error ? loadError.message : "정보를 불러오지 못했습니다."));
  }, []);

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();
    setMessage("");
    setError("");
    try {
      const updated = await updateMe({ name, password: password || undefined });
      setProfile(updated);
      setPassword("");
      setMessage("내 정보가 수정되었습니다.");
    } catch (submitError) {
      setError(submitError instanceof Error ? submitError.message : "수정에 실패했습니다.");
    }
  }

  return (
    <div className="grid gap-6 lg:grid-cols-[1.1fr_0.9fr]">
      <Card>
        <h2 className="text-2xl font-bold text-slate-900">나의 정보</h2>
        {profile ? (
          <dl className="mt-6 grid gap-4 text-sm text-slate-600">
            <div>
              <dt className="font-semibold text-slate-900">이메일</dt>
              <dd>{profile.email}</dd>
            </div>
            <div>
              <dt className="font-semibold text-slate-900">이름</dt>
              <dd>{profile.name}</dd>
            </div>
            <div>
              <dt className="font-semibold text-slate-900">역할</dt>
              <dd>{profile.role}</dd>
            </div>
            <div>
              <dt className="font-semibold text-slate-900">가입일</dt>
              <dd>{new Date(profile.created_at).toLocaleString()}</dd>
            </div>
          </dl>
        ) : (
          <p className="mt-4 text-sm text-slate-500">정보를 불러오는 중입니다.</p>
        )}
      </Card>

      <Card>
        <h2 className="text-2xl font-bold text-slate-900">내 정보 수정</h2>
        <form className="mt-6 space-y-4" onSubmit={handleSubmit}>
          <div>
            <Label>이름</Label>
            <InputField value={name} onChange={(event) => setName(event.target.value)} />
          </div>
          <div>
            <Label>새 비밀번호</Label>
            <InputField
              type="password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              placeholder="변경할 때만 입력"
            />
          </div>
          {message ? <p className="text-sm text-brand-700">{message}</p> : null}
          {error ? <p className="text-sm text-rose-500">{error}</p> : null}
          <Button type="submit">변경사항 저장</Button>
        </form>
      </Card>
    </div>
  );
}
