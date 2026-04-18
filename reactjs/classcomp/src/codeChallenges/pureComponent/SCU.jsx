import React from "react";
class Child extends React.Component {
  shouldComponentUpdate(nextProps) {
    return nextProps.users !== this.props.users;
  }

  render() {
    console.log("UserList Render (SCU)");
    return (
      <ul>
        {this.props.users.map(u => <li key={u}>{u}</li>)}
      </ul>
    );
  }
}
export default Child;