import Searchbar from "../components/SearchBar";
import Card from "../components/Card";
import context from "../context/context";
import { useContext } from "react";
import "./../stylesheets/listingpage.css"

function ListingPage() {
    const { listings } = useContext(context);

    return (
        <div className="listings-page">
            <Searchbar />
            <div className="listings">
            {listings && listings[0] && (
                // <Card
                //     photo_main={listings[0].photo_main}
                //     title={listings[0].title}
                //     area={listings[0].area}
                //     price={listings[0].price}
                //     state={listings[0].state}
                //     city={listings[0].city}
                //     id={listings[0].id}
                // />
                listings.map((value,idx) => {
                    return <Card
                    photo_main={value.photo_main}
                    title={value.title}
                    area={value.area}
                    price={value.price}
                    state={value.state}
                    city={value.city}
                    id={value.id}
                    key = {idx}
                />
                })
            )}
            </div>
        </div>
    );
}

export default ListingPage;
