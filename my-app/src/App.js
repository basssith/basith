
import React, { useState } from 'react';
import './App.css';

const App = () => {
    const [entries, setEntries] = useState([
        {
            destination: 'Paris',
            date: 'October 1, 2024',
            description: 'This was my first trip to Paris! I visited the Eiffel Tower, enjoyed delicious pastries, and explored the charming streets of Montmartre. The view from the top of the tower was breathtaking!',
            image: 'paris.jpg', // Ensure this image is in the public folder
        },
        {
            destination: 'Tokyo',
            date: 'October 10, 2024',
            description: "Tokyo was an incredible experience! I loved the vibrant culture, the food, and the mix of traditional and modern architecture. Don't miss the cherry blossoms in spring!",
            image: 'tokyo.jpg', // Ensure this image is in the public folder
        },
        {
            destination: 'Spain',
            date: 'October 10, 2024',
            description: 'Spain was a wonderful country. The people are very kind, and the places are truly beautiful.',
            image: 'spain.jpg', // Ensure this image is in the public folder
        },
    ]);

    const removeEntry = (index) => {
        setEntries(entries.filter((_, i) => i !== index));
    };

    return (
        <div>
            <header>
                <h1>My Travel Journal</h1>
            </header>

            {entries.map((entry, index) => (
                <article key={index}>
                    <h2>Destination: {entry.destination}</h2>
                    <img src={entry.image} alt={`Image of ${entry.destination}`} />
                    <p>Date: {entry.date}</p>
                    <p>{entry.description}</p>
                    <button onClick={() => alert(`Added entry for ${entry.destination}`)}>ADD</button>
                    <button onClick={() => removeEntry(index)}>Remove</button>
                </article>
            ))}

            <footer>
                <p>© 2024 My Travel Journal</p>
            </footer>
        </div>
    );
};

export default App;
