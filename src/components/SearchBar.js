import React, { Component } from 'react'



class SearchBar extends Component {
  constructor (props) {
    super(props)
  }
  
  render () {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          What do you want to know?
          <input type="text"/>
        </label>
        <input type="submit" value="Submit" />
      </form>
    )
  }
}



export default SearchBar