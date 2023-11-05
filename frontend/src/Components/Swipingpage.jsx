import React, { useState } from "react";
import './Swipingpage.css'

function Swipingpage() {
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
                <p>Artist Compatability</p>
                <p>Genre Compatability</p>
                <p>Song Preference</p>
                <p>Album Preference</p>
                <p style={textStyle}>You entered: {socialMedia}</p>
            </div>
        </div>
    );
}

export default Swipingpage;