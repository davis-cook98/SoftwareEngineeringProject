import React from "react";
import Avatar from "@material-ui/core/Avatar";
import Button from "@material-ui/core/Button";
import CssBaseline from "@material-ui/core/CssBaseline";
import TextField from "@material-ui/core/TextField";
import Grid from "@material-ui/core/Grid";
import Box from "@material-ui/core/Box";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import Typography from "@material-ui/core/Typography";
import Container from "@material-ui/core/Container";
import { Link } from "react-router-dom";
import { withStyles } from '@material-ui/core/styles';
import axios from "axios";

const styles = theme => ({
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

class Login extends React.Component {
  constructor() {
    super();
    this.state = { username : '',
                   password : ''
     };
     this.handleChange = this.handleChange.bind(this);
    }
  
  handleChange = (event) => {
    this.setState({ [event.target.name]: event.target.value});
  }
  handleSubmit = event => {
    event.preventDefault();
    var apiUrl = "/ReadAPI/findUser/?";
    var query = apiUrl.concat('username=' + this.state.username + '&' + 'password=' + this.state.password);
    axios.get(query)
    .then(res=>{
      console.log(res);
      console.log(res.data);
      localStorage.setItem("token", res.data.Token);
    })
    .catch(Error=>{
      console.log(Error);
    })
  }
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
            Sign in
          </Typography>
          <form className={classes.form} Validate>
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="username"
              label="Username"
              name="username"
              autoComplete="username"
              value={this.state.username}
              onChange={this.handleChange}
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
              autoComplete="current-password"
              value={this.state.password}
              onChange={this.handleChange}
              autoFocus
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
              onClick={ this.handleSubmit }
            >
              Sign In
            </Button>
            <Grid container>
              <Grid item component={Link} to="/signup">
                <Typography>Don't have an account? Sign up here!</Typography>
              </Grid>
              <Grid item component={Link} to="/">
                <Typography>Return to home screen</Typography>
              </Grid>
            </Grid>
          </form>
        </div>
        <Box mt={8}></Box>
      </Container>
    );
  }
}

export default withStyles(styles)(Login)
