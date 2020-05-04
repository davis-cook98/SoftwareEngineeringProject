
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
