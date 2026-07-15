import React from 'react';
import { useState } from 'react';
import PropertyCard from './PropertyCard.jsx';
import SearchBar from './SearchBar.jsx';

function Home() {
  const [properties, setProperties] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  React.useEffect(() => {
    fetch('/api/properties')
      .then(response => response.json())
      .then(data => setProperties(data));
  }, []);

  return (
    <div>
      <SearchBar searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
      {properties.filter(property => property.name.toLowerCase().includes(searchTerm.toLowerCase())).map((property) => (
        <PropertyCard key={property.id} property={property} />
      ))}
    </div>
  );
}

export default Home;