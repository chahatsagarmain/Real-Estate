import "./../stylesheets/searchbar.css"

function Searchbar(){

    return (
        <div className="search-bar">
            <label for="date">Date Published</label>
            <select name="published_order" id="date">
                <option value="Ascending">Ascending</option>
                <option value="Descending">Descending</option>
            </select>
            <label for="sale_type">Sale Type</label>
            <select name="sale_type" id="sale_type">
                <option value="For Sale">For Sale</option>
                <option value="For Rent">For Rent</option>
            </select>
            <label for="bedrooms">Bedrooms</label>
            <select name="bedrooms" id="bedrooms">
                <option value="0+">O+</option>
                <option value="1+">1+</option>
                <option value="2+">2+</option>
                <option value="3+">3+</option>
            </select>
            <label for="bathrooms">Bathrooms</label>
            <select name="bathrooms" id="bathrooms">
                <option value="0+">0+</option>
                <option value="1+">1+</option>
                <option value="2+">2+</option>
                <option value="3+">3+</option>
            </select>
            <label for="area">Area</label>
            <select name="area" id="area">
                <option value="0+">0+</option>
                <option value="1000+">1000+</option>
                <option value="2000+">2000+</option>
                <option value="3000+">3000+</option>
            </select>
            <label for="home_type">Home Type</label>
            <select name="home_type" id="home_type">
                <option value="Apartment">Apartment</option>
                <option value="Condo">Condo</option>
                <option value="Farmhouse">Farmhouse</option>
            </select>
            <label for="price">Price</label>
            <select name="price" id="price">
                <option value="0+">0+</option>
                <option value="1000+">1000+</option>
                <option value="2000+">2000+</option>
            </select>
            <label for="keywords">Keywords</label>
            <input name="keywords" type="text"></input>
        </div>
    )
}

export default Searchbar