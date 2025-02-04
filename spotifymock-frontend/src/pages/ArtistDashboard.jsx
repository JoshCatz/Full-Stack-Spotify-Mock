import React, { useEffect, useState } from 'react';
import { fetchProtectedData } from '../utils/api';

const ArtistDashboard = () => {
    const [data, setData] = useState(null);

    useEffect(() => {
        const getData = async () => {
            try {
                const result = await fetchProtectedData('/protected-endpoint/');
                setData(result);
            } catch (err) {
                console.error('Error fetching data:', err);
            }
        };

        getData();
    }, []);

    return (
        <div>
            <h1>Artist Dashboard</h1>
            {data ? <p>{JSON.stringify(data)}</p> : <p>Loading...</p>}
        </div>
    );
};

export default ArtistDashboard;
