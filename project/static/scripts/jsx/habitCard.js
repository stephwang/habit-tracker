var HabitCard = React.createClass({

  // sets initial state
  getInitialState: function(){
    return { complete: '' };
  },

  render: function() {
    var date = this.props.date;
    var habit = this.props.habit;
    console.log(date);
    console.log(habit);

    return (
      <div class="habit-card">
        <div class="habit-card-title">
          {{date}}
        </div>
        <ul>
          <li>{{habit}}</li>
        </ul>
      </div>
    );
  }

});

module.exports = HabitCard;