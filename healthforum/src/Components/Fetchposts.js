import React, { Component } from "react";

import { Query } from "react-apollo";
import { GET_POSTS } from "../Queries";

class Fetchposts extends Component {
  constructor(props) {
    super(props);
    this.state = {
      postdata: ""
    };
  }
  render() {
    return (
        <Query query={GET_POSTS}>
        {({ loading, error, data }) => {
          if (loading) return "Loading...";
          if (error) return `Error! ${error.message}`;
    
          return (
              <div className="Fetchposts">
              {data.forum.map(post => (
                <h3 key={post.id} value={post.post}>
                  {post.post}
                </h3>
              ))}
              </div>
          );
        }}
      </Query>
    );
  }
}

export default Fetchposts;
