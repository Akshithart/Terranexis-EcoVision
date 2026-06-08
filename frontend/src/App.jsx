import { useState } from "react";
import axios from "axios";

function App() {

  const [file, setFile] = useState(null);

  const analyzeWaste = async () => {
    const response = await axios.post(
      "http://127.0.0.1:8000/analyze"
    );

    console.log(response.data);
  };

  return (
    <div>

      <h1>Terranexis EcoVision</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={analyzeWaste}>
        Analyze Waste
      </button>

    </div>
  );
}

export default App;