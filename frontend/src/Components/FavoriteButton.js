import React from "react";
import FavoriteIcon from "@material-ui/icons/Favorite";
import axios from "axios";
import { IconButton } from "@material-ui/core";

class FavoriteButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  toggleFavorite() {
    var apiUrl = "/toggleFavorite/?name=";
    var query = apiUrl.concat(this.props.name + "&title=" + this.props.title);
    axios.post(query).then((res) => {
      console.log(res);
    });
  }
  render() {
    return (
      <div>
        <IconButton
          value="submit"
          type="submit"
          size="medium"
          variant="contained"
          color="primary"
          //onClick={this.toggleFavorite}
        >
          <FavoriteIcon />
        </IconButton>
      </div>
    );
  }
}

export default FavoriteButton;
