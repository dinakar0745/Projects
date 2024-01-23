import React, { useState } from 'react';
import { loadScript } from 'react-script-tag';

const Payment = () => {
  const [payment, setPayment] = useState(null);

  const initializePayment = async () => {
    const res = await fetch('/api/payment/create', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    const data = await res.json();

    const options = {
      key: 'your-razorpay-key',
      amount: data.amount,
      currency: data.currency,
      name: 'Your Company Name',
      description: 'Payment for your service',
      order_id: data.id,
      handler: (response) => {
        console.log(response);
        // Handle success or failure
      },
    };

    const paymentInstance = new window.Razorpay(options);
    paymentInstance.open();
    setPayment(paymentInstance);
  };

  return (
    <div>
      <h2>Payment Page</h2>
      <button onClick={initializePayment}>Pay Now</button>
      {loadScript('https://checkout.razorpay.com/v1/checkout.js')}
    </div>
  );
};

export default Payment;
