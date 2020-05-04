import axios from "axios";

const axios = require("axios").default;

const WriteAPI = axios.create({
  baseURL: 'http://127.0.0.1:5000/WriteAPI',
  withCredentials: true,
  headers: {
    'Content-Type': 'application/vnd.api+json',
  },
});

async function toggleFav(input, input2) {
  try {
    const response = await axios.post(
      "http://127.0.0.1:5001/WriteAPI/toggleFavorite/",
      {
        params: {
          title: input,
          name: input2,
        },
        config,
      }
    );
    console.log(response);
  } catch (error) {
    console.log(error);
  }
}

export default WriteAPI;