import React, {useState, useEffect} from 'react';
import axios from 'axios';
import Coin from './coin';

function MainPage() {

    const [coins, setCoins] = useState([]);
    const [search, setSearch] = useState('')

    useEffect(() => {
        axios.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false')
        .then(res => {
            setCoins(res.data);
            console.log(res.data);
        })
    });

    const handleChange = e => {
        setSearch(e.target.value)
    }

    const filteredCoins = coins.filter(coin =>
        coin.name.toLowerCase().includes(search.toLowerCase())
        )

    return (
        <div>
            <div>main page</div>

            <div>
                <h1>Search</h1>
                <form>
                    <input type='text' placeholder='Search'/>
                </form>
            </div>
            {filteredCoins.map(coin => {
                return(
                    <Coin 
                        key = {coin.id}
                        name = {coin.name}
                        image = {coin.image}
                        symbols = {coin.symbol}
                        volume = {coin.market_cap}
                        price = {coin.current_price}
                    />
                )
            })}
        </div>
    )
}

export default MainPage;