import React, {Component} from 'react';
import './App.css';
import logo from './logo.svg';
import FilterBar from './components/FilterBar';
import FilteredTable from './components/FilteredTable';
/*this app does a thing*/
export class app extends Component {
  constructor(props) { 
    super(props);
    this.state = {
      returnedData: {},
    };
  }

  updateFilteredData(newData) {
    this.setState({
      returnedData: newData,
    });
  }
  componentDidMount() {
  }
  componentWillUnmount() {
  }
  render() {
    let filteredTables;
    if (this.state.returnedData && 'filteredData' in this.state.returnedData) {
      filteredTables =Object.keys(this.state.returnedData.filteredData).map((col)=>{
        return (<FilteredTable  key={col} rows={this.state.returnedData.filteredData[col]} name={col}>

        </FilteredTable>);
      });
    }

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
        </header>
        <div id="bodyArea">
          {filteredTables}
        </div>
        <div id="filterArea">
          <FilterBar setFilteredData={this.updateFilteredData.bind(this)}></FilterBar>
        </div>

      </div>
    );
  }
}

export default app;
