import PropTypes from 'prop-types';
import React, { Component } from 'react'
import $ from 'jquery';


import ClockFunction from './clock'
import Navigation from './navigation'

import styles2 from '../../static/styles/underground_lines.css';

export default class BoxNavigation extends Component {
    constructor(props){
    super(props);
    this.state = { list: [] };
    this.fetchAJAXdata = this.fetchAJAXdata.bind(this);
}

componentWillMount() {
    this.fetchAJAXdata();
}

componentWillReceiveProps() {
    this.fetchAJAXdata();
}

fetchAJAXdata() {
    $.ajax({
        url: "http://localhost:8000/businfo/buslist",
        datatype: 'json',
        cache: false,
        success: function (fetchedData) {
            this.setState({ list: fetchedData })
        }.bind(this)
    })
}
    render() {
        return (
        <div>
            <Navigation data={this.state.list}></Navigation>
            <ClockFunction></ClockFunction>
        </div>
        )
    }
}
