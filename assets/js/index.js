import PropTypes from 'prop-types';
import ReactDOM from "react-dom";
import React, { Component } from 'react'

import Navigation from './navigation'
//import Carousel from './carousel'

/*import { HashRouter, Router, Route, Switch, Link } from 'react-router-dom'
import Home from './home'
import Charts from './charts'
import About from './about'
*/

//import styles1 from '../../static/styles/reset.css';
import styles from '../../static/styles/base.css';
//import styles1 from '../../static/styles/pure.css'


//<Carousel></Carousel>

class Index extends Component {
    render() {
        return (<div>
                <Navigation></Navigation>
            </div>
        )
    }
}

ReactDOM.render(<Index />, document.getElementById('container'));
