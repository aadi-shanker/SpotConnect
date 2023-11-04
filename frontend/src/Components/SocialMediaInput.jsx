import React, { useState } from "react";
import './SocialMediaInput.css'

function SocialMediaInput() {
    const [socialMedia, setSocialMedia] = useState('');

    const handleSocialMediaChange = (e) => {
        setSocialMedia(e.target.value);
    };

    // Inline style object for text alignment
    const textStyle = {
        color: 'green',
        textAlign: 'center',
    };

    return (
        <div className='socialMediaInputPage'>
            <div className="socialMediaInputContainer">
                <label htmlFor="socialMediaInput" style={textStyle}>Enter your social media and specifiy what it is (Ex: @hackatuci - instagram):</label>
                <input
                    type="text"
                    id="socialMediaInput"
                    value={socialMedia}
                    onChange={handleSocialMediaChange}
                />
                <p style={textStyle}>You entered: {socialMedia}</p>
            </div>
        </div>
    );
}

export default SocialMediaInput;
