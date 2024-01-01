const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const nodemailer = require('nodemailer');

// Initialize Express
const app = express();
const port = process.env.PORT || 3000;

// Connect to MongoDB
mongoose.connect('mongodb+srv://dp:Welcome987@cluster0.5bbi6i0.mongodb.net/email?retryWrites=true&w=majority', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define a MongoDB Schema
const emailSchema = new mongoose.Schema({
  email: String,
});

// Create a MongoDB Model
const Email = mongoose.model('Email', emailSchema);

// Body parser middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Nodemailer configuration
const transporter = nodemailer.createTransport({
  service: 'Gmail', // e.g., 'Gmail', 'Yahoo', etc.
  auth: {
    user: 'dinakar.pathakota@gmail.com',
    pass: 'mwvm dfsx qxal wzze',
  },
});

// Define a route for the root path ("/")
app.get('/', (req, res) => {
    res.send('Hello, this is the landing page.');
});

// Express route for handling form submissions
app.post('/submit', async (req, res) => {
  const { email } = req.body;

  // Save the email to MongoDB
  const newEmail = new Email({ email });
  await newEmail.save();

  // Send a thank you email
  const mailOptions = {
    from: 'dinakar.pathakota@gmail.com',
    to: email,
    subject: 'Thank You for Subscribing',
    text: 'Thank you for subscribing to our newsletter!',
  };

  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      return console.log(error);
    }
    console.log('Email sent: ' + info.response);
  });

  res.send('Thank you! Check your email for confirmation.');
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
