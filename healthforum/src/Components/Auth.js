import React, { Component } from "react";

class Auth extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      password: ""
    };
  }

  render() {
    return (
      <div className="Login">
      <form>
          <input type="text" onChange={e => this.setState({username: e.target.value})} placeholder="username"/>
          <input type="password" onChange={e => this.setState({password: e.target.value})} placeholder="password" />
          <button onClick={this.loginUser}>Login</button>
      </form>
      </div>
    );
  }
}

export default Auth;
