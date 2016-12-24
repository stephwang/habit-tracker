var HabitCard = require('./habitCard');
var Header = require('./header');

var TrackerPage = React.createClass({

  render: function() {
    var data = this.props.data;

    console.log(data);
    
    return (
      <div>
        { data.map(function(item){ return <HabitCard date={item.date} habit={item.habit} status={item.status}/> }) }
      </div>
    );
  }

});

// list of days, defined with JavaScript object literals
var data = [
  {
    "date": "Dec 23"
    , "habit": "coding"
    , "status": "false"
  }
  , {
    "date": "Dec 24"
    , "habit": "coding"
    , "status": "true"
  }
];

ReactDOM.render(
  <TrackerPage data={ data } />,
  document.getElementById('main')
);

ReactDOM.render(
  <Header />,
  document.getElementById('header')
);