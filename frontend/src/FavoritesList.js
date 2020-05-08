import React from "react";
import Link from "@material-ui/core/Link";
import Typography from "@material-ui/core/Typography";
import Divider from '@material-ui/core/Divider';
import axios from "axios";

export default class FavoritesList extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      articles: [],
    };
  }
  componentDidMount() {
    var apiUrl = "/ReadAPI/getFavorites/?username=DAVIS";
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
