import React from "react";
import TextField from "@material-ui/core/TextField";
import Link from "@material-ui/core/Link";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import Divider from "@material-ui/core/Divider";
import ExpansionPanel from "@material-ui/core/ExpansionPanel";
import axios from "axios";

import FavoriteButton from './FavoriteButton';

class SearchBar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      articles: [],
      query: ""
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange = (event) => {
    this.setState({ [event.target.name]: event.target.value });
  };

  handleSubmit = (event) => {
    event.preventDefault();
    var apiUrl = "/ReadAPI/search/?param=";
    var search = apiUrl.concat(this.state.query);
    axios.get(search).then((res) => {
      console.log(res);
      this.setState({ articles: res.data });
    });
  }
  render() {
    return (
      <div>
        <div>
          <form>
            <TextField
              name="query"
              id="standard-full-width"
              type="query"
              style={{ margin: "dense" }}
              placeholder="Enter your search"
              fullWidth
              value={this.state.query}
              margin="normal"
              onChange={this.handleChange}
            />
            <Button
              value="submit"
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              onClick={this.handleSubmit}
            >
              Search
            </Button>
          </form>
          <ExpansionPanel>
            <p>
              <ul>
                {this.state.articles.map((article) => (
                  <div>
                    <Link
                      href={article.Url}
                      rel="noopener noreferrer"
                      target="_blank"
                    >
                      <Typography variant="h6">{article.Title}</Typography>
                    </Link>
                    <Typography variant="h8">{article.Description}</Typography>
                    <FavoriteButton />
                    <Divider />
                  </div>
                ))}
              </ul>
            </p>
          </ExpansionPanel>
        </div>
      </div>
    );
  }
}

export default SearchBar;
