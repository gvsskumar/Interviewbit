import React from "react";
class UserList extends React.Component{
    state = {users:[],loading:true}

    controller = new AbortController()

    componentDidMount(){
        fetch('https://jsonplaceholder.typicode.com/users',{signal:this.controller.signal})
        .then(res=>res.json())
        .then(data=>{this.setState({users:data,loading:false})})
        .catch(err=>{
            if(err.name!=='AbortError')console.error(err)
        })
    }
    componentWillUnmount(){
    //    this.controller.abort()
    }
    render(){
        if(this.state.loading)return(<p>Loading......</p>)
        return(<ul>
            {this.state.users.map(user=>(<li key={user.id}>{user.name}</li>))}
        </ul>)
    }
}
export default UserList