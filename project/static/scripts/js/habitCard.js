(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
var HabitCard = React.createClass({displayName: "HabitCard",

  // sets initial state
  getInitialState: function(){
    return { complete: '' };
  },
  
  render: function() {

    return (
      React.createElement("div", {className: "habit-card"}, 
        React.createElement("div", {className: "habit-card-title"}, 
          this.props.date
        ), 
        React.createElement("ul", null, 
          React.createElement("input", {type: "checkbox", name: this.props.habit, checked: this.props.status == "true" && "checked"}), this.props.habit
        )
      )
    );
  }

});

module.exports = HabitCard;

},{}]},{},[1]);
