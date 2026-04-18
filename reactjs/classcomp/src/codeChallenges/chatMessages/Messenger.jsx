import React from "react";
import ChatBox from "./ChatBox";

class Messenger extends React.Component {
  state = {
    messages: ["Hello", "Hi"],
    inputText: ""
  };

  typedText = (e) =>{
    this.setState({ inputText: e.target.value });
  }

  addMessage = () => {
     if (!this.state.inputText.trim()) return; 
    this.setState(prev => ({
      messages: [...prev.messages, this.state.inputText],
      inputText: ""
    }));
  };

  render() {
    return (
      <div>
        <input type="text" onChange={this.typedText} value={this.state.inputText} />
        <button onClick={this.addMessage}>Add</button>
        <ChatBox messages={this.state.messages} />
      </div>
    );
  }
}

export default Messenger;