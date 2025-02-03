import { useState } from "react";

const Home = () => {
    
    return (
        <div className="sections grid-rows-2 bg-[#121212] h-screen p-4 rounded-lg">
            <div className="top-listens grid-rows-2">
                <div className="category-btns text-white font-extralight space-x-2">
                    <button className="bg-[#1f1f20] px-3 py-1 bg-opacity-50 rounded-2xl">All</button>
                    <button className="bg-[#1f1f20] px-3 py-1 bg-opacity-50 rounded-2xl"> Music</button>
                    <button className="bg-[#1f1f20] px-3 py-1 bg-opacity-50 rounded-2xl">Podcast</button>
                    <button className="bg-[#1f1f20] px-3 py-1 bg-opacity-50 rounded-2xl">Audiobooks</button>
                </div>
                <div className="top-listen-list">

                </div>
            </div>
            <div className="made-for-you">

            </div>
            <div className="recently-played">

            </div>
        </div>
    );
}

export default Home;