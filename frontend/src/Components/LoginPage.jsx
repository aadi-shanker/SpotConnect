import {useEffect, useState} from "react";


function LoginPage() {
    const CLIENT_ID = "257664458a0b4da38b7d2fb3898c059f"
    const REDIRECT_URI = "http://localhost:5173/social"
    const AUTH_ENDPOINT = "https://accounts.spotify.com/authorize"
    const RESPONSE_TYPE = "token"
    const SCOPES = 'user-top-read user-read-private user-read-email'
    const SPOTIFY_AUTH = `${AUTH_ENDPOINT}?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&response_type=${RESPONSE_TYPE}&scope=${SCOPES}`;


    const [token, setToken] = useState("")

    function redirectToSpotify(){
        window.open(SPOTIFY_AUTH)
    }

    useEffect(() => {
        const hash = window.location.hash
        let token = window.localStorage.getItem("token")

        if (!token && hash) {
            token = hash.substring(1).split("&").find(elem => elem.startsWith("access_token")).split("=")[1]

            window.location.hash = ""
            window.localStorage.setItem("token", token)
        }

        setToken(token)

    }, [])

    const logout = () => {
        setToken("")
        window.localStorage.removeItem("token")
    }

    return (
        <button onClick={redirectToSpotify} className="Button">Login with Spotify</button>

  );
}


export default LoginPage;
