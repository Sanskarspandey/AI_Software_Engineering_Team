import React from 'react';

function SearchBar({ searchTerm, setSearchTerm }) {
  return (
    <form>
      <input type="text" value={searchTerm} onChange={(event) => setSearchTerm(event.target.value)} placeholder="Search properties..." />
    </form>
  );
}

export default SearchBar;