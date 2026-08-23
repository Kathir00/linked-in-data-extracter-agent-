import React, { useState } from "react";

import ProfileForm from "../components/ProfileForm.jsx";
import ProfileResult from "../components/profileResult.jsx";


function ProfilePage({ onLogout }) {

  const [result, setResult] = useState(null);

  const handleResult = (data) => {
    setResult(data);
  };


  return (
    <div className="profile-page">

      {/* HEADER */}

      <header className="profile-header">

        <div className="header-brand">

          <div className="header-logo">
            Li
          </div>

          <h2 className="header-title">
            LinkedIn Profile Agent
          </h2>

        </div>


        <button
          className="logout-button"
          onClick={onLogout}
        >
          Logout
        </button>

      </header>


      {/* MAIN */}

      <main className="profile-content">

        <section className="hero-section">

          <div className="hero-badge">
            ✦ AI-Powered Profile Extraction
          </div>

          <h1>
            Extract LinkedIn Profile Data
          </h1>

          <p>
            Enter a LinkedIn profile URL and let the
            agent automatically extract the person's
            name, role, and company.
          </p>

        </section>


        {/* URL INPUT */}

        <ProfileForm
          onResult={handleResult}
        />


        {/* RESULT */}

        <ProfileResult
          result={result}
        />

      </main>

    </div>
  );
}


export default ProfilePage;