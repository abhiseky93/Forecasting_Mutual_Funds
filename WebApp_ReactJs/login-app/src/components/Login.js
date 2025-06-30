import React, { useState } from 'react';
import {
  MDBContainer,
  MDBInput,
  MDBBtn,
  MDBCard,
  MDBCardBody,
  MDBCardHeader,
  MDBCardFooter
} from 'mdb-react-ui-kit';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = (e) => {
    e.preventDefault();
    // Handle login logic here
    console.log('Logging in with:', email, password);
  };

  return (
    <MDBContainer className="d-flex justify-content-center align-items-center vh-100">
      <MDBCard style={{ maxWidth: '400px', width: '100%' }}>
        <MDBCardHeader className="text-center">
          <h3>Login</h3>
        </MDBCardHeader>
        <MDBCardBody>
          <form onSubmit={handleLogin}>
            <MDBInput
              label="Email"
              id="emailInput"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="mb-4"
            />
            <MDBInput
              label="Password"
              id="passwordInput"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="mb-4"
            />
            <MDBBtn type="submit" className="mb-4" color="primary" block>
              Log In
            </MDBBtn>
          </form>
        </MDBCardBody>
        <MDBCardFooter className="text-center">
          <p>Don’t have an account? <a href="#">Sign Up</a></p>
        </MDBCardFooter>
      </MDBCard>
    </MDBContainer>
  );
};

export default Login;
