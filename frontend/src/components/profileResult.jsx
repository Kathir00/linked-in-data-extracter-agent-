import React from "react";

import { downloadExcel } from "../api.js";


function ProfileResult({ result }) {

  if (!result) {
    return null;
  }


  const profile = result.data;


  const handleDownload = async () => {

    try {

      await downloadExcel(
        "linkedin_profile.xlsx"
      );

    } catch (error) {

      alert(
        error.message ||
        "Download failed"
      );

    }
  };


  return (
    <section className="result-section">

      <div className="result-header">

        <h2 className="result-title">
          Extracted Profile
        </h2>

        <div className="success-badge">
          ✓ Extraction Complete
        </div>

      </div>


      <div className="result-grid">

        {/* FIRST NAME */}

        <div className="result-card">

          <div className="result-icon">
            A
          </div>

          <div className="result-label">
            First Name
          </div>

          <p className="result-value">
            {profile.first_name || "-"}
          </p>

        </div>


        {/* LAST NAME */}

        <div className="result-card">

          <div className="result-icon">
            A
          </div>

          <div className="result-label">
            Last Name
          </div>

          <p className="result-value">
            {profile.last_name || "-"}
          </p>

        </div>


        {/* ROLE */}

        <div className="result-card">

          <div className="result-icon">
            💼
          </div>

          <div className="result-label">
            Current Role
          </div>

          <p className="result-value">
            {profile.role || "-"}
          </p>

        </div>


        {/* COMPANY */}

        <div className="result-card">

          <div className="result-icon">
            🏢
          </div>

          <div className="result-label">
            Company
          </div>

          <p className="result-value">
            {profile.company || "-"}
          </p>

        </div>

      </div>


      {/* DOWNLOAD */}

      {result.download_url && (

        <div className="download-section">

          <button
            className="download-button"
            onClick={handleDownload}
          >
            ↓ Download Excel
          </button>

        </div>

      )}

    </section>
  );
}


export default ProfileResult;