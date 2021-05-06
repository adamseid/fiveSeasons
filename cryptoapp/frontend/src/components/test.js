import React, {useState, useEffect} from 'react';
import axios from 'axios';
import Coin from './coin';

function Test() {

    const [coins, setCoins] = useState([]);


    useEffect(() => {
        axios.get('http://localhost:8000/get-response')
        .then(res => {
            setCoins(res.data);
        })
    });


    return (
        <div>
            <div>test:</div>
            <div>{coins.response}</div>
        </div>
    )
}

export default Test;