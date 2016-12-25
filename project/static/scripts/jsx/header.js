var Header = React.createClass({
  
  render: function() {

    return (
    <div className="header-elements">
        <div className="logo"><a href="/">Habitz</a></div>
        <div className="sign-up"><a href="/signup">Sign up</a></div>
        <div className="log-in"><a href="/login">Log in</a></div>
    </div>
    );
  }

});

ReactDOM.render(
  <Header />,
  document.getElementById('header')
);