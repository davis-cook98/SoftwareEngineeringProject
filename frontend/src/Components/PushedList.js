import React from "react";
import Link from "@material-ui/core/Link";
import Typography from "@material-ui/core/Typography";
import Divider from '@material-ui/core/Divider';
import axios from "axios";
import jwt_decode from 'jwt-decode';

export default class PushedList extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      articles: [],
    };
  }
  componentDidMount() {
    const userToken = localStorage.token;
    const decToken = jwt_decode(userToken);
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
