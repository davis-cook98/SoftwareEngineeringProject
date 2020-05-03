import React from 'react';
import ReactDOM from 'react-dom';
import {
    BrowserRouter as Router,
    Route
  } from "react-router-dom";
import './index.css';
import App from './App';
import { Security, LoginCallback } from '@okta/okta-react';
import * as serviceWorker from './serviceWorker';

const CALLBACK_PATH = '/implicit/callback';

const routing = (
    <Router>
            <Route exact path="/" component={App} />
            <Route path={CALLBACK_PATH} component={LoginCallback} />
    </Router>
)

ReactDOM.render(routing, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();