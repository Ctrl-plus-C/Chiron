import React, { Component } from "react";
import {
  FormControl,
  FormGroup,
  Grid,
  Row,
  Col,
  Button
} from "react-bootstrap";

import { Mutation } from "react-apollo";
import { ADD_POST } from "../Queries";

class Createpost extends Component {
  constructor(props) {
    super(props);
    this.state = {
      postdata: ""
    };
  }
  render() {
    return (
      <Mutation mutation={ADD_POST}>
        {(insert_forum, { data }) => (
          <div className="Createpost">
            <Grid>
              <form
                onSubmit={e => {
                  e.preventDefault();
                  insert_forum({
                    variables: { post: this.state.postdata, author: "anupam" }
                  });
                  console.log("executed");
                }}
              >
                <Row className="show-grid">
                  <Col xs={12} md={12}>
                    <FormGroup bsSize="large">
                      <FormControl
                        onChange={e =>
                          this.setState({ postdata: e.target.value })
                        }
                        type="text"
                        placeholder="Create a post"
                      />
                    </FormGroup>
                  </Col>
                  <Col xs={12} md={3} mdPush={10}>
                    <Button type="Submit" bsStyle="primary" bsSize="large">
                      Post
                    </Button>
                  </Col>
                </Row>
              </form>
            </Grid>
          </div>
        )}
      </Mutation>
    );
  }
}

export default Createpost;
