import React from 'react';
import "./../stylesheets/card.css";
import { useNavigate } from 'react-router-dom';

function Card(props) {
    const { photo_main, title, area, price, state, city, id } = props;
    const navigate = useNavigate();

    function detailpage() {
        navigate(`/listing/${id}`);
    }

    const photo_url = `http://localhost:8000${photo_main}`;

    return (
        <div className="card">
            <img src={photo_url} alt="listing image" />
            <h2 id="title">{title}</h2>
            <p id="price">Price: {price}</p>
            <p id="area">Area (in sqft): {area}</p>
            <p id="address">City: {city}, {state}</p>
            <button id="view-listing" onClick={detailpage}>View Listing</button>
        </div>
    );
}

export default Card;
