import React, { Component } from "react";
import "./App.css";
import Navbarhealth from "./Components/Navbarhealth";
import Createpost from "./Components/Createpost";
import Fetchposts from "./Components/Fetchposts";
import Auth from "./Components/Auth";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Navbarhealth/>
        <Createpost/>
        <hr/>
        <Fetchposts/>
      </div>
    );
  }
}

export default App;
