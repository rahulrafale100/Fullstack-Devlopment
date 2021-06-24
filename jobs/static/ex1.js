'use strict';

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };  //JSON(javascript object notation)
  }

  render() {
    if (this.state.liked) {
        return React.createElement(
            'button',
            { onClick: () => this.setState({ liked: false  }) },
            'Unlike'
        )
    }
    else{
      return React.createElement(
          'button',
          { onClick: () => this.setState({ liked: true }) },
          'Like'
      );}
  }
}

const rdemo = document.querySelector("#rdemo");   // Indicating the field where to do this
ReactDOM.render(React.createElement(LikeButton), rdemo);  // What to do there