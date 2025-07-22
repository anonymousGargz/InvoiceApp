import React from "react";
import { Link } from "react-router-dom"

function Home() {
  return (
    <div className="bg-slate-900 text-white min-h-screen" draggable="true">
      <div className="flex items-center justify-center bg-white p-6 mx-auto shadow-lg max-w">
        <img className="size-20 shrink-0" src="/src/logo.png" alt="InvoiceR Logo" />
        <div className="text-5xl font-bold text-slate-800 text-center">
          InvoiceR
        </div>
      </div>
    </div>

  )


}

export default Home;