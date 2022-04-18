import React, { useEffect } from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
  useEffect(() => {
    // DJANGO RESOURCES NEED TRAILING SLASH FOR SOME GODDAMN REASON
    // PROD_BACKEND - LEAVE THIS ENABLED BY DEFAULT SINCE THIS GETS SERVED until we flag on env vars
    // fetch("https://okada-api.com/")
    //   .then((response) => response.json())
    //   .then((data) => console.log(data));
    // LOCAL_BACKEND
    fetch("http://127.0.0.1:8000/groups/")
      .then((response) => response.json())
      .then((data) => console.log(data));
  });

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
