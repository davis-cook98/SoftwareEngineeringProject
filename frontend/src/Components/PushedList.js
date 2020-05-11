import React from "react";
import Link from "@material-ui/core/Link";
import Typography from "@material-ui/core/Typography";
import Divider from '@material-ui/core/Divider';
import axios from "axios";
import jwt_decode from 'jwt-decode';

//Returns all pushed articles for a user (middle of app.js)
export default class PushedList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      articles: [],
    };
  }
  componentDidMount() {
    //Get jwt from localStorage, decodes it, setup API call, API call
    var userToken = localStorage.token;
    var decToken = jwt_decode(userToken);
    var apiUrl = "/ReadAPI/getPushed/?username=";
    var search = apiUrl.concat(decToken.identity.Username);
    axios.get(search).then((res) => {
      console.log(res);
      this.setState({ articles: res.data });
    });
  }

  render() { 
    return (
      <ul>
        {this.state.articles.map((article) => (
          <div>
            <Link href={article.Url} rel="noopener noreferrer" target="_blank">
            <Typography variant="h6">
              { article.Title }
            </Typography>
            </Link>
            <Typography variant="h8">
              { article.Description }
            </Typography>
            <Divider />
          </div>
        ))}
      </ul>
    );
  }
}
