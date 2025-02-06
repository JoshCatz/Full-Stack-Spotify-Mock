import React from "react";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from "./pages/Home";
import Search from "./components/Search";
import Navbar from "./components/Navbar";
import ProtectedRoute from "./components/ProtectedRoute";
import ArtistLogin from "./pages/ArtistLogin";
import Login from "./pages/Login";
import SignUp from "./pages/Signup"
import ArtistSignUp from "./pages/ArtistSignUp";
import ArtistDashboard from "./pages/ArtistDashboard";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />}/>
        <Route path="/signup" element={<SignUp />}/>
        <Route path="/artist/login" element={<ArtistLogin />}/>
        <Route path="/artist/signup" element={<ArtistSignUp />}/>
      <Route
        path="/"
        element={
          <ProtectedRoute>
            <div className="grid grid-cols-1">
              <Search />
              <div className="grid grid-cols-[75px_auto] gap-2 h-screen">
                <div>
                  <Navbar />
              </div>
              <div className="">
                <Home />
              </div>
            </div>
          </div>
          </ProtectedRoute>
        }
        />
      </Routes>
    </Router>
  );
}

export default App;