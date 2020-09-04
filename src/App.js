import React, { Component } from 'react';
import './App.css';
import logo from './logo.svg';
import FilterBar from './components/FilterBar';
import { FilteredTable, Styles } from './components/FilteredTable';
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
    let filteredTables, filteredTablesHeader;
    if (this.state.returnedData && 'filteredData' in this.state.returnedData) {
      filteredTables = Object.keys(this.state.returnedData.filteredData).map((col) => {
        return (<FilteredTable key={col} rows={this.state.returnedData.filteredData[col]} name={col}>

        </FilteredTable>);
      });
      filteredTablesHeader = (<Styles>
        <table>
          <th>
            Region: {this.state.returnedData.filters.name}
          </th>
        </table>
      </Styles>)
    }

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
        </header>
        <div id="displayHeader">
              {filteredTablesHeader}
          </div>
        <div id="displayArea">
          <div id="displayBody">
            {filteredTables}
          </div>
        </div>
        <div id="filterArea">
          <FilterBar setFilteredData={this.updateFilteredData.bind(this)}></FilterBar>
        </div>

      </div>
    );
  }
}

export default app;
