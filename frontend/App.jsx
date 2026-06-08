import { useState } from "react";

function App() {

  const [file,setFile] = useState(null);

  return (
    <div>

      <h1>Terranexis EcoVision</h1>

      <input
        type="file"
        onChange={(e)=>setFile(e.target.files[0])}
      />

      <button>
        Analyze Waste
      </button>

    </div>
  );
}

export default App;