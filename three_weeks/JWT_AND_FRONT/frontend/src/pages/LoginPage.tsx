import { FormEvent, useState } from "react";
import { Navigate } from "react-router-dom";

import { Button } from "../components/Button";
import { Card } from "../components/Card";
import { InputField } from "../components/InputField";
import { Label } from "../components/Label";
import { useAuth } from "../hooks/useAuth";

export function LoginPage() {
  const { user, login, signup } = useAuth();
  const [mode, setMode] = useState<"login" | "signup">("login");
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  if (user) {
    return <Navigate to="/" replace />;
  }

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();
    setError("");
    try {
      if (mode === "login") {
        await login({ email, password });
      } else {
        await signup({ email, name, password });
      }
    } catch (submitError) {
      setError(submitError instanceof Error ? submitError.message : "인증에 실패했습니다.");
    }
  }

  return (
    <div className="flex min-h-screen items-center justify-center p-4">
      <Card className="w-full max-w-md">
        <p className="text-sm font-semibold uppercase tracking-[0.18em] text-brand-600">JWT Member Frontend</p>
        <h1 className="mt-3 text-3xl font-bold text-slate-900">{mode === "login" ? "로그인" : "회원가입"}</h1>
        <p className="mt-2 text-sm text-slate-500">Light Green 톤으로 구성된 관리자/사용자 통합 콘솔입니다.</p>

        <form className="mt-8 space-y-4" onSubmit={handleSubmit}>
          <div>
            <Label>이메일</Label>
            <InputField value={email} onChange={(event) => setEmail(event.target.value)} type="email" required />
          </div>

          {mode === "signup" && (
            <div>
              <Label>이름</Label>
              <InputField value={name} onChange={(event) => setName(event.target.value)} required />
            </div>
          )}

          <div>
            <Label>비밀번호</Label>
            <InputField
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              type="password"
              required
            />
          </div>

          {error ? <p className="text-sm text-rose-500">{error}</p> : null}

          <Button className="w-full" type="submit">
            {mode === "login" ? "로그인" : "회원가입"}
          </Button>
        </form>

        <Button
          className="mt-4 w-full"
          variant="secondary"
          onClick={() => setMode((current) => (current === "login" ? "signup" : "login"))}
        >
          {mode === "login" ? "회원가입으로 이동" : "로그인으로 이동"}
        </Button>
      </Card>
    </div>
  );
}
