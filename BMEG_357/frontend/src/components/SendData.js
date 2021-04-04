import React, { Component } from "react";
import logo from '/static/images/tempGraph.jpg';
import { render } from "react-dom";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";

export default class SendData extends Component{
    constructor(props){
        super(props);
    }

    render() {
        return (
            <Grid container spacing={1}>
                <Grid item xs={12} align="center" class = "title">
                    <Typography component="h4" variant="h4" color = "secondary">
                        Send Data
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <div class="grid-container">
                        <form className="form">
                            <label><p>Name</p></label>
                            <input placeholder="Name"/>
                            <label><p>Email</p></label>
                            <input placeholder="Email"/>
                            <label><p>Message</p></label>
                            <textarea placeholder="Message"></textarea>
                            <button type="submit">
                                Submit
                            </button>
                        </form>
                    </div> 
                </Grid>
            </Grid>
        );
    }
}