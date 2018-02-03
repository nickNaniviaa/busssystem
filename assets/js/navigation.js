import PropTypes from 'prop-types';
import React, { Component } from 'react'

import styles2 from '../../static/styles/underground_lines.css';

export default class Navigation extends Component {
    render() {
        return (
            <div className="header">
                <h1 id="title-line">Guadalajara</h1>
                <div className="floatinglist-stations">
                    <p className="nextstop1">Av.Londres</p>
                    <p className="nextstop2">R. Estonia</p>
                    <p className="nextstop3">Av. Lituaniaaaaaa</p>
                    <p className="nextstop4">..........</p>
                    <p className="nextstop5">T.S.A.</p>
                </div>
                <div className="container">
                    <div className="rectangle"></div>
                    <div className="ball1"></div>
                    <div className="ball2"></div>
                    <div className="ball3"></div>
                    <div className="ball4"></div>
                    <div className="ball5"></div>
                </div>

            </div>
        )
    }
}

/*
                <ul className="list-stations">
                    <li>Av. Londres</li>
                    <li>Rua Estônia</li>
                    <li>...</li>
                    <li>Terminal Santo Antônio</li>
                </ul>
                */