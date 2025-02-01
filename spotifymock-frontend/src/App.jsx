import React from "react";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from "./pages/Home";
import Search from "./components/Search";
import Navbar from "./components/Navbar";

const App = () => {
  return (
    <Router>
      <div className="grid grid-cols-1">
        <Search />
        <div className="grid grid-cols-[75px_auto] gap-2 h-screen">
          <div>
            <Navbar />
          </div>
          <div className="">
            <Routes>
              <Route path="/" element={<Home />} />
            </Routes>
          </div>
        </div>
      </div>
    </Router>
  );
}

export default App