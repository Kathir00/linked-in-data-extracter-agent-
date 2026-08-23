import React from "react";
import LoginForm from "../components/LoginForm.jsx";

function LoginPage({ onLogin }) {
  return (
    <div>
      <LoginForm onLogin={onLogin} />
    </div>
  );
}

export default LoginPage;