import PropTypes from 'prop-types';
import React, { Component } from 'react';

import styles2 from '../../static/styles/imagens.css';

import cafeImg from '../../static/cafe_simple.png';
import produtoMaquiagem from '../../static/produtos_maquiagem.png';
import vistaSuperior from '../../static/vista_superior.jpg';
import queensPoker from '../../static/queens_poker.png';


var imagesName = [cafeImg,
                  produtoMaquiagem,
                  vistaSuperior,
                  queensPoker,
                ];

var intervalTime = 10;

export default class ImageRotator extends Component {
    constructor(props){
        super(props)
        this.state = {index_value: 0, currentCount: intervalTime, intervalId: 0}
        this.timer = this.timer.bind(this);
    }


    componentDidMount() {
        var intervalId = setInterval(this.timer, 1000);
        this.setState({ intervalId: intervalId});
    }

    componentWillUnmount() {
        clearInterval(this.state.intervalId)
    }

    timer(){
        var newCount = this.state.currentCount - 1;
        if (newCount>=0){
            this.setState({currentCount:newCount});       
        }
        else{            
            this.setState({ currentCount: intervalTime});
            if (this.state.index_value == 3){
                this.setState({index_value:0})
            }
            else{
                this.setState({index_value: this.state.index_value+1})
            }
        }
    }

    render() {
        return (<div>
                <img className="imagem-propaganda" src={ imagesName[this.state.index_value] } type="image"/>
            </div>
        )
    }
}

