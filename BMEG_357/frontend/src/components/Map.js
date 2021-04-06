import React, { Component } from "react";
import firstFloor from '/static/images/1.png';
import secondFloor from '/static/images/2.png';
import thirdFloor from '/static/images/3.png';
import fourthFloor from '/static/images/4.png';
import fifthFloor from '/static/images/5.png';
import sixFloor from '/static/images/6.png';
import sevenFloor from '/static/images/7.png';
import eightFloor from '/static/images/8.png';

import { render } from "react-dom";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";


export default class Map extends Component{
    constructor(props){
        super(props);
        const floor1 = firstFloor;
        const floor2 = secondFloor;
        const floor3 = thirdFloor;
        const floor4 = fourthFloor;
        const floor5 = fifthFloor;
        const floor6 = sixFloor;
        const floor7 = sevenFloor;
        const floor8 = eightFloor;
        this.state = {
            index: 0,
            images: [floor1,floor2,floor3,floor4,floor5,floor6,floor7,floor8]
        }
    }

    render(){
        return (
            <Grid container spacing={1} direction = "column">
                <Grid item xs={12}>
                </Grid>
                <Grid item xs={12} align="center">
                  <h1 class = "titleText">
                    Map
                  </h1>
                </Grid>
                <Grid item xs={12} align="flex-start" container spacing ={1}>
                    <Grid item xs={10} align="flex-start" class = "maptitle">
                        <br /> <br />
                        <br /> <br />
                        <img class = "mapImage" src={this.state.images[this.state.index]}/>   
                    </Grid>
                    <Grid item xs={2} class = "maptitle" align="flex-start">
                        <p class = "legend">Legend</p>
                        <p class = "legendBody">
                            △ Model 1<br /> <br />
                        </p>
                        <p class = "legendBody">
                            ◻ Model 2<br /> <br />
                        </p>
                        <p class = "legendBody">
                            🔴 In Use <br /> <br />
                        </p>    
                        <p class = "legendBody">
                            🟢 Available<br /> <br />
                        </p>
                        <p class = "legendBody">
                            🟡 Out of Battery<br />
                        </p>
                    </Grid>
                </Grid>
                <Grid item xs={12} align="center" container spacing ={2} direction = "row">
                    <Grid item xs={2} align="center">
                    </Grid>
                    <Grid item xs={1}>
                        <Button variant="outlined" onClick={() =>  this.setState({index:0})}>
                            Floor 1
                        </Button >
                    </Grid>
                    <Grid item xs={1}>
                        <Button variant="outlined" onClick={() =>  this.setState({index:1})}>
                            Floor 2
                        </Button >
                    </Grid>
                    <Grid item xs={1} >
                        <Button variant="outlined" onClick={() =>  this.setState({index:2})}>
                            Floor 3
                        </Button >  
                    </Grid>
                    <Grid item xs={1}>
                        <Button variant="outlined" onClick={() =>  this.setState({index:3})}>
                            Floor 4
                        </Button >
                    </Grid>
                    <Grid item xs={1}>
                        <Button variant="outlined" onClick={() =>  this.setState({index:4})}>
                            Floor 5
                        </Button >   
                    </Grid>
                    <Grid item xs={1}>
                        <Button variant="outlined" onClick={() =>  this.setState({index:5})}>
                            Floor 6
                        </Button >
                    </Grid>
                    <Grid item xs={1}>
                        <Button variant="outlined" onClick={() =>  this.setState({index:6})}>
                            Floor 7
                        </Button >  
                    </Grid>
                    <Grid item xs={1}>
                        <Button variant="outlined" onClick={() =>  this.setState({index:7})}>
                            Floor 8
                        </Button >
                    </Grid>
                </Grid>
            </Grid>
        );
    }
}