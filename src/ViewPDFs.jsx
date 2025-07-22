import React from "react"

function ViewPDFs() {
  return (
    <div className="bg-slate-900 text-white min-h-screen" draggable="true">
      <div className="flex items-center justify-center bg-white p-6 mx-auto shadow-lg max-w">
        <img className="size-20 shrink-0" src="/src/logo.png" alt="InvoiceR Logo" />
        <div className="text-5xl font-bold text-slate-800 text-center">
          ViewPDFs
        </div>
      </div>
    </div>
  )


}

export default ViewPDFs;