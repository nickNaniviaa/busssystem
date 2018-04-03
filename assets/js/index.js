import PropTypes from 'prop-types';
import ReactDOM from "react-dom";
import React, { Component } from 'react';

import Navigation from './navigation';
import ImageRotator from './imagerotator'

import styles from '../../static/styles/base.css';


class Index extends Component {
    render() {
        return (<div>
                <Navigation></Navigation>
                <ImageRotator></ImageRotator>
            </div>
        )
    }
}

ReactDOM.render(<Index />, document.getElementById('react_render'));
