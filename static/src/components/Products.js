import React, { Component } from 'react';
import Product from './Product';

class Products extends Component {
    constructor(props) {
        super(props);
        this.state = {
            products: Object.keys(localStorage),
            total_sum: 0.0
        }
        this.updateSubtotal = this.updateSubtotal.bind(this)
    }

    updateSubtotal(productSum) {
        this.setState((prevState) => ({
            total_sum: prevState.total_sum + productSum
        }));
    }

    componentDidMount() {
        let products = Object.keys(localStorage);
        this.state = {
            ...this.state,
            products: products
        };
    }

    render() {
        return (
            <>
                {this.state.products.map(product => <Product productId={product} key={product} totalProductPrice={this.updateSubtotal.bind(this)} />)}
                <tr className="bottom_button">
                    <td>
                        <a className="gray_btn" href="#">Update Cart</a>
                    </td>
                    <td>

                    </td>
                    <td>

                    </td>
                    <td>
                        <div className="cupon_text d-flex align-items-center">
                            <input type="text" placeholder="Coupon Code" />
                            <a className="primary-btn" href="#">Apply</a>
                            <a className="gray_btn" href="#">Close Coupon</a>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>

                    </td>
                    <td>

                    </td>
                    <td>
                        <h5>Subtotal</h5>
                    </td>
                    <td>
                        <h5>${this.state.total_sum.toFixed(2)}</h5>
                    </td>
                </tr>
            </>
        )
    }
}

export default Products;