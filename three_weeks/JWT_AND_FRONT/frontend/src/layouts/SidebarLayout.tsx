import { NavLink, Outlet } from "react-router-dom";

import { Button } from "../components/Button";
import { useAuth } from "../hooks/useAuth";

const commonMenus = [
  { to: "/", label: "대시보드" },
  { to: "/me", label: "내 정보" }
];

const adminMenus = [
  { to: "/members", label: "회원 목록" },
  { to: "/blacklist", label: "토큰 블랙리스트" }
];

export function SidebarLayout() {
  const { user, logout } = useAuth();

  return (
    <div className="min-h-screen bg-transparent p-4 md:p-6">
      <div className="mx-auto grid min-h-[calc(100vh-2rem)] max-w-7xl gap-4 md:grid-cols-[280px_1fr]">
        <aside className="rounded-[32px] bg-brand-800 p-6 text-white shadow-soft">
          <div className="mb-8">
            <p className="text-sm uppercase tracking-[0.2em] text-brand-100">Member Console</p>
            <h1 className="mt-3 text-3xl font-bold">JWT Portal</h1>
          </div>

          <div className="mb-8 rounded-3xl bg-white/10 p-4">
            <p className="text-sm text-brand-100">로그인 사용자</p>
            <p className="mt-2 text-lg font-semibold">{user?.name}</p>
            <p className="text-sm text-brand-100">{user?.role}</p>
          </div>

          <nav className="space-y-2">
            {commonMenus.map((menu) => (
              <NavLink
                key={menu.to}
                to={menu.to}
                end={menu.to === "/"}
                className={({ isActive }) =>
                  `block rounded-2xl px-4 py-3 text-sm font-medium transition ${
                    isActive ? "bg-white text-brand-800" : "text-brand-100 hover:bg-white/10"
                  }`
                }
              >
                {menu.label}
              </NavLink>
            ))}
            {user?.role === "ADMIN" &&
              adminMenus.map((menu) => (
                <NavLink
                  key={menu.to}
                  to={menu.to}
                  className={({ isActive }) =>
                    `block rounded-2xl px-4 py-3 text-sm font-medium transition ${
                      isActive ? "bg-white text-brand-800" : "text-brand-100 hover:bg-white/10"
                    }`
                  }
                >
                  {menu.label}
                </NavLink>
              ))}
          </nav>

          <Button className="mt-8 w-full" variant="secondary" onClick={() => void logout()}>
            로그아웃
          </Button>
        </aside>

        <main className="rounded-[32px] bg-white/70 p-4 backdrop-blur md:p-8">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
