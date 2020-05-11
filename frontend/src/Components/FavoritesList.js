import React from "react";
import Link from "@material-ui/core/Link";
import Typography from "@material-ui/core/Typography";
import Divider from '@material-ui/core/Divider';
import axios from "axios";
import jwt_decode from 'jwt-decode';
import FavoriteButton from '../Components/FavoriteButton'

//Gets the users favorites, and returns them (bottom of app.js)
export default class FavoritesList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      articles: [],
    };
  }
  componentDidMount() {
    //Get jwt from localStorage, decode it, setup query, call
    var userToken = localStorage.token;
    var decToken = jwt_decode(userToken);
    this.Username = decToken.identity.Username;
    var apiUrl = "/ReadAPI/getFavorites/?username=";
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
            <FavoriteButton _id={ article._id } username={ this.Username }/>
            <Divider />
          </div>
        ))}
      </ul>
    );
  }
}
