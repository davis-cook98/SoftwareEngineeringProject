import axios from "axios";

const axios = require("axios").default;

const ReadAPI = axios.create({
  baseURL: "http://127.0.0.1:5000/ReadAPI",
  withCredentials: true,
  headers: {
    "Content-Type": "application/vnd.api+json",
  },
});

async function getOne(input) {
  try {
    const response = await axios.get("http://127.0.0.1:5000/ReadAPI/getOne/", {
      params: {
        title: input,
      },
      config,
    });
    console.log(response);
  } catch (error) {
    console.log(error);
  }
}

async function getAll(input) {
  try {
    const response = await axios.get("http://127.0.0.1:5000/ReadAPI/getAll/", {
      params: {
        title: input,
      },
      config,
    });
    console.log(response);
  } catch (error) {
    console.log(error);
  }
}

export default ReadAPI;