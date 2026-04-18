import React from "react";
class Search extends React.Component{
    state = {inputValue: "",queryTxt:""}
    timeout = null
    handler = (e) =>{
        const value = e.target.value;
        
         // ✅ Update UI immediately
         this.setState({inputValue:value})
        // ✅ Debounce actual query
        clearTimeout(this.timeout)

        this.timeout = setTimeout(()=>{
            this.setState({queryTxt:value})

        },500)
    }
    componentWillUnmount(){
        clearTimeout(this.timeout)
    }
    render(){
        return(<>
        <input type="text" onChange={this.handler} value={this.state.inputValue} />
        <p>Typing: {this.state.inputValue}</p>
        <p>Debounced: {this.state.queryTxt}</p>
        </>)
    }
}
export default Search
