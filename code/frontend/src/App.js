import React, { useState } from "react";
import axios from "axios";

function App() {
  const [emailBody, setEmailBody] = useState("");
  const [response, setResponse] = useState(null);

  const handleSubmit = async () => {
    try {
      const res = await axios.post("http://localhost:8000/process-email", { email_body: emailBody });
      setResponse(res.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="App">
      <h1>Loan Request Classification</h1>
      <textarea
        value={emailBody}
        onChange={(e) => setEmailBody(e.target.value)}
        rows="10"
        cols="50"
        placeholder="Paste email body here..."
      />
      <br />
      <button onClick={handleSubmit}>Classify Email</button>

      {response && (
        <div>
          <h3>Classification:</h3>
          <p>{response.classification}</p>
          <h3>Extracted Data:</h3>
          <p>CUSIP: {response.key_data.CUSIP}</p>
          <p>Amount: {response.key_data.Amount}</p>
          <p>Date: {response.key_data.Date}</p>
          <p>Route: {response.route}</p>
        </div>
      )}
    </div>
  );
}

export default App;
