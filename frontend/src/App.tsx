import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';
import { io } from "socket.io-client";

function App() {
  const [answer, setAnswer] = useState("");
  useEffect(() => {
    fetch("http://localhost:5000/test")
    .then(res => res.text())
    .then((result) => {
      setAnswer(result)
    })
  }, [])
  //TODO: receive ping from backend through WebSockets
  let serverResponse: string = "";
  const socket = io("ws://localhost:5000");
  socket.send("test message");
  socket.on("message", (data) => {
    serverResponse = data;
  });

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>result: {answer}</p>
        <p>server response: {serverResponse}</p>
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
