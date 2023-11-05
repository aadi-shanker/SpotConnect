import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import {
  createBrowserRouter,
  Router,
  RouterProvider
} from "react-router-dom"
import LoginPage from "./Components/LoginPage.jsx";
import SocialMediaInput from "./Components/SocialMediaInput.jsx"
import HandlOutput from "./Components/HandlOutput.jsx";


const router = createBrowserRouter([
  {
    path: "/",
    element: <LoginPage/>
  },
  {
    path: "/social",
    element: <SocialMediaInput/>
  },
  {
    path: "/handle",
    element: <HandlOutput/>
  }
])
ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
