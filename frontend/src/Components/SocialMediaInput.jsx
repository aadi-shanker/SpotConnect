import { useNavigate } from "react-router-dom";
import React, { useState } from "react";
import './SocialMediaInput.css'
import Zotify from "../assets/Zotify.svg";
import Crossbar from "../assets/crossbar.png"
import SocialHandle from "../assets/SocialHandle.png"
import LoginButton from "../assets/LoginButton.svg"

function SocialMediaInput() {
    const [socialMedia, setSocialMedia] = useState('');

    const handleSocialMediaChange = (e) => {
        setSocialMedia(e.target.value);
    };

    const handleSubmit = () => {
        // You can handle the submission here, e.g., send the data to the backend
        console.log("Submit button clicked. Data: ", socialMedia);
    };

    // Inline style object for text alignment
    const textStyle = {
        color: 'green',
    };

    let navigate = useNavigate();

    function handleClick() {
        navigate("/swipe");
    }


    return (
        <div className='centerpiece'>
                <img className="zotify-logo" alt="Zotify Logo" src={Zotify} />
                <img className="cross-bar" src={Crossbar} />
                <div className="close-stack">
                    <img src={SocialHandle} />
                    <input
                    type="text"
                    className="rounded-text-box"
                    value={socialMedia}
                    onChange={handleSocialMediaChange}
                />
                </div>
                <img className="login-button" onClick={handleClick} alt="Login Button" src={LoginButton} />
        </div>
    );
}

export default SocialMediaInput;
