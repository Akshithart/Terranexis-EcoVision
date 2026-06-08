import { useState } from "react";
import axios from "axios";

function App() {

  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const analyzeWaste = async () => {
    const response = await axios.post(
      "http://127.0.0.1:8000/analyze"
    );

    setResult(response.data);
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

      {result && (
        <div>

          <h2>{result.waste_type}</h2>

          <p>
            Carbon Saved:
            {result.carbon_saved}
          </p>

          <p>
            Revenue:
            ₹{result.revenue}
          </p>

          <p>
            Score:
            {result.sustainability_score}
          </p>
          <p>
            Recommendation:
            {result.suggestion}
          </p>

        </div>
      )}

    </div>
  );
}

export default App;