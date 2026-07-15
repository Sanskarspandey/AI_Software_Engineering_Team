import React from 'react';
import PropertyCard from './PropertyCard.jsx';
import axios from 'axios';

function PropertyDetails({ match }) {
  const [property, setProperty] = useState(null);

  React.useEffect(() => {
    const fetchProperty = async () => {
      const response = await axios.get(`/api/properties/${match.params.id}`);
      setProperty(response.data);
    };
    fetchProperty();
  }, [match.params.id]);

  return (
    <div>
      {property ? <PropertyCard property={property} /> : 'Loading...'}
    </div>
  );
}

export default PropertyDetails;