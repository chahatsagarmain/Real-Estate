import { useNavigate } from "react-router";
import "./../stylesheets/contact.css"
import { useState } from "react";

function Contact() {

    const [input, setInput] = useState({
        "subject": "",
        "message": ""
    })

    const navigate = useNavigate()

    function inputChange(event) {
        const name = event.target.name
        const value = event.target.value
        console.log(input)
        setInput({ ...input, [name]: value })
    }

    function sumbit(event) {
        event.preventDefault()
        sendData()
    }

    async function sendData() {
        try {
            const form = new FormData()
            form.append("subject",input.subject)
            form.append("message",input.message)

            const options = {
                method: "POST",
                body: form,
                credentials: 'include'
            }

            const response = await fetch("http://localhost:8000/api/contacts/", options).then(response => response.json()).catch(error => {
                console.log(error)
                alert(error)
            })

            if (response.status >= 300) {
                alert(response)
                console.log(response)
            }
            else {
                alert("Message Sent")
                navigate("/")
            }
        }
        catch(error){
            alert(error)
            console.log(error)
        }
    }


    return (
        <div className="contact">
            <div className="contact-form">
                <h2>Contact Us</h2>
                <form encType="multipart/form-data" onSubmit={sumbit}>
                    <label>Subject</label>
                    <input type="text" placeholder="Enter the subject here" name="subject" onChange={inputChange}></input>
                    <label>Message</label>
                    <textarea placeholder="Enter your message here" name="message" onChange={inputChange}></textarea>
                    <button name="sumbit" onSumbit={sumbit}>Sumbit</button>
                </form>
            </div>
        </div>
    )
}


export default Contact