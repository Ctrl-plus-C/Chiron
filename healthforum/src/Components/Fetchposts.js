import React, { Component } from "react";

import { Query } from "react-apollo";
import { GET_POSTS } from "../Queries";
import { Panel, Grid, Col, Row } from "react-bootstrap";

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
              <Grid>
                <Row>
                  <Col mdPush={2} md={8}>
                    {data.forum.map((post,index) => (
                      <Panel>
                        <Panel.Heading>
                          <Panel.Title componentClass="h3">
                            {index} {post.author}
                          </Panel.Title>
                        </Panel.Heading>
                        <Panel.Body>{post.post}</Panel.Body>
                      </Panel>
                    ))}
                  </Col>
                </Row>
              </Grid>
            </div>
          );
        }}
      </Query>
    );
  }
}

export default Fetchposts;
