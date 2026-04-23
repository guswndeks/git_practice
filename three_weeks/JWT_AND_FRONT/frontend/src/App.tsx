import { Navigate, Route, Routes } from "react-router-dom";

import { SidebarLayout } from "./layouts/SidebarLayout";
import { DashboardPage } from "./pages/DashboardPage";
import { BlacklistPage } from "./pages/BlacklistPage";
import { LoginPage } from "./pages/LoginPage";
import { MembersPage } from "./pages/MembersPage";
import { MyProfilePage } from "./pages/MyProfilePage";
import { ProtectedRoute } from "./routes/ProtectedRoute";
import { useAuth } from "./hooks/useAuth";

function AdminRoute({ children }: { children: JSX.Element }) {
  const { user } = useAuth();
  if (user?.role !== "ADMIN") {
    return <Navigate to="/" replace />;
  }
  return children;
}

export function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route
        path="/"
        element={
          <ProtectedRoute>
            <SidebarLayout />
          </ProtectedRoute>
        }
      >
        <Route index element={<DashboardPage />} />
        <Route path="me" element={<MyProfilePage />} />
        <Route
          path="members"
          element={
            <AdminRoute>
              <MembersPage />
            </AdminRoute>
          }
        />
        <Route
          path="blacklist"
          element={
            <AdminRoute>
              <BlacklistPage />
            </AdminRoute>
          }
        />
      </Route>
    </Routes>
  );
}
