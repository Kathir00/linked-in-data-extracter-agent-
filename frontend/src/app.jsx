import React, { useState } from "react";

import LoginPage from "./pages/login.jsx";
import ProfilePage from "./pages/profile.jsx";

function App() {
  const [authenticated, setAuthenticated] = useState(
    Boolean(localStorage.getItem("access_token"))
  );

  const handleLogin = () => {
    setAuthenticated(true);
  };

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    setAuthenticated(false);
  };

  if (!authenticated) {
    return <LoginPage onLogin={handleLogin} />;
  }

  return <ProfilePage onLogout={handleLogout} />;
}

export default App;