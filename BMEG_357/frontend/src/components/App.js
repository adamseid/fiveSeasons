import React, {Component} from 'react';
import { render } from "react-dom";
import LandingPage from "./LandingPage";
import Filter from "./Filter";
import Graphing from "./Graphing";
import SendData from "./SendData";
import Map from "./Map";
import {
    BrowserRouter as Router, 
    Switch, 
    Route, 
    Link, 
    Redirect
} from "react-router-dom";


export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
        <Router>
            <Switch>
                <Route exact path='/' component={LandingPage}></Route>
                <Route path='/filter' component={Filter}></Route>
                <Route path='/graphing' component={Graphing}></Route>
                <Route path='/sendData' component={SendData}></Route>
                <Route path='/map' component={Map}></Route>
            </Switch>
        </Router>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
