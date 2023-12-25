import React from 'react';

function Card(props) {
    const { photo_main, title, area, price, state, city, id } = props;

    return (
        <div className="card">
            <img src={photo_main} alt="listing image" />
            <h2 id="title">{title}</h2>
            <p id="price">{price}</p>
            <p id="area">{area}</p>
            <p id="address">{city}, {state}</p>
            <button id="view-listing">View Listing</button>
        </div>
    );
}

export default Card;
