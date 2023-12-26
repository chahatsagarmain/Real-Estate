import React, { useState, useEffect } from "react";
import { useContext } from "react";
import context from "../context/context";
import "./../stylesheets/listingsdetail.css";

function ListingDetail() {
  const [listingDetailed, setListingDetailed] = useState("");
  const [realtor, setRealtor] = useState([{}]);
  const { listings } = useContext(context);

  useEffect(() => {

    const fetchData = async () => {
      const url_path = window.location.pathname.split("/");
      const listing_id = url_path[url_path.length - 1];
      const listing = listings.find(
        (element) => element.id === Number.parseInt(listing_id)
      );

      if (listing) {
        setListingDetailed(listing);
        await getRealtor(listing.realtor);
      } else {
        console.error("Listing not found");
      }
    };

    fetchData();
  }, []);

  async function getRealtor(realtorId) {
    try {
      const options = {
        method: "GET",
        credentials: "include",
      };

      const response = await fetch(
        `http://localhost:8000/api/realtor/${realtorId}`,
        options
      );

      const response_data = await response.json();

      if (!response.ok) {
        console.error("Error fetching realtor");
      } else {
        setRealtor(response_data);
      }
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div className="listing-detail">
      {listingDetailed && realtor ? (
        <>
          <div className="row-1">
            <div className="row-1-col-1">
              <h2>{listingDetailed.title}</h2>
              <img
                src={`${listingDetailed.photo_main}`}
                alt="main photo"
              />
            </div>
            <div className="row-1-col-2">
              <h3>{realtor.name}</h3>
              <img
                src={`${realtor[0].photo}`}
                alt="realtor photo"
              />
              <p>Email: {realtor[0].email}</p>
              <p>Phone: {realtor[0].phone}</p>
              <p>Description: {realtor[0].description}</p>
            </div>
          </div>
          <div className="row-2">
            <p>Address: {listingDetailed.address}</p>
            <p>City: {listingDetailed.city}</p>
            <p>State: {listingDetailed.state}</p>
            <p>Zipcode: {listingDetailed.zipcode}</p>
            <p>Description: {listingDetailed.description}</p>
            <p>Sale Type: {listingDetailed.sale_type}</p>
            <p>Listing Date: {listingDetailed.listing_date}</p>
          </div>
          <div className="row-3">
            {(() => {
              const images = [];
              for (let i = 1; i <= 10; i++) {
                console.log(realtor)
                console.log(realtor.email)
                const photo_url = `${listingDetailed[`photo_${i}`]}`;
                images.push(<img key={i} src={photo_url} alt={i}/>);
              }
              return images;
            })()}
          </div>
        </>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default ListingDetail;
