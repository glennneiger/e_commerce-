import React, { Component } from 'react';
import API from '../actions/API';

class Product extends Component {

    constructor(props) {
        super(props);
        let max_products = 12;
        let product_amount = parseInt(localStorage.getItem(props.productId));
        this.state = {
            product_amount,
            max_products,
            product_data: { attributes: { price: 0., title: "" } },
            product_price: 0.0
        }
        this.props.totalProductPrice(this.state.product_price * product_amount);
    }

    increaseItemCount() {
        this.setState((prev_state, { product_amount }) => ({
            product_amount: parseInt(prev_state.product_amount) >= this.state.max_products ? this.state.max_products : parseInt(prev_state.product_amount) + 1
        }));
        if (this.state.product_amount < this.state.max_products) {

            this.props.totalProductPrice(this.state.product_price);
        }

    };

    decreaseItemCount() {
        this.setState((prev_state, { product_amount }) => ({
            product_amount: parseInt(prev_state.product_amount) <= 1 ? 1 : parseInt(prev_state.product_amount) - 1
        }));
        if (this.state.product_amount > 1) {

            this.props.totalProductPrice((-1) * this.state.product_price);
        }

    };

    componentDidMount() {
        API.get(`products/${this.props.productId}`)
            .then(res => {
                const product_data = res.data.data
                this.setState({ product_data: product_data, product_price: parseFloat(product_data.attributes.price) })
                this.props.totalProductPrice(this.state.product_price * this.state.product_amount);
            })

    }

    render() {
        return (
            <tr key={this.props.productId}>
                <td>
                    <div className="media">
                        <div className="d-flex">
                            <img src="localhost:1337/static/img/organic-food/b4.png" alt="" />
                        </div>
                        <div className="media-body">
                            <p>{this.state.product_data.attributes.title}</p>
                        </div>
                    </div>
                </td>
                <td>
                    <h5>${this.state.product_price}</h5>
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
                    <h5>${(this.state.product_price * this.state.product_amount).toFixed(2)}</h5>
                </td>
            </tr>
        )
    }
}

export default Product;