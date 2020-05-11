import React from "react";
import ArrowUpwardIcon from '@material-ui/icons/ArrowUpward';
import axios from "axios";
import { IconButton } from "@material-ui/core";

class PushedButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
    };
  }
  togglePushed = () => {
    var apiUrl = "WriteAPI/togglePushed/?_id=";
    var query = apiUrl.concat(this.props._id);
    axios.get(query).then((res) => {
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
          onClick={this.togglePushed}
        >
          <ArrowUpwardIcon />
        </IconButton>
      </div>
    );
  }
}

export default PushedButton;
