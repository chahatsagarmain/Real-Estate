import Searchbar from "../components/SearchBar";
import Card from "../components/Card";
import context from "../context/context";
import { useContext } from "react";

function ListingPage() {
    const { listings, setListings } = useContext(context);

    return (
        <div className="listings-page">
            <Searchbar />
            {listings && listings[0] && (
                <Card
                    photo_main={listings[0].photo_main}
                    title={listings[0].title}
                    area={listings[0].area}
                    price={listings[0].price}
                    state={listings[0].state}
                    city={listings[0].city}
                    id={listings[0].id}
                />
            )}
        </div>
    );
}

export default ListingPage;
