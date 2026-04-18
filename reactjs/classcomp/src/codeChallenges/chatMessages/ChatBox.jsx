import React from "react";
class ChatBox extends React.Component {
  listRef = React.createRef();

  getSnapshotBeforeUpdate(prevProps) {
    // If new messages are added
    if (prevProps.messages.length < this.props.messages.length) {
      const list = this.listRef.current;

      // Capture scroll position BEFORE update
      return list.scrollHeight - list.scrollTop;
    }
    return null;
  }

  componentDidUpdate(prevProps, prevState, snapshot) {
    if (snapshot !== null) {
      const list = this.listRef.current;

      // Restore scroll AFTER update
      list.scrollTop = list.scrollHeight - snapshot;
    }
  }

  render() {
    return (
      <div ref={this.listRef} style={{ height: "200px", overflow: "auto" }}>
        {this.props.messages.map((msg, i) => (
          <div key={i}>{msg}</div>
        ))}
      </div>
    );
  }
}
export default ChatBox