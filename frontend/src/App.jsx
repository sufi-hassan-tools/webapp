import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import ThemePage from './pages/ThemePage';
import './index.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/theme/:storeId" element={<ThemePage />} />
      </Routes>
    </Router>
  );
}

export default App;

