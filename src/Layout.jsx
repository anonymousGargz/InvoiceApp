import Navbar from "./Navbar"
import { Outlet } from "react-router-dom"
import React from "react";
function Layout() {
    return (
        <>
            <Navbar />
            <main>
                <Outlet/>
            </main>
        </>
    )
}

export default Layout;