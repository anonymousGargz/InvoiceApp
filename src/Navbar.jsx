import { Link } from "react-router-dom"
import React from "react";
function Navbar() {

    return (
        <>
            <div className="flex bg-slate-900 justify-center space-x-40 p-6">
                <Link to="/">
                    <button className="w-80 bg-yellow-600 shadow-lg font-semibold hover:bg-sky-700 text-xl text-slate-900 py-2 px-4 rounded-3xl">
                        Home
                    </button>
                </Link>
                <Link to="/GeneratePDF">
                    <button className="w-80 bg-white shadow-lg font-semibold hover:bg-sky-700 text-xl text-slate-900 py-2 px-4 rounded-3xl">
                        Generate Invoice PDFs
                    </button>
                </Link>
                <Link to="/ViewPDFs">
                    <button className="w-80 bg-yellow-600 shadow-lg font-semibold hover:bg-sky-700 text-xl text-slate-900 py-2 px-4 rounded-3xl">
                        View Generated PDFs
                    </button>
                </Link>
            </div>


        </>
    )

}

export default Navbar;