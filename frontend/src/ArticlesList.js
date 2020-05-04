import React from "react";
import axios from "axios";

export default class ArticlesList extends React.Component {
  state = {
    articles: [],
  };

  componentDidMount() {
    axios.get("/ReadAPI/getAll/?title=").then((res) => {
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
