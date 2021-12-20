import axios from 'axios';

const apiClient = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    withCredentials: true,
    headers:{
        Accept: 'application/json',
        'Content-Type': 'application/json'
    }
})

export default {
    getServices(){
        return apiClient.get("/api/services-list/")
    },
    getClients(){
        return apiClient.get("/api/clients-list/")
    },
    getCause(){
        return apiClient.get("/api/cause-list/")
    },
    getOutageType(){
        return apiClient.get("/api/outage_type-list/")
    },
};