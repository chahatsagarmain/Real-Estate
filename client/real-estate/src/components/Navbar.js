import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import './../stylesheets/navbar.css';
import context from '../context/context';

function NavBar() {

  const {userName , setUsername} = useContext(context)

  return (
    <header>
    <div className="nav-bar">
      <div className="logo-title">
        <h2>EstateExplorer</h2>
      </div>
      <div className="nav-buttons">
        <Link to="/contact">Contact</Link>
        <Link to="/login">Login</Link>
        <Link to="/register">Register</Link>
      </div>
    </div>
    </header>
  );
}

export default NavBar;
