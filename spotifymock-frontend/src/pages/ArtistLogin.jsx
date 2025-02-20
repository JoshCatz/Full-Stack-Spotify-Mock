import { useState } from "react";
import SpotifyLogo from '../assets/imgs/SpotifyLogo.png';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';

const ArtistLogin = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate(); // For redirecting upon successful login

    const handleSubmit = async (e) => {
        e.preventDefault(); // Prevent page refresh

        try {
            const response = await axios.post('http://localhost:8000/auth/jwt/create/', {
                username: username,
                password: password,
            });

            const { access, refresh } = loginResponse.data;

            localStorage.setItem('accessToken', access);
            localStorage.setItem('refreshToken', refresh);

            // Redirect the user to the artist dashboard/homepage
            navigate('/');

        } catch (err) {
            // Set error message if login fails
            if (err.response && err.response.data) {
                setError('Invalid username or password');
            } else {
                setError('Something went wrong. Please try again.');
            }
        }
    };
    
    return (
        <div className="bg-gradient-to-t from-black from-10% via-neutral-900 via-35% to-neutral-800 to-90% flex flex-col items-center justify-center h-screen space-y-5">
            <div className="login-card bg-[#121212] w-[80%] h-[90%] rounded-lg mt-8 px-4 py-2 pt-10 flex flex-col items-center text-white space-y-4">
                <img className="w-[50px] h-[50px]" src={SpotifyLogo} alt="" />
                <h1 className="text-3xl font-bold">Artist Log in to Spotify</h1>
                <p className="text-sm text-neutral-400">By Joshua Catzoela</p>

                <form onSubmit={handleSubmit} className="login-form flex flex-col space-y-3">
                    <label htmlFor="username" className="text-[0.8em] font-semibold">Email or username</label>
                    <input type="text" id="username" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Email or username" className="border border-solid border-gray-700 rounded-sm p-2"/>

                    <label htmlFor="password" className="text-[0.8em] font-semibold">Password</label>
                    <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" className="border border-solid border-gray-700 rounded-sm p-2"/>

                    <button type="submit" className="login-btn bg-green-500 rounded-3xl text-black font-bold px-35 py-3 mt-3">Log In</button>
                </form>

                {error && <p className="text-red-500 mt-2">{error}</p>}
                
                <Link to="/password-recovery" className="text-white underline mt-4">
                    Forgot your password?
                </Link>


                <p className="text-neutral-400 mt-4">
                    Don't have an account?{' '}
                    <Link to="/artist/signup" className="text-white underline">
                        Sign up for Spotify
                    </Link>
                </p>
            </div>

            <div className="footer bg-[#121212] w-full h-[10%] text-neutral-400 pt-4">
                <p className="text-center text-[0.7em]">This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply.</p>
            </div>
        </div>
    );
}

export default ArtistLogin;