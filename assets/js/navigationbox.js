import PropTypes from 'prop-types';
import React, { Component } from 'react';
import $ from 'jquery';

import ClockFunction from './clock';
import Navigation from './navigation';

import styles2 from '../../static/styles/underground_lines.css';

var intervalTime = 2;

export default class BoxNavigation extends Component {
    constructor(props){
    super(props);
    this.state = { list: [], accumulator: 0, currentCount: intervalTime, intervalID: 0 };
    this.fetchAJAXdata = this.fetchAJAXdata.bind(this);
    this.fetchAJAXupdate = this.fetchAJAXupdate.bind(this);
    
    this.timer = this.timer.bind(this);

    }

    componentWillMount() {
        this.fetchAJAXdata();
    }

    componentWillReceiveProps() {
        this.fetchAJAXdata();
    }

    componentDidMount() {
        var intervalId = setInterval(this.timer, 1000);
        this.setState({ intervalId: intervalId});
    }

    componentWillUnmount() {
        clearInterval(this.state.intervalId)
    }

    fetchAJAXdata() {
        $.ajax({
            url: "http://localhost:8000/businfo/buslist",
            datatype: 'json',
            cache: false,
            success: function (fetchedData) {
                console.log("Atualizou os Dados");
                this.setState({ list: fetchedData })
            }.bind(this)
        })
    }

    fetchAJAXupdate() {
        $.ajax({
            url: "http://localhost:8000/businfo/bus",
            datatype: 'json',
            cache: false,
            success: function (fetchedData) {
                var accumulator = fetchedData[0].accumulator
                console.log(accumulator)

                if (this.state.accumulator != accumulator){
                    console.log("Update Accumulator");
                    this.fetchAJAXdata();
                    this.setState({ accumulator : accumulator });
                }
            }.bind(this)
        })
    }

    timer(){
        var newCount = this.state.currentCount - 1;
        if (newCount>=0){
            this.setState({currentCount:newCount});
            this.fetchAJAXupdate();       
        }
        else{            
            this.setState({ currentCount: intervalTime});
        }
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
