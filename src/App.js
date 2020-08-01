import React, { useEffect, useState,Component } from 'react';
import './App.css';
import logo from './logo.svg';
import FilterBar from './components/FilterBar';

export class app extends Component {
  // useEffect(() => {
  //   fetch('/time').then(res => res.json()).then(data => {
  //     setCurrentTime(data.time);
  //   });
  // }, []);
  //Get Regions
  //Get Region info
  //Get Region Data/submit chosen region info
  constructor(props){
    super(props);
    this.state = {
        filterSelection:{},
        regionData:{},
        regions:[]
    };
  }


componentDidMount() {
}
componentWillUnmount() {
}
render() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      <FilterBar regions={this.getRegions}></FilterBar>
    </div>
  );
}
  
}

export default app;
