import React, { Component } from 'react';

export class MainFilter extends Component {
    constructor(props) {
        super(props);
        this.state = {
            value: ""
        };
    }
    componentDidMount() {
    }
    componentWillUnmount() {
    }
    handleChange(event) {
        this.setState({ value: event.target.value });
        this.props.changeFunc(event.target.value);
        this.props.setSelection(event.target.name, event.target.value);
    }
    render() {
        var regionSelection;
        if (this.props.regions) {
            regionSelection = this.props.regions.map((region) => {
                return (<option key={region} value={region}>{region}</option>);
            });
        }

        return (
            <label className="MainFilter">
                <span class="filterName">Choose The Region:</span>
                <span>
                    <select name="name" value={this.state.value} onChange={this.handleChange.bind(this)}>
                        <option value=""></option>
                        {regionSelection}
                    </select>
                </span>
            </label>
        )
    }
}


export default MainFilter
