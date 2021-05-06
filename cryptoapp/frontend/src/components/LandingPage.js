import React, { Component } from 'react'
import Grid from "@material-ui/core/Grid";
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

// Landing Page with default properties. Contains 6 states which change automatically on the website
export default class LandingPage extends Component {
    constructor(props) {
        super(props);
        this.interval = null;
        this.state = {
            symbol: 0,
            id: 0,
            balance: 0,
            pv: 0,
            cv: 0,
            gains: 0,
            returns: 0,
            isLoaded:false,
        };
    }

    //Updates the internal state with the most current data from the backend every 5 seconds.
    //Param: none
    //Return: none
    componentDidMount() {
        this.interval = setInterval(()=> {
        fetch("http://127.0.0.1:8000/coin-info")
          .then(res => res.json())
          .then(
            (result) => {
              this.setState({
                symbol: result.symbol,
                id: result.id,
                balance: result.balance,
                pv: result.purchase_value,
                cv: result.current_value,
                gains: result.gains,
                returns: result.returns,
                isLoaded: true
              });
            },
            (error) => {
              this.setState({
                isLoaded: true,
                error
              });
            }
        )},5000)
    }
    
    //Clears memory of state so the website wont break. It prevents leaving errors and leaking memory
    //Param: none
    //Return: none
    componentWillUnmount() {
        clearInterval(this.interval);
    }
    
    //Renders the webstie. The page is broken up into grids. The first grid contains the title.
    //The second grid contains a table where the internal states are placed (symbol, id, balance, pv, cv, gains, returns)
    render() {
        const classes = makeStyles({
            table: {
              minWidth: 650,
            },
        });
        return (
            <Grid container spacing={1}>
                <Grid item xs={12} align="center" className = "title">
                    <h1 className = "titleText">
                        Five Seasons Fund
                    </h1>                    
                </Grid>
                <Grid item xs={12} align="center">
                    <TableContainer component={Paper}>
                        <Table className={classes.table} aria-label="simple table">
                            <TableHead>
                                <TableRow>
                                    <TableCell>Symbol</TableCell>
                                    <TableCell align="right">ID</TableCell>
                                    <TableCell align="right">Balance</TableCell>
                                    <TableCell align="right">PV</TableCell>
                                    <TableCell align="right">CV</TableCell>
                                    <TableCell align="right">gains</TableCell>
                                    <TableCell align="right">returns</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                <TableRow key={this.state.symbol}>
                                        <TableCell component="th" scope="row">{this.state.symbol}</TableCell>
                                        <TableCell align="right">{this.state.id}</TableCell>
                                        <TableCell align="right">{this.state.balance}</TableCell>
                                        <TableCell align="right">{this.state.pv}</TableCell>
                                        <TableCell align="right">{this.state.cv}</TableCell>
                                        <TableCell align="right">{this.state.gains}</TableCell>
                                        <TableCell align="right">{this.state.returns}</TableCell>
                                </TableRow>
                            </TableBody>
                        </Table>
                    </TableContainer>
                </Grid>
            </Grid>
        );
    }
}
