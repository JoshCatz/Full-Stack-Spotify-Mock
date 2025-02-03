import library from '../assets/imgs/LibraryIcon.png'
import favorites from '../assets/imgs/FavoritesIcon.png'

const Navbar = () => {
    return (
        <div className="p-2 bg-[#121212] h-screen rounded-lg">
            <button>
                <img src={library} alt="" />
            </button>
            <button>
                <img  src={favorites} alt="" />
            </button>
        </div>
    );
}

export default Navbar;