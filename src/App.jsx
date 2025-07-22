import React from "react"
import Home from "./Home"
import ViewPDFs from "./ViewPDFs"
import GeneratePDF from "./GeneratePDF"
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Layout from './Layout'
function App() {
  return (
    <Router>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<Home />} />
          <Route path="/GeneratePDF" element={<GeneratePDF />} />
          <Route path="/ViewPDFs" element={<ViewPDFs />} />
        </Route>
      </Routes>
    </Router>
  )
}

export default App;
