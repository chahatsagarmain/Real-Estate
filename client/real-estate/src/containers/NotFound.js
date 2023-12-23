import "./../stylesheets/notfound.css";
import error404 from "./../assets/error404.png";

function NotFound(){

    return (
        <div className="not-found">
            <h1>Your are at wrong route</h1>
            <img className="error404" src={error404} alt={"error 404"}/>
        </div>
    )
}

export default NotFound;