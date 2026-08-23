const API_URL =
  import.meta.env.VITE_API_URL ||
  "http://127.0.0.1:8000";


// ==========================================
// LOGIN
// ==========================================

export async function login(username, password) {
  const response = await fetch(
    `${API_URL}/auth/login`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify({
        username,
        password,
      }),
    }
  );

  const data = await response.json();

  if (!response.ok) {
    throw new Error(
      data.detail || "Login failed"
    );
  }

  return data;
}


// ==========================================
// EXTRACT PROFILE
// ==========================================

export async function extractProfile(
  linkedinUrl
) {
  const token =
    localStorage.getItem("access_token");

  if (!token) {
    throw new Error(
      "You are not authenticated."
    );
  }

  const response = await fetch(
    `${API_URL}/profile/extract`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({
        linkedin_url: linkedinUrl,
      }),
    }
  );

  const data = await response.json();

  if (!response.ok) {
    throw new Error(
      data.detail ||
      "Profile extraction failed"
    );
  }

  return data;
}


// ==========================================
// DOWNLOAD EXCEL
// ==========================================

export async function downloadExcel(
  filename
) {
  const token =
    localStorage.getItem("access_token");

  if (!token) {
    throw new Error(
      "You are not authenticated."
    );
  }

  const response = await fetch(
    `${API_URL}/profile/download/${filename}`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  if (!response.ok) {
    const data = await response.json();

    throw new Error(
      data.detail ||
      "Excel download failed"
    );
  }

  const blob = await response.blob();

  const url =
    window.URL.createObjectURL(blob);

  const link =
    document.createElement("a");

  link.href = url;
  link.download = filename;

  document.body.appendChild(link);

  link.click();

  link.remove();

  window.URL.revokeObjectURL(url);
}