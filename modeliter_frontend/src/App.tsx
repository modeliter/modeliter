import React, { useState } from "react";
import "./App.css";

function App() {
  const [input, setInput] = useState("");
  const onChangeInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInput(e.target.value);
  };
  const [output, setOutput] = useState("");
  const onClickSubmit = async () => {
    let response = await fetch("/api/v1/reverse", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ input }),
    });
    let { output } = await response.json();
    setOutput(output);
  };

  return (
    <div className="App">
      <header className="App-header">
        <input type="text" value={input} onChange={onChangeInput} />
        <button onClick={onClickSubmit}>Submit</button>
        <p>{output}</p>
      </header>
    </div >
  );
}

export default App;
