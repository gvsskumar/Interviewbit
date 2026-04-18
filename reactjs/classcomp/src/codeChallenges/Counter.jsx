import React from "react";
class Counter extends React.Component{
    constructor(props){
        super(props)
        this.state = {count:0}
    }
    componentDidMount(){
        console.log('mount')
    }
    componentDidUpdate(){
        console.log('update')
    }
    componentWillUnmount(){
        console.log('unmount')
    }
    increment = () =>{
        this.setState((prev)=>({count:prev.count+1}))
    }
    render(){
        return(<div>
            <h2>{this.state.count}</h2>
            <button onClick={this.increment}>Increment</button>
        </div>)
    }
}
export default Counter