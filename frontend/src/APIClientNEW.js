import axios from 'axios';

const axios = require('axios').default;

var config = { headers: {  
  'Content-Type': 'application/json',
  'Access-Control-Allow-Origin': '*'}
}

async function getOne(input) {
  try {
    const response = await axios.get("http://localhost:5000", { title: input }, config);
    console.log(response);
  }
  catch (error) {
    console.log(error);
  }
}

getOne("c")