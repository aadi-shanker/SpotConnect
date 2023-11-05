import React, { useState } from "react";
import './Swipingpage.css'
import GreenArrow from "../assets/GreenArrow.svg"
import RedArrow from "../assets/RedArrow.svg"
import { useNavigate } from "react-router-dom";

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

    let navigate = useNavigate();

    function SwipeRight() {
        navigate("/handle");
    }

    function SwipeLeft() {
        navigate("/swipe");
    }

    return (
        <div className='center-block'>
            <p>Artist Compatability</p>
            <p>Genre Compatability</p>
            <p>Song Preference</p>
            <p>Album Preference</p>
            <div className="row-space">
<               img className="red-arrow" onClick={SwipeLeft} alt="Swipe Left" src={RedArrow} />
                <img className="green-arrow" onClick={SwipeRight} alt="Swipe Right" src={GreenArrow} />
            </div>
            
        </div>
    );
}

export default Swipingpage;