import React, { Component } from 'react';

class Product extends Component {

    constructor(props) {
        super(props);
        let max_products = 12;
        let product_amount = localStorage.getItem(props.productId);
        this.state = {
            product_amount,
            max_products
        }

        this.props.totalProductPrice(360.00 * product_amount);
    }

    increaseItemCount() {
        this.setState((prev_state, { product_amount }) => ({
            product_amount: parseInt(prev_state.product_amount) >= this.state.max_products ? this.state.max_products : parseInt(prev_state.product_amount) + 1
        }));
        if (this.state.product_amount <= this.state.max_products) {
            this.props.totalProductPrice(360.00);
        }

    };

    decreaseItemCount() {
        this.setState((prev_state, { product_amount }) => ({
            product_amount: parseInt(prev_state.product_amount) <= 1 ? 1 : parseInt(prev_state.product_amount) - 1
        }));

        this.props.totalProductPrice((-1) * 360.00);
    };



    render() {
        return (
            <tr key={this.props.productId}>
                <td>
                    <div className="media">
                        <div className="d-flex">
                            <img src="localhost:1337/static/img/organic-food/b4.png" alt="" />
                        </div>
                        <div className="media-body">
                            <p>{this.props.productId}</p>
                        </div>
                    </div>
                </td>
                <td>
                    <h5>$360.00</h5>
                </td>
                <td>
                    <div className="product_count">
                        <input type="text" name="qty" id="sst" maxLength="12" value={this.state.product_amount} title="Quantity:"
                            className="input-text qty" />
                        <button onClick={this.increaseItemCount.bind(this)}
                            className="increase items-count" type="button"><i className="lnr lnr-chevron-up"></i></button>
                        <button onClick={this.decreaseItemCount.bind(this)}
                            className="reduced items-count" type="button"><i className="lnr lnr-chevron-down"></i></button>
                    </div>
                </td>
                <td>
                    <h5>${360.00 * this.state.product_amount}</h5>
                </td>
            </tr>
        )
    }
}

export default Product;