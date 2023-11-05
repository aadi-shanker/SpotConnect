import { useNavigate } from "react-router-dom";
import React, { useState } from "react";
import './SocialMediaInput.css'

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
        navigate("/handle");
    }


    return (
        <div className='socialMediaInputPage'>
            <div className="socialMediaInputContainer">
                <label htmlFor="socialMediaInput" style={textStyle}>Enter your social media and specify what it is (Ex: @hackatuci - Instagram):</label>
                <input
                    type="text"
                    id="socialMediaInput"
                    value={socialMedia}
                    onChange={handleSocialMediaChange}
                />
                <p style={textStyle}>You entered: {socialMedia}</p>
                <button type="Submit" onClick={handleClick}>
                Submit
                </button>
            </div>
        </div>
    );
}

export default SocialMediaInput;
