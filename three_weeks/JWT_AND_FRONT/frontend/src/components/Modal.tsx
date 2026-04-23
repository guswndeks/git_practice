import type { PropsWithChildren } from "react";

import { Button } from "./Button";

export function Modal({
  children,
  open,
  title,
  onClose
}: PropsWithChildren<{ open: boolean; title: string; onClose: () => void }>) {
  if (!open) {
    return null;
  }

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/35 p-4">
      <div className="w-full max-w-lg rounded-3xl bg-white p-6 shadow-soft">
        <div className="mb-4 flex items-center justify-between">
          <h3 className="text-lg font-bold text-slate-800">{title}</h3>
          <Button variant="secondary" onClick={onClose}>
            닫기
          </Button>
        </div>
        {children}
      </div>
    </div>
  );
}
