import React, { useState } from 'react';
import { TextField, Button, Container, Typography, Box } from '@mui/material';

const Login = ({ onLogin }) => {
    const[email, setemail] = useState('');
    const[password, setPassword] = useState('');

    const handleemailChange = (event) => {
        setemail(event.target.value);
    }

    const handlePasswordChange = (event) => {
        setPassword(event.target.value);
    }

    const handleLoginFormSubmit = (event) =>{
        event.preventDefault();
        if (email && password) {
            onLogin(email,password);
        }
    };


    return (
    <Container style={{maxWidth : "400px"}}>
        <Box mt={5} p={3} bgcolor="white" boxShadow={3}>
          <Typography variant="h4" align="center">
            Login
          </Typography>
          <form onSubmit={handleLoginFormSubmit}>
            <TextField
              type = "email"
              label="email"
              variant="outlined"
              fullWidth
              value={email}
              onChange={handleemailChange}
              margin="normal"
            />
            <TextField
              label="Password"
              variant="outlined"
              type="password"
              fullWidth
              value={password}
              onChange={handlePasswordChange}
              margin="normal"
            />
            <Button type="submit" variant="contained" color="primary" fullWidth>
              Login
            </Button>
          </form>
        </Box>
      </Container>

    );
};

export default Login;