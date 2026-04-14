import { useState, useEffect } from "react";

function App() {
  const [externalTeams, setExternalTeams] = useState([]);
  const [myTeams, setMyTeams] = useState([]);
  const [newTeamName, setNewTeamName] = useState("");

  // Cargar mis equipos de la DB al iniciar
  useEffect(() => {
    fetchMyTeams();
  }, []);

  const fetchExternal = async () => {
    const res = await fetch("http://localhost:5000/api/external-teams");
    const data = await res.json();
    setExternalTeams(data.teams || []);
  };

  const fetchMyTeams = async () => {
    const res = await fetch("http://localhost:5000/api/teams");
    const data = await res.json();
    setMyTeams(data);
  };

  const addTeam = async (e) => {
    e.preventDefault();
    if (!newTeamName) return;
    await fetch("http://localhost:5000/api/teams", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: newTeamName }),
    });
    setNewTeamName("");
    fetchMyTeams();
  };

  const deleteTeam = async (id) => {
    await fetch(`http://localhost:5000/api/teams/${id}`, { method: "DELETE" });
    fetchMyTeams();
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-200 p-6 font-sans">
      <h1 className="text-3xl font-bold text-center text-indigo-400 mb-10 uppercase tracking-tighter">
        Gestión de Equipos de Fútbol - Sistemas UCE
      </h1>

      <div className="grid md:grid-cols-2 gap-10 max-w-6xl mx-auto">
        {/* SECCIÓN API EXTERNA */}
        <div className="bg-slate-900 p-6 rounded-2xl border border-slate-800 shadow-xl">
          <h2 className="text-xl font-semibold mb-4 text-indigo-300">
            Equipos Premier League (API)
          </h2>
          <button
            onClick={fetchExternal}
            className="w-full bg-indigo-600 hover:bg-indigo-500 py-2 rounded-lg font-bold transition-all mb-4"
          >
            Cargar Equipos Externos
          </button>
          <div className="h-64 overflow-y-auto space-y-2 pr-2">
            {externalTeams.map((t) => (
              <div
                key={t.id}
                className="bg-slate-800 p-2 rounded border border-slate-700 text-sm"
              >
                {t.name}
              </div>
            ))}
          </div>
        </div>

        {/* SECCIÓN CRUD INTERNO */}
        <div className="bg-slate-900 p-6 rounded-2xl border border-slate-800 shadow-xl">
          <h2 className="text-xl font-semibold mb-4 text-emerald-300">
            Mis Equipos Favoritos (CRUD DB)
          </h2>

          <form onSubmit={addTeam} className="flex gap-2 mb-6">
            <input
              type="text"
              value={newTeamName}
              onChange={(e) => setNewTeamName(e.target.value)}
              placeholder="Nombre del equipo..."
              className="flex-1 bg-slate-800 border border-slate-700 p-2 rounded-lg focus:outline-none focus:border-emerald-500 text-white"
            />
            <button className="bg-emerald-600 hover:bg-emerald-500 px-4 rounded-lg font-bold text-white">
              Añadir
            </button>
          </form>

          <div className="space-y-2">
            {myTeams.map((t) => (
              <div
                key={t.id}
                className="flex justify-between items-center bg-slate-800 p-3 rounded-lg border border-slate-700"
              >
                <span>{t.name}</span>
                <button
                  onClick={() => deleteTeam(t.id)}
                  className="text-red-400 hover:text-red-300 text-xs font-bold uppercase"
                >
                  Eliminar
                </button>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
