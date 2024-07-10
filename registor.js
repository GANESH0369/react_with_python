// Register.js
import React, { Component } from 'react';
import axios from 'axios';

class Register extends Component {
  constructor(props) {
    super(props);
    this.state = {
      fname: '',
      lname: '',
      email: '',
      password: ''
    };
  }

  handleChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  handleSubmit = async (e) => {
    e.preventDefault();
    const { fname, lname, email, password } = this.state;
    try {
      const response = await axios.post('http://localhost:8000/', { fname, lname, email, password });
      console.log(response.data);
      alert("Thank you for registration!");
    } catch (error) {
      console.error('Error:', error);
      alert("Registration failed. Please try again.");
    }
  };

  render() {
    const { fname, lname, email, password } = this.state;
    return (
      <div className="App">
        <h1>User Registration</h1>
        <form onSubmit={this.handleSubmit} className="registration-form">
          <input type="text" name="fname" value={fname} onChange={this.handleChange} placeholder="First Name" required />
          <input type="text" name="lname" value={lname} onChange={this.handleChange} placeholder="Last Name" required />
          <input type="email" name="email" value={email} onChange={this.handleChange} placeholder="Email" required />
          <input type="password" name="password" value={password} onChange={this.handleChange} placeholder="Password" required />
          <button type="submit">Register</button>
        </form>
      </div>
    );
  }
}

export default Register;
