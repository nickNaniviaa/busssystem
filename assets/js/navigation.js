import PropTypes from 'prop-types';
import React, { Component } from 'react'
import $ from 'jquery';

export default class Navigation extends Component {
    render() {
        var length = 0;
        var length = this.props.data.length;

        if (length > 0 ){
            var lista_array = this.props.data;
            var station_name_elements = [];
            var station_time_elements = [];
            var station_dots_elements = [];

            var number_iterations = length > 5 ? 5 : length
           
            for(var i = number_iterations; i > 0; i--){
                var name_stop = "nextstop"+(i);
                var time_stop = "timestop"+(i);
                if (i == number_iterations){
                    var dot = "ball"+(5);
                    
                    station_name_elements.push(<p className={name_stop} key={i}>{lista_array[length-1].bus_stop_name}</p>);
                    station_time_elements.push(<p className={time_stop} key={i}>{lista_array[length-1].real_time_arrival}</p>);
                    station_dots_elements.push(<div className={dot} key={i}></div>);
                }
                else{
                    var dot = "ball"+(i);
                    
                    station_name_elements.push(<p className={name_stop} key={i}>{lista_array[i-1].bus_stop_name}</p>);
                    station_time_elements.push(<p className={time_stop} key={i}>{lista_array[i-1].real_time_arrival}</p>);
                    station_dots_elements.push(<div className={dot} key={i}></div>);
                }
            }
        }

        var className

        return (
            <div className="header">
                <h1 id="title-line">Guadalajara</h1>
                <div className="floatinglist-stations">
                    {station_name_elements}
                </div>
                <div className="floatinglist-time">
                    {station_time_elements}
                </div>

                <div className="container">
                    <div className="rectangle"></div>
                    {station_dots_elements}
                </div>

            </div>
        )
    }
}


Navigation.PropTypes = {
    data: PropTypes.array
}
