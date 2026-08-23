import React, { useState } from "react";

import { extractProfile } from "../api.js";


function ProfileForm({ onResult }) {

  const [linkedinUrl, setLinkedinUrl] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  const [error, setError] =
    useState("");


  const handleSubmit = async (event) => {

    event.preventDefault();

    setError("");
    setLoading(true);

    try {

      const result =
        await extractProfile(linkedinUrl);

      onResult(result);

    } catch (error) {

      setError(
        error.message ||
        "Profile extraction failed"
      );

    } finally {

      setLoading(false);

    }
  };


  return (
    <div>

      <form
        className="extract-card"
        onSubmit={handleSubmit}
      >

        <label className="extract-label">
          LinkedIn Profile URL
        </label>


        <div className="url-row">

          <input
            className="url-input"
            type="url"
            value={linkedinUrl}
            onChange={(event) =>
              setLinkedinUrl(
                event.target.value
              )
            }
            placeholder="https://www.linkedin.com/in/username/"
            required
          />


          <button
            className="extract-button"
            type="submit"
            disabled={loading}
          >

            {loading
              ? "Extracting..."
              : "Extract Profile"}

          </button>

        </div>


        {loading && (

          <div className="loading-card">

            <div className="spinner"></div>

            <div>

              <p className="loading-title">
                Extracting profile...
              </p>

              <p className="loading-text">
                Scraping LinkedIn data and
                processing the profile.
              </p>

            </div>

          </div>

        )}


        {error && (

          <div className="profile-error">
            {error}
          </div>

        )}

      </form>

    </div>
  );
}


export default ProfileForm;