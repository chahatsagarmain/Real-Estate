import './App.css';
import {
  createBrowserRouter,
  RouterProvider
} from 'react-router-dom';
import NotFound from './containers/NotFound';
import Layout from './containers/Layout';
import Contact from "./containers/Contact";
import Register from './containers/Register';
import context from './context/context.js';
import {useState } from 'react';
import Login from "./containers/LogIn.js"
import Home from './containers/Home.js';

const router = createBrowserRouter([
  {
    path : "/",
    element : <Layout />,
    children : [
      {
        path : "",
        element : <Home />
      },
      {
        path : ":page",
        element : <div><h1>root route</h1></div>
      },
      {
        path : "contact",
        element : <Contact />
      },
      {
       path : "register",
       element :<Register />,
      },
      {
        path : "login",
        element : <Login />
      }
    ],
    
  },
  {
    path: '*',
    element: <NotFound />
  }
])



function App() {

  const [userName , setUsername] = useState(null)
  const [currentPage , setCurrentPage] = useState("")
  const [listings , setListings] = useState([])

  return (
    <context.Provider value = {{userName,setUsername}} >
      <RouterProvider router={router}>
      </RouterProvider>
    </context.Provider>
  );
}

export default App;
