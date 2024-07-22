import React from 'react';
import './App.css';
import '@fontsource/manrope'; // Defaults to weight 400
import { Navbar } from './Components/navbar';
import { Section1 } from './Components/section1';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Navbar />
      </header>
      <Section1 />
    </div>
  );
}

export default App;
