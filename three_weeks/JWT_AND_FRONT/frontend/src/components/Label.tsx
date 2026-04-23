import type { PropsWithChildren } from "react";

export function Label({ children }: PropsWithChildren) {
  return <label className="mb-2 block text-sm font-semibold text-slate-700">{children}</label>;
}
