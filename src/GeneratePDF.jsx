import React from "react"
import axios from "axios";
import { useState } from "react";


function GeneratePDF() {
  function handleUpload(){
    if (!file) {
      console.log("No file selected");
      return;
    }
    const fd = new FormData();
    fd.append('file', file);

    axios.post('http://httpbin.org/post', fd, {
      onUploadProgress: (progressEvent) => { console.log (progressEvent.progress*100) },
      headers: {

      }
    })
    .then(res => console.log(res.data))
    .catch(err => console.error(err))
  }
  const [file, setFile ] = useState(null);
  return (
    <div className="bg-slate-900 text-white min-h-screen" draggable="true">
      <div className="flex items-center justify-center bg-white p-6 mx-auto shadow-lg max-w">
        <img className="size-20 shrink-0" src="/src/logo.png" alt="InvoiceR Logo" />
        <div className="text-5xl font-bold text-slate-800 text-center">
          GeneratePDF
        </div>
      </div>
      <input onChange={ (e) => {setFile (e.target.files[0]) } } type="file"/>
      <button onClick={ handleUpload }> Upload </button>
    </div>
  );


}

export default GeneratePDF;