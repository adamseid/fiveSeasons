import React, { Component } from "react";
import { render } from "react-dom";
import LandingPage from "./LandingPage";
import MainPage from "./MainPage"
import test from "./test"
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from "react-router-dom";



export default class App extends Component {
    constructor(props){
        super(props);

    }

    render(){
        return <Router>
            <Switch>
                <Route path='/landingpage' component={LandingPage}/>
                <Route path='/mainpage' component={MainPage}/>
                <Route path='/test' component={test}/>
            </Switch>

        </Router>;
    }

}

const appDiv = document.getElementById("app");
render(<App/>, appDiv);
