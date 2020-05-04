import axios from 'axios';

const axios = require('axios');


const READ_URI = 'http://localhost:500';


class APIClient {
  constructor(accessToken) {
    this.accessToken = accessToken;
  }

getSingleArticle() {
  return this.perform('get', '0/ReadAPI/getOne/');
}

getAllArticles() {
  return this.perform('get', '0/ReadAPI/getAll/');
}

addfavorite() {
  return this.perform('post', '0/WriteAPI/addFavorite/')
}

removeFavorite() {
  return this.perform('post', '/WriteAPI/removeFavorite/')
}
async perform (method, resource, data) {
   return client({
     method,
     url: resource,
     data,
     headers: {
       Authorization: `Bearer ${this.accessToken}`
     }
   }).then(resp => {
     return resp.data ? resp.data : [];
   })
 }
}

export default APIClient;
