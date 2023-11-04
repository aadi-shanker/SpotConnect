import React, { useState } from "react";
import SocialMediaInput from "./Components/socialMediaInput";

function App() {

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
    
    <SocialMediaInput/>
  );
}

export default App;
