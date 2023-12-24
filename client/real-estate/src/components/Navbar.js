import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import './../stylesheets/navbar.css';
import context from '../context/context';
import { useCookies } from 'react-cookie'
import { useEffect } from 'react';
import {useNavigate} from 'react-router';

function NavBar() {

  const { userName, setUsername } = useContext(context)
  const [cookie, setCookie, removeCookie] = useCookies()
  const navigate = useNavigate()

  useEffect(
    () => {
      checkCookie()
    }, [cookie])

  async function checkCookie() {

    try {
      const options = {
        method: "GET",
        credentials: "include"
      }
      const response = await fetch("http://localhost:8000/api/users/checkcookie", options)
      const response_data = await response.json()
      if (response.status >= 300) {
        alert(response_data)
        console.log(response_data)
      }
      else {
        console.log(response_data)
        setUsername(response_data.username)
      }
    }
    catch (error) {
      alert(error)
      console.log(error)
    }
  }

  function logout() {
    removeCookie("token")
    setUsername("")
  }

  function route(){
    navigate("")
  }

  return (
    <header>
      <div className="nav-bar">
        <div className="logo-title">
          <h2 onClick={route}>EstateExplorer</h2>
        </div>
        <div className="nav-buttons">
          <Link to="/contact">Contact</Link>
          {!userName && <Link to="/login">Login</Link>}
          {!userName && <Link to="/register">Register</Link>}
          {userName && <p>{userName}</p>}
          {userName && <p onClick={logout}>Logout</p>}
        </div>
      </div>
    </header>
  );
}

export default NavBar;
