import { Card } from "../components/Card";
import { useAuth } from "../hooks/useAuth";

export function DashboardPage() {
  const { user } = useAuth();

  return (
    <div className="space-y-6">
      <div>
        <p className="text-sm font-semibold uppercase tracking-[0.18em] text-brand-600">Overview</p>
        <h2 className="mt-3 text-3xl font-bold text-slate-900">환영합니다, {user?.name}님</h2>
        <p className="mt-2 text-slate-500">현재 역할은 {user?.role}이며, 사이드 메뉴는 역할에 따라 자동으로 바뀝니다.</p>
      </div>

      <div className="grid gap-4 md:grid-cols-3">
        <Card>
          <p className="text-sm text-slate-500">인증 정책</p>
          <p className="mt-2 text-2xl font-bold text-slate-900">Access 5분</p>
        </Card>
        <Card>
          <p className="text-sm text-slate-500">리프레시 토큰</p>
          <p className="mt-2 text-2xl font-bold text-slate-900">5일 유지</p>
        </Card>
        <Card>
          <p className="text-sm text-slate-500">권한</p>
          <p className="mt-2 text-2xl font-bold text-slate-900">{user?.role}</p>
        </Card>
      </div>
    </div>
  );
}
