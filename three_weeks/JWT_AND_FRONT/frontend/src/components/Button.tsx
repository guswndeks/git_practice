import type { ButtonHTMLAttributes, PropsWithChildren } from "react";

type ButtonVariant = "primary" | "secondary" | "danger";

const styles: Record<ButtonVariant, string> = {
  primary: "bg-brand-600 text-white hover:bg-brand-700",
  secondary: "bg-white text-brand-700 border border-brand-200 hover:bg-brand-50",
  danger: "bg-rose-500 text-white hover:bg-rose-600"
};

export function Button({
  children,
  variant = "primary",
  className = "",
  ...props
}: PropsWithChildren<ButtonHTMLAttributes<HTMLButtonElement>> & { variant?: ButtonVariant }) {
  return (
    <button
      className={`inline-flex items-center justify-center rounded-xl px-4 py-2 text-sm font-semibold transition ${styles[variant]} ${className}`}
      {...props}
    >
      {children}
    </button>
  );
}
