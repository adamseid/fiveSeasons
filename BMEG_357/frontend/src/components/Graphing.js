import React, { Component } from "react";
import logo from '/static/images/tempGraph.jpg';
import { render } from "react-dom";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";


export default class Graphing extends Component {
  constructor(props) {
    super(props);
  }
  
  render() {
    return (
        <Grid container spacing={1}>
            <Grid item xs={12} align="center" class = "title">
              <h1 class = "titleText">
                Trends
              </h1>
            </Grid>
            <Grid item xs={12} align="center">
                <div class="grid-container">
                  <img class = "graphingImage" src={logo}/>
                </div> 
            </Grid>
        </Grid>
    );
  }
}