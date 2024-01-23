const express = require('express');
const router = express.Router();
const Razorpay = require('razorpay');

const razorpay = new Razorpay({
  key_id: 'your-razorpay-key-id',
  key_secret: 'your-razorpay-key-secret',
});

router.post('/create', async (req, res) => {
  try {
    const payment_capture = 1;
    const amount = 500; // Amount in paise
    const currency = 'INR';

    const options = {
      amount,
      currency,
      payment_capture,
    };

    const response = await razorpay.orders.create(options);

    res.json({
      id: response.id,
      amount: response.amount,
      currency: response.currency,
    });
  } catch (error) {
    console.error('Error creating Razorpay order:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

module.exports = router;
