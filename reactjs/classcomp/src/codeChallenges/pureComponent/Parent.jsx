import React from "react";
// import Child from './Child'
import Child from "./SCU";
class Parent extends React.Component{
    state = {count:0}
    userList = ["Surya","Venkata","Satya","Kumar"]
    componentDidMount(){
        setInterval(()=>{
            this.setState(prev=>({count:prev.count+1}))
        },1000)
    }
    render(){
        console.log('render Parent Component')
        return(<div>
            <h1>Count: {this.state.count}</h1>
            <Child users={this.userList} />
        </div>)
    }
}
export default Parent