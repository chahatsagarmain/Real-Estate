import { Outlet } from "react-router";
import NavBar from "./../components/Navbar";
import Footer from "./../components/Footer";
import './../App.css';

function Layout(){
    return (
        <div className="app">
            <NavBar />
            <Outlet />
            <Footer />
         </div>
    )
}

export default Layout;