import gql from "graphql-tag";

export const ADD_POST = gql`
  mutation($post: String!, $author: String!) {
    insert_forum(objects: [{ post: $post, author: $author }]) {
      affected_rows
    }
  }
`;

export const GET_POSTS = gql`
  {
    forum (order_by: {id: desc}) {
      id
      post
      author
    }
  }
`;
