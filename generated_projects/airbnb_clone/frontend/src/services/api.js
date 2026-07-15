import axios from 'axios';

const API_URL = '/api';

export const fetchProperties = () => axios.get(`${API_URL}/properties`);
export const fetchPropertyById = (id) => axios.get(`${API_URL}/properties/${id}`);
export const registerUser = async ({ email, password }) => await axios.post(`${API_URL}/register`, { email, password });
export const loginUser = async ({ email, password }) => await axios.post(`${API_URL}/login`, { email, password });
export const fetchUserProfile = () => axios.get(`${API_URL}/user`);

export default API_URL;