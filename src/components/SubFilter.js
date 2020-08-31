import React, { Component } from 'react';
import Nouislider from "nouislider-react";
import "nouislider/distribute/nouislider.css";

export class SubFilter extends Component {
    constructor(props) {
        super(props);
        this.state = {
            name: this.props.name,
            leftValue: this.props.min,
            rightValue: this.props.max,
            visible: true
        };
        //this.handleChange=this.handleChange.bind(this);
    }
    onChangeSlide(data) {
        //console.log(data);
        this.setState({
            leftValue: data[0],
            rightValue: data[1]
        });
        this.props.setSelection(this.state.name, { Min: data[0], Max: data[1] });
    }
    onclick() {
        this.setState({
            visible: !this.state.visible
        });

        this.props.setSelection(this.state.name, this.state.visible ? { Min: this.state.leftValue, Max: this.state.rightValue } : "");
    }
    componentDidMount() {
        // this.setState({
        //     leftValue:this.props.min,
        //     rightValue:this.props.max
        // });
    }
    componentWillUnmount() {
    }
    render() {
        return (
            <div className="SubFilter">
                <input type="checkbox" checked={this.state.visible} onChange={this.onclick.bind(this)} />
                <label className="filterName">
                    {this.props.name + ": "}
                </label>
                {this.state.visible &&
                    <Nouislider
                        start={[this.state.leftValue, this.state.rightValue]}
                        step={1}
                        connect={true}
                        tooltips={[true, true]}
                        key={this.props.name}
                        range={{
                            min: this.props.min,
                            max: this.props.max
                        }}
                        onSlide={this.onChangeSlide.bind(this)}
                    />
                }

            </div>
        )
    }
}

export default SubFilter;
