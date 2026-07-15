import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function Profile() {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  const fetchUser = async () => {
    try {
      const response = await axios.get('/api/user');
      setUser(response.data);
    } catch (error) {
      console.error(error.response.data.message);
    }
  };

  React.useEffect(() => {
    fetchUser();
  }, []);

  return (
    <div>
      {user ? <UserProfile user={user} /> : 'Loading...'}
    </div>
  );
}

function UserProfile({ user }) {
  const navigate = useNavigate();
  const logoutHandler = () => {
    localStorage.removeItem('token');
    navigate('/login');
  };

  return (
    <div>
      <h1>{user.name}</h1>
      <button onClick={logoutHandler}>Logout</button>
    </div>
  );
}

export default Profile;