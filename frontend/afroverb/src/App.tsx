import React from 'react';
import './App.css';
import '@fontsource/manrope'; // Defaults to weight 400
import { Navbar } from './Components/navbar';
import { Section1 } from './Components/section1';
import { Section2 } from './Components/section2';
import { Section3 } from './Components/section3';
import { Section4 } from './Components/section4';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Navbar />
      </header>
      <Section1 />
      <Section2 />
      <Section3 />
      <Section4 />
    </div>
  );
}

export default App;
