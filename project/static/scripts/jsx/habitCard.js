var HabitCard = React.createClass({

  // sets initial state
  getInitialState: function(){
    return { complete: '' };
  },
  
  render: function() {

    return (
      <div className = "habit-card">
        <div className = "habit-card-title">
          {this.props.date}
        </div>
        <ul>
          <input type="checkbox" name={this.props.habit} checked={this.props.status == "true" && "checked"}/>{this.props.habit}
        </ul>
      </div>
    );
  }

});

module.exports = HabitCard;