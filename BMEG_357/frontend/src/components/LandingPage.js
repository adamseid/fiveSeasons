import React, { Component } from "react";
import { render } from "react-dom";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import Filter from "./Filter";
import {
    BrowserRouter as Router, 
    Switch, 
    Route, 
    Link, 
    useHistory
} from "react-router-dom";


export default class LandingPage extends Component {
  constructor(props) {
    super(props);
  }
  
  render() {
    return (
        <Grid container spacing={1}>
            <Grid item xs={12} align="center" class = "title">
                <Typography component="h4" variant="h4" color = "secondary">
                    Cactus Track
                </Typography>
            </Grid>

            <Grid item xs={12} align="center">
                <div class="grid-container">
                    <Button style={{ textDecoration: 'none' }} to="/map" component={Link} class="map">
                        <p class = "item1">MAP</p>
                    </Button >
                    <Button class="lists" style={{ textDecoration: 'none' }} to="/filter" component={Link}>
                        <p class = "item2">LISTS</p>
                    </Button>
                    <Button style={{ textDecoration: 'none' }} to="/graphing" component={Link} class="trends">
                        <p class = "item3">TRENDS</p>
                    </Button>  
                    <Button style={{ textDecoration: 'none' }} to="/sendData" component={Link} class="sendData">
                        <p class = "item4">SEND DATA</p>
                    </Button>
                </div> 
            </Grid>
        </Grid>
    );
  }
}