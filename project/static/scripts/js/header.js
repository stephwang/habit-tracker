(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
var Header = React.createClass({displayName: "Header",
  
  render: function() {

    return (
    React.createElement("div", {className: "header-elements"}, 
        React.createElement("div", {className: "logo"}, React.createElement("a", {href: "/"}, "Habitz")), 
        React.createElement("div", {className: "sign-up"}, React.createElement("a", {href: "/signup"}, "Sign up")), 
        React.createElement("div", {className: "log-in"}, React.createElement("a", {href: "/login"}, "Log in"))
    )
    );
  }

});

ReactDOM.render(
  React.createElement(Header, null),
  document.getElementById('header')
);

},{}]},{},[1]);
