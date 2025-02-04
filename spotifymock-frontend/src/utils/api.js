import axios from 'axios';

// Fetch data from a protected endpoint
export const fetchProtectedData = async (endpoint) => {
    const token = localStorage.getItem('accessToken');

    try {
        const response = await axios.get(`http://localhost:8000${endpoint}`, {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        });
        return response.data;
    } catch (err) {
        console.error('Failed to fetch protected data', err);
        throw err;
    }
};
