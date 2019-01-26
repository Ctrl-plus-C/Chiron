import React, { Component } from "react";

class Auth extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      password: ""
    };

    this.loginUser = this.loginUser.bind(this);
  }

  loginUser(e) {
    e.preventDefault();
    fetch("http://127.0.0.1:8000/api/login", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username: this.state.username,
        password: this.state.password
      })
    })
    .then(res => res.json())
    .then(resdata => localStorage.setItem('authToken', resdata.token));
    console.log(localStorage.getItem('authToken'));
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
