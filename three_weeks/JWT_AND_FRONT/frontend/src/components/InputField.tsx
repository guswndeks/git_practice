import type { InputHTMLAttributes } from "react";

export function InputField({ className = "", ...props }: InputHTMLAttributes<HTMLInputElement>) {
  return (
    <input
      className={`w-full rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm outline-none transition focus:border-brand-400 focus:ring-2 focus:ring-brand-100 ${className}`}
      {...props}
    />
  );
}
