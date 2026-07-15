import React from 'react';
import { Link } from 'react-router-dom';

function PropertyCard({ property }) {
  return (
    <div>
      <Link to={`/property/${property.id}`}><img src={property.image} alt={property.name} /></Link>
      <h2>{property.name}</h2>
      <p>{property.location}</p>
      <p>${property.price}</p>
    </div>
  );
}

export default PropertyCard;