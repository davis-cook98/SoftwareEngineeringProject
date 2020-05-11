import React from "react";
import Link from "@material-ui/core/Link";
import Typography from "@material-ui/core/Typography";
import Divider from "@material-ui/core/Divider";
import FavoriteButton from "../Components/FavoriteButton";
import PushedButon from '../Components/PushedButton';
import jwt_decode from "jwt-decode";
import axios from "axios";

//Renders the articles on the top of app.js
export default class ArticlesList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      articles: [],
      admin: false,
    };
  }

  componentDidMount() {
    var userToken = localStorage.token;
    if (userToken === "undefined") {
      var decToken = jwt_decode(userToken);
      this.Username = decToken.identity.Username;
      //Currently does not work, working on fix
      if (this.Username === "admin"){
        this.setState({ admin: true });      
      }
    }
    var apiUrl = "/ReadAPI/getAll/?title=";
    var search = apiUrl.concat(this.props.query);
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
              <Typography variant="h6">{article.Title}</Typography>
            </Link>
            <Typography variant="h8">{article.Description}</Typography>
            {this.state.admin && (
              <PushedButon _id={article._id} />
            )}
            {localStorage.token ? (
              <FavoriteButton _id={article._id} username={this.Username} />
            ) : null}
            <Divider />
          </div>
        ))}
      </ul>
    );
  }
}
