import React from "react";
class Child extends React.PureComponent{
    render(){
        console.log('render Child Component')
        return(<ul>
            {this.props.users.map((el,index)=>(<li key={index}>{el}</li>))}
        </ul>)
    }
}
export default Child