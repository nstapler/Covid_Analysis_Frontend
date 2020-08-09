import React, {Component } from 'react';
import './App.css';
import logo from './logo.svg';
import FilterBar from './components/FilterBar';

export class app extends Component {

  constructor(props) {
    super(props);
    this.state = {
      filterSelection: {},
      regionData: {},
      regions: []
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
