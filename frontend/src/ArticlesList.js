import React from "react";
import axios from "axios";

export default class ArticlesList extends React.Component {

  constructor(props){
    super(props);
    this.state = {
      articles: [],
    }
  }
  componentDidMount() {
    var apiUrl = "/ReadAPI/getAll/?title=";
    var search = apiUrl.concat(this.props.query)
    axios.get(search).then((res) => {
      console.log(res);
      this.setState({ articles: res.data });
    });
  }

  render() {
    return (
      <ul>
        {this.state.articles.map((article) => (
          <li>{article.Title}>{article.ID}</li>
        ))}
      </ul>
    );
  }
}
