import "./../stylesheets/home.css";
import {useNavigate} from 'react-router-dom';

function Home(){
    const navigate = useNavigate()
    function route(){
        navigate("/1")
    }
    return (
        <div className="home">
            <div className="home-body">
                <p id="home-title">Find Your real estate here !</p>
                <p>Find the suitable estate for the right price !</p>
                <p>Accompanied by top of the line realtors !</p>
                <p>All of this on your findertips !</p>
                <button onClick={route}>Explore!</button>
            </div>
        </div>
    )
}

export default Home