import React from 'react'

const Coin = ({ name, image, symbol, price, volume }) => {
    return (
        <div>
            <div>
                <div>
                    <img src={image} alt='crypto' />
                    <h1>{name}</h1>
                    <p>{symbol}</p>
                </div>
                <div>
                    <p>${price}</p>
                    <p>${volume.toLocaleString()}</p>
                </div>
            </div>
        </div>
    )
}

export default Coin
