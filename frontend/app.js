const API_BASE = "http://localhost:5000";

async function loadApi() {
  const el = document.getElementById("api-message");
  el.textContent = "Cargando...";
  try {
    const res = await fetch(`${API_BASE}/`);
    const data = await res.json();
    el.textContent = data.message;
  } catch {
    el.textContent = "Error llamando a la API";
  }
}

async function loadDb() {
  const el = document.getElementById("db-time");
  el.textContent = "Cargando...";
  try {
    const res = await fetch(`${API_BASE}/db`);
    const data = await res.json();
    el.textContent = data.db_time || data.error;
  } catch {
    el.textContent = "Error llamando a la DB";
  }
}

loadApi();
loadDb();
