import axios from 'axios' ;


const READ_URI = 'http://localhost:4433';
const WRITE_URI = 'http://localhost:4433/WRITE';


const clientREAD = axios.create(readURL: READ_URI,
json: true});

const clientWrite = axios.create(writeURL: WRITE_URI,
json: true});

class APIClient {
  constructor(accessToken) {
    this.accessToken = accessToken;
  }
  
}
