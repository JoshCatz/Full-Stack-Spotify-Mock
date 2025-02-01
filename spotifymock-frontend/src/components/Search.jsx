import Home from '../assets/imgs/HomeIcon.png'

const Search = () => {
    return (
        <div className="text-white bg-black flex p-2 items-center justify-between">
            <div className="navigating-btns flex items-center space-x-4">
                <div className="window-btns text-xs space-x-2">
                    <button className="px-1 bg-red-500 rounded-4xl">x</button>
                    <button className="px-1 bg-yellow-500 rounded-4xl">-</button>
                    <button className="px-1 bg-green-500 rounded-4xl">+</button>
                </div>
                <div className="text-2xl font-thin space-x-5">
                    <button>&lt;</button>
                    <button>&gt;</button>
                </div>
            </div>
            <div className="search-bar flex items-center space-x-2">
                <button className="home-btn bg-[#1f1f20] px-1 py-3 rounded-4xl flex justify-center">
                    <img className="w-[50%]" src={Home} alt="" />
                </button>
                <form action="search" className="search-input px-2 py-3 bg-[#1f1f20] rounded-4xl space-x-2">
                    <button>*</button>
                    <input type="search" placeholder="What do you want to play?"/>
                </form>
            </div>
            <div className="profile bg-blue-400 py-2 px-4 rounded-4xl">
                <button>J</button>
            </div>
        </div>
    );
}

export default Search;