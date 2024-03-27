import React, { ReactNode } from "react";
import ReactDOM from "react-dom/client";
import App from "./App.tsx";
import "./styles/index.css";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import VideoAnalysis from "./pages/VideoAnalysis.tsx";
import { useLink, VideoContext } from "./hooks/useLink.ts";

function Provider({ children }: { children: ReactNode }) {
  const link = useLink();
  return <VideoContext.Provider value={link} children={children} />;
}

export default Provider;

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "/video",
    element: (
      <Provider>
        <VideoAnalysis />
      </Provider>
    ),
  },
]);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
