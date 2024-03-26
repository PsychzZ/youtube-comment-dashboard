import { useState } from "react";
import "./styles/App.css";
import { Button, Typography } from "@mui/material";
import NavBar from "./components/NavBar";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <NavBar />
      <h1>Vite + React</h1>
      <div className="card">
        <Button
          variant="outlined"
          onClick={() => setCount((count) => count + 1)}
        >
          {count}
        </Button>
        <Typography>
          Edit <code>src/App.tsx</code> and save to test HMR
        </Typography>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  );
}

export default App;
