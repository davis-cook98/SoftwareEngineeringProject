
import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import DashboardIcon from '@material-ui/icons/Dashboard';
import SearchIcon from '@material-ui/icons/Search';
import AssignmentIcon from '@material-ui/icons/Assignment';
import PeopleIcon from '@material-ui/icons/People';
import { Link } from "react-router-dom";
import { render } from "react-dom";
import { hasRole, isAllowed } from './Auth';

const user = {
  roles: ['user'],
  rights: ['can_favorite']
 }

export const mainListItems = (
  
    <div>
      <ListItem button>
        <ListItemIcon>
          <DashboardIcon/>
        </ListItemIcon>
        <ListItemText primary="Home" />
      </ListItem>
      <ListItem button>
        <ListItemIcon>
          <AssignmentIcon />
        </ListItemIcon>
        <ListItemText primary="Feed" />
      </ListItem>
      <ListItem button component={Link} to="/login">
        <ListItemIcon>
          <PeopleIcon />
        </ListItemIcon>
        <ListItemText primary="Login"/>
      </ListItem>
    </div>
);