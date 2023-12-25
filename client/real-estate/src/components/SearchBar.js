import "./../stylesheets/searchbar.css";
import { useState } from "react";
import { useContext } from "react";
import context from "../context/context";


const initialInputSearch = {
  "published_order": "Ascending",
  "sale_type": "FOR_SALE",
  "bedrooms": "0+",
  "bathrooms": "0+",
  "area": "0+",
  "price": "0+",
  "home_type": "APARTMENT",
  "keywords": ""
};

function Searchbar() {
    const [inputSearch, setInputSearch] = useState(initialInputSearch)

    const {listings,setListings} = useContext(context)
  
    function inputChange(event){
      const name = event.target.name
      const value = event.target.value
  
      setInputSearch({...inputSearch, [name]: value})
    }

    function sumbit(event){
        submitForm(event)
    }

    async function submitForm(event) {
        event.preventDefault()
        try {
          const form = new FormData();
      
          form.append("published_order", inputSearch.published_order);
          form.append("sale_type", inputSearch.sale_type);
          form.append("bedrooms", inputSearch.bedrooms);
          form.append("bathrooms", inputSearch.bathrooms);
          form.append("area", inputSearch.area);
          form.append("price", inputSearch.price);
          form.append("home_type", inputSearch.home_type);
          form.append("keywords", inputSearch.keywords);
      
        
          const options = {
            method: "POST",
            body: form,
            credentials: 'include' 
          }
      
          const response = await fetch("http://localhost:8000/api/listings/search", options);
          const responseData = await response.json();
          setTimeout(()=>{},1000)
          if(response.ok){
            setListings(responseData)
            console.log(responseData)
            //console.log(responseData)
            
          }
          else{
            console.log(responseData)
          }
      
        } catch (error) {
            alert("First log in")
          console.error('Error:', error);
        }
      }
      
    return (
      <div className="search-bar">
        <form encType="multipart/form-data" id="search-form" className="search-form-grid" onSubmit={sumbit}>
          <div className="grid-row">
            <div className="grid-item">
              <label htmlFor="date">Date Published</label>
              <select name="published_order" id="date" onChange={inputChange} value={inputSearch.published_order}>
                <option value="Ascending">Ascending</option>
                <option value="Descending">Descending</option>
              </select>
            </div>
            <div className="grid-item">
              <label htmlFor="sale_type">Sale Type</label>
              <select name="sale_type" id="sale_type" onChange={inputChange} value={inputSearch.sale_type}>
                <option value="FOR_SALE">FOR_SALE</option>
                <option value="FOR_RENT">FOR_RENT</option>
              </select>
            </div>
            <div className="grid-item">
              <label htmlFor="bedrooms">Bedrooms</label>
              <select name="bedrooms" id="bedrooms" onChange={inputChange} value={inputSearch.bedrooms}>
                <option value="0+">0+</option>
                <option value="1+">1+</option>
                <option value="2+">2+</option>
                <option value="3+">3+</option>
              </select>
            </div>
            <div className="grid-item">
              <label htmlFor="bathrooms">Bathrooms</label>
              <select name="bathrooms" id="bathrooms" onChange={inputChange} value={inputSearch.bathrooms}>
                <option value="0+">0+</option>
                <option value="1+">1+</option>
                <option value="2+">2+</option>
                <option value="3+">3+</option>
              </select>
            </div>
          </div>
          <div className="grid-row">
            <div className="grid-item">
              <label htmlFor="area">Area</label>
              <select name="area" id="area" onChange={inputChange} value={inputSearch.area}>
                <option value="0+">0+</option>
                <option value="1000+">1000+</option>
                <option value="2000+">2000+</option>
                <option value="3000+">3000+</option>
              </select>
            </div>
            <div className="grid-item">
              <label htmlFor="home_type">Home Type</label>
              <select name="home_type" id="home_type" onChange={inputChange} value={inputSearch.home_type}>
                <option value="APARTMENT">APARTMENT</option>
                <option value="CONDO">CONDO</option>
                <option value="FARMHOUSE">FARMHOUSE</option>
              </select>
            </div>
            <div className="grid-item">
              <label htmlFor="price">Price</label>
              <select name="price" id="price" onChange={inputChange} value={inputSearch.price}>
                <option value="0+">0+</option>
                <option value="1000+">1000+</option>
                <option value="2000+">2000+</option>
              </select>
            </div>
            <div className="grid-item">
              <label htmlFor="keywords">Keywords</label>
              <input name="keywords" type="text" onChange={inputChange} value={inputSearch.keywords}></input>
            </div>
          </div>
          <div className="grid-row">
            <div className="grid-item">
              <button>Search</button>
            </div>
          </div>
        </form>
      </div>
    );
  }
  
  export default Searchbar;
  