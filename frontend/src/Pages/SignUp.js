import React from "react";
import Avatar from "@material-ui/core/Avatar";
import Button from "@material-ui/core/Button";
import CssBaseline from "@material-ui/core/CssBaseline";
import TextField from "@material-ui/core/TextField";
import Grid from "@material-ui/core/Grid";
import Box from "@material-ui/core/Box";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import Typography from "@material-ui/core/Typography";
import { withStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
import { Link } from "react-router-dom";
import axios from "axios";

const styles = (theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: "100%", // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
});

class SignUp extends React.Component {
  constructor() {
    super();
    this.state = { username: "", password: "", first_name: "", last_name: "" };
  }

  handleChange = (event) => {
    this.setState({ [event.target.name]: event.target.value });
  };
  handleSubmit = (event) => {
    event.preventDefault();
    var apiUrl = "/WriteAPI/addUser/?";
    var query = apiUrl.concat(
      "username=" +
        this.state.username +
        "&" +
        "password=" +
        this.state.password +
        "&" +
        "first_name=" +
        this.state.first_name + 
        "&" +
        "last_name=" +
        this.state.last_name
    );
    axios.post(query).then((res) => {
      console.log(res);
      console.log(res.data);
      
    })
    .catch(Error =>{
      console.log(Error)
    });

  };
  render() {
    const { classes } = this.props;
    return (
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <div className={classes.paper}>
          <Avatar className={classes.avatar}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign up
          </Typography>
          <form
            className={classes.form}
            noValidate
          >
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="unsername"
              label="Username"
              name="username"
              value={this.state.username}
              onChange={this.handleChange}
              autoComplete="username"
              autoFocus
            />
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              name="password"
              label="Password"
              type="password"
              id="password"
              value={this.state.password}
              onChange={this.handleChange}
              autoComplete="current-password"
            />
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              name="first_name"
              label="First name"
              type="first_name"
              id="first_name"
              value={this.state.first_name}
              onChange={this.handleChange}
              autoComplete="first_name"
            />
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              name="last_name"
              label="Last name"
              type="last_name"
              id="last_name"
              value={this.state.last_name}
              onChange={this.handleChange}
              autoComplete="last_name"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
              onClick={this.handleSubmit}
            >
              Sign Up
            </Button>
            <Grid container>
              <Grid item xs>
                <Grid item component={Link} to="/">
                  <Typography>Don't want to commit?</Typography>
                </Grid>
              </Grid>
            </Grid>
          </form>
        </div>
        <Box mt={8}></Box>
      </Container>
    );
  }
}

export default withStyles(styles)(SignUp);
