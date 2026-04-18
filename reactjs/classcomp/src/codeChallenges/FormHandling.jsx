import React from "react";
class FormInputHandle extends React.Component{
    state = {name:''}
    handler = (e) => {
        this.setState({name:e.target.value})
    }
    render(){
        return(<>
        <input type="text" onChange={this.handler} value={this.state.name} />
        <p>{this.state.name}</p>
        </>)
    }
}
export default FormInputHandle