import { FormEvent, useEffect, useState } from "react";

import { adminApi } from "../api/admin";
import { Button } from "../components/Button";
import { Card } from "../components/Card";
import { InputField } from "../components/InputField";
import { Label } from "../components/Label";
import { Modal } from "../components/Modal";
import { TextArea } from "../components/TextArea";
import type { BlacklistItem } from "../types/auth";

export function BlacklistPage() {
  const [items, setItems] = useState<BlacklistItem[]>([]);
  const [accessToken, setAccessToken] = useState("");
  const [reason, setReason] = useState("MANUAL_BLOCK");
  const [note, setNote] = useState("");
  const [editing, setEditing] = useState<BlacklistItem | null>(null);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  async function loadItems() {
    try {
      const data = await adminApi.getBlacklist();
      setItems(data);
    } catch (loadError) {
      setError(loadError instanceof Error ? loadError.message : "블랙리스트를 불러오지 못했습니다.");
    }
  }

  useEffect(() => {
    void loadItems();
  }, []);

  async function handleCreate(event: FormEvent) {
    event.preventDefault();
    setMessage("");
    setError("");
    try {
      await adminApi.createBlacklist({ access_token: accessToken, reason, note });
      setAccessToken("");
      setReason("MANUAL_BLOCK");
      setNote("");
      setMessage("블랙리스트가 등록되었습니다.");
      await loadItems();
    } catch (submitError) {
      setError(submitError instanceof Error ? submitError.message : "등록에 실패했습니다.");
    }
  }

  async function handleDelete(id: number) {
    try {
      await adminApi.deleteBlacklist(id);
      await loadItems();
    } catch (deleteError) {
      setError(deleteError instanceof Error ? deleteError.message : "삭제에 실패했습니다.");
    }
  }

  async function handleUpdate(event: FormEvent) {
    event.preventDefault();
    if (!editing) {
      return;
    }
    try {
      await adminApi.updateBlacklist(editing.id, { reason: editing.reason, note: editing.note ?? "" });
      setEditing(null);
      await loadItems();
    } catch (updateError) {
      setError(updateError instanceof Error ? updateError.message : "수정에 실패했습니다.");
    }
  }

  return (
    <div className="space-y-6">
      <Card>
        <h2 className="text-2xl font-bold text-slate-900">토큰 블랙리스트 등록</h2>
        <form className="mt-6 grid gap-4 lg:grid-cols-[1.2fr_0.8fr]" onSubmit={handleCreate}>
          <div className="lg:col-span-2">
            <Label>Access Token</Label>
            <TextArea rows={5} value={accessToken} onChange={(event) => setAccessToken(event.target.value)} required />
          </div>
          <div>
            <Label>사유</Label>
            <InputField value={reason} onChange={(event) => setReason(event.target.value)} required />
          </div>
          <div>
            <Label>비고</Label>
            <InputField value={note} onChange={(event) => setNote(event.target.value)} />
          </div>
          <div className="lg:col-span-2">
            <Button type="submit">블랙리스트 등록</Button>
          </div>
        </form>
        {message ? <p className="mt-4 text-sm text-brand-700">{message}</p> : null}
        {error ? <p className="mt-4 text-sm text-rose-500">{error}</p> : null}
      </Card>

      <Card>
        <h2 className="text-2xl font-bold text-slate-900">토큰 블랙리스트 목록</h2>
        <div className="mt-6 overflow-hidden rounded-2xl border border-slate-100">
          <table className="min-w-full text-left text-sm">
            <thead className="bg-brand-50 text-slate-700">
              <tr>
                <th className="px-4 py-3">ID</th>
                <th className="px-4 py-3">사유</th>
                <th className="px-4 py-3">만료일</th>
                <th className="px-4 py-3">작업</th>
              </tr>
            </thead>
            <tbody>
              {items.map((item) => (
                <tr key={item.id} className="border-t border-slate-100">
                  <td className="px-4 py-3">{item.id}</td>
                  <td className="px-4 py-3">{item.reason}</td>
                  <td className="px-4 py-3">{new Date(item.expires_at).toLocaleString()}</td>
                  <td className="px-4 py-3">
                    <div className="flex gap-2">
                      <Button variant="secondary" onClick={() => setEditing(item)}>
                        수정
                      </Button>
                      <Button variant="danger" onClick={() => void handleDelete(item.id)}>
                        삭제
                      </Button>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Card>

      <Modal open={Boolean(editing)} title="블랙리스트 수정" onClose={() => setEditing(null)}>
        <form className="space-y-4" onSubmit={handleUpdate}>
          <div>
            <Label>사유</Label>
            <InputField
              value={editing?.reason ?? ""}
              onChange={(event) =>
                setEditing((current) => (current ? { ...current, reason: event.target.value } : current))
              }
            />
          </div>
          <div>
            <Label>비고</Label>
            <TextArea
              rows={4}
              value={editing?.note ?? ""}
              onChange={(event) =>
                setEditing((current) => (current ? { ...current, note: event.target.value } : current))
              }
            />
          </div>
          <Button type="submit">저장</Button>
        </form>
      </Modal>
    </div>
  );
}
