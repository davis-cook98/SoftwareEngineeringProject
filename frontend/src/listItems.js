
import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import DashboardIcon from '@material-ui/icons/Dashboard';
import SearchIcon from '@material-ui/icons/Search';
import AssignmentIcon from '@material-ui/icons/Assignment';
import PeopleIcon from '@material-ui/icons/People';
import StarIcon from '@material-ui/icons/Star';

export const mainListItems = (
  <div>
    <ListItem button>
      <ListItemIcon>
        <DashboardIcon />
      </ListItemIcon>
      <ListItemText primary="Home" />
    </ListItem>
    <ListItem button>
      <ListItemIcon>
        <SearchIcon />
      </ListItemIcon>
      <ListItemText primary="Search" />
    </ListItem>
    <ListItem button>
      <ListItemIcon>
        <AssignmentIcon />
      </ListItemIcon>
      <ListItemText primary="Feed" />
    </ListItem>
    <ListItem button>
      <ListItemIcon>
        <PeopleIcon />
      </ListItemIcon>
      <ListItemText primary="Login" />
    </ListItem>
    <ListItem button>
      <ListItemIcon>
        <StarIcon />
      </ListItemIcon>
      <ListItemText primary="Favorites" />
    </ListItem>
  </div>
);