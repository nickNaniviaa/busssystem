import PropTypes from 'prop-types';
import ReactDOM from "react-dom";
import React, { Component } from 'react';

import NavigationBox from './navigationbox';
import ImageRotator from './imagerotator'

import styles from '../../static/styles/base.css';


class Index extends Component {
    render() {
        return (<div>
                <NavigationBox></NavigationBox>
                <ImageRotator></ImageRotator>
            </div>
        )
    }
}

ReactDOM.render(<Index />, document.getElementById('react_render'));
