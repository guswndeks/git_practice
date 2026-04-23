import type { PropsWithChildren } from "react";

export function Card({ children, className = "" }: PropsWithChildren<{ className?: string }>) {
  return <section className={`rounded-3xl bg-white p-6 shadow-soft ${className}`}>{children}</section>;
}
