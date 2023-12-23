import { useState } from "react";
import "./../stylesheets/login.css"
import { useContext } from "react";
import "./../context/context"
import context from "./../context/context";
import { useNavigate } from "react-router";

function Login(){
    const navigate = useNavigate()
    const [inputForm , setForm ] = useState({
        "email" : "",
        "password" : "",
      });

    const {userName , setUsername} = useContext(context)
    
    function inputFields(event){
        const field_name = event.target.name;
        const field_value = event.target.value;

        const newObj = {...inputForm,[field_name] : field_value} 

        setForm(newObj)
    }

    function sumbit(event){
        console.log(inputForm)
        if(!inputForm.email ||  !inputForm.password){
            return alert("Please enter all fields")
        }

    
        const temp_str = inputForm.password
        if(temp_str.length < 8){
            return alert("password should of atleast 8 digits")
        }
        
        sendinputForm(event);

    }

    async function sendinputForm(event){
        
        try{
            event.preventDefault()

            const form = new FormData()
            form.append('email',inputForm.email);
            form.append('password',inputForm.password);

            console.log(form);
            const options = {
                method : "POST",
                body : form,
                credentials : 'include'
            }
            const response = await fetch("http://localhost:8000/api/users/login/" , options).then(
                (response) => response.json()
            ).catch(error => {
                console.log(error)
            })

            if(response.status >= 300){
                alert(response.message)
                console.log(response)
            }
            else{
                setUsername(response.username)
                console.log(response)
                console.log(userName)
                navigate("/1")
                
            }

        }
        catch(error){
            console.log(error)
        }

        
    }

    return(
        <header>
        <div className="register">
            <div className="register-box">
                <p>Login</p>
                <form encType="multipart/form-data" onSubmit={sumbit}>
                    <label>Email</label>
                    <input type="email" name="email" onChange={inputFields}></input>
                    <label>Password</label>
                    <input type="password" name="password" onChange={inputFields}></input>
                    <button name="sumbit" >Sumbit</button>
                </form>
            </div>
        </div>
        </header>
    )
}

export default Login