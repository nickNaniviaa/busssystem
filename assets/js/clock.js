import React, { Component } from 'react';


export default class ClockFunction extends Component {

    constructor() {
        super();
        this.state = { time: new Date() }; // initialise the state
    }

    componentDidMount() { // create the interval once component is mounted
        this.update = setInterval(() => {
            this.setState({ time: new Date() });
        }, 1 * 1000); // every 1 seconds
    }

    componentWillUnmount() { // delete the interval just before component is removed
        clearInterval(this.update);
    }

    render() {
        const { time } = this.state; // retrieve the time from state
        var hour = time.getHours();
        var minute = time.getMinutes();
        if (hour < 10){
            hour = "0"+ hour;
        }
        if (minute < 10){
            minute = "0"+ minute;
        }

        return (<div>
            <h2 className="clock">
                {/* print the string prettily */}
                {hour+":"+minute}
            </h2>
        </div>);
    }
}