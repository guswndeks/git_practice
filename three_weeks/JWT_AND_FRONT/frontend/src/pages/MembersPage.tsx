import { useEffect, useState } from "react";

import { adminApi } from "../api/admin";
import { Card } from "../components/Card";
import type { UserDetail, UserSummary } from "../types/auth";

export function MembersPage() {
  const [members, setMembers] = useState<UserSummary[]>([]);
  const [selected, setSelected] = useState<UserDetail | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    adminApi
      .getUsers()
      .then((data) => {
        setMembers(data);
        if (data[0]) {
          return adminApi.getUserDetail(data[0].id).then(setSelected);
        }
      })
      .catch((loadError) => setError(loadError instanceof Error ? loadError.message : "회원 정보를 불러오지 못했습니다."));
  }, []);

  async function handleSelect(userId: number) {
    try {
      const detail = await adminApi.getUserDetail(userId);
      setSelected(detail);
    } catch (detailError) {
      setError(detailError instanceof Error ? detailError.message : "상세 조회에 실패했습니다.");
    }
  }

  return (
    <div className="grid gap-6 lg:grid-cols-[1.1fr_0.9fr]">
      <Card>
        <h2 className="text-2xl font-bold text-slate-900">회원 목록</h2>
        {error ? <p className="mt-4 text-sm text-rose-500">{error}</p> : null}
        <div className="mt-6 overflow-hidden rounded-2xl border border-slate-100">
          <table className="min-w-full text-left text-sm">
            <thead className="bg-brand-50 text-slate-700">
              <tr>
                <th className="px-4 py-3">ID</th>
                <th className="px-4 py-3">이름</th>
                <th className="px-4 py-3">이메일</th>
                <th className="px-4 py-3">역할</th>
              </tr>
            </thead>
            <tbody>
              {members.map((member) => (
                <tr
                  key={member.id}
                  className="cursor-pointer border-t border-slate-100 hover:bg-brand-50/60"
                  onClick={() => void handleSelect(member.id)}
                >
                  <td className="px-4 py-3">{member.id}</td>
                  <td className="px-4 py-3">{member.name}</td>
                  <td className="px-4 py-3">{member.email}</td>
                  <td className="px-4 py-3">{member.role}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Card>

      <Card>
        <h2 className="text-2xl font-bold text-slate-900">회원 상세</h2>
        {selected ? (
          <dl className="mt-6 grid gap-4 text-sm text-slate-600">
            <div>
              <dt className="font-semibold text-slate-900">이름</dt>
              <dd>{selected.name}</dd>
            </div>
            <div>
              <dt className="font-semibold text-slate-900">이메일</dt>
              <dd>{selected.email}</dd>
            </div>
            <div>
              <dt className="font-semibold text-slate-900">역할</dt>
              <dd>{selected.role}</dd>
            </div>
            <div>
              <dt className="font-semibold text-slate-900">생성일</dt>
              <dd>{new Date(selected.created_at).toLocaleString()}</dd>
            </div>
            <div>
              <dt className="font-semibold text-slate-900">수정일</dt>
              <dd>{new Date(selected.updated_at).toLocaleString()}</dd>
            </div>
          </dl>
        ) : (
          <p className="mt-4 text-sm text-slate-500">왼쪽 목록에서 회원을 선택하세요.</p>
        )}
      </Card>
    </div>
  );
}
