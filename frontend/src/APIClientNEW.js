import axios from 'axios';

const axios = require('axios').default;

var config = { headers: {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'}
  }

async function getOne(input) {
    try {
      const response = await axios.get("http://127.0.0.1:5000/ReadAPI/getOne/", {
      params: {
        title: input
      }, config});
      console.log(response);
    }
    catch (error) {
      console.log(error);
    }
  }

  async function getAll(input) {
    try {
      const response = await axios.get("http://127.0.0.1:5000/ReadAPI/getAll/", {
        params: {
          title: input
        }, config});
        console.log(response);
        }
        catch (error) {
          console.log(error);
        }
    }
    async function toggleFav(input, input2) {
      try {
        const response = await axios.post("http://127.0.0.1:5001/WriteAPI/toggleFavorite/", {
          params: {
            title: input,
            name: input2
          }, config});
          console.log(response);
          }
          catch (error) {
            console.log(error);
          }
      }
