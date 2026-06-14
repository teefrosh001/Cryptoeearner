const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname)));

// In-memory data store (for demo - persists while server runs)
let users = [
  { id: 1, username: 'user1', email: 'user@example.com', balance: 1250.75, status: 'active' }
];
let deposits = [];
let withdrawals = [];
let plans = [
  { id: 1, name: 'Starter', min: 100, max: 1000, duration: '7 days', profit: '15%' },
  { id: 2, name: 'Silver', min: 1000, max: 5000, duration: '14 days', profit: '25%' },
  { id: 3, name: 'Gold', min: 5000, max: 20000, duration: '30 days', profit: '40%' },
  { id: 4, name: 'VIP', min: 20000, max: 100000, duration: '60 days', profit: '60%' }
];
let transactions = [];

// Admin credentials
const ADMIN_USER = 'makeit001';
const ADMIN_PASS = 'Makemoney@12';

// Routes
app.get('/api/users', (req, res) => res.json(users));
app.get('/api/deposits', (req, res) => res.json(deposits));
app.get('/api/withdrawals', (req, res) => res.json(withdrawals));
app.get('/api/plans', (req, res) => res.json(plans));

// Login (simple demo)
app.post('/api/login', (req, res) => {
  const { email, password } = req.body;
  // Demo login - accept any
  res.json({ success: true, user: { email, balance: 1250.75 } });
});

app.post('/api/admin/login', (req, res) => {
  const { username, password } = req.body;
  if (username === ADMIN_USER && password === ADMIN_PASS) {
    res.json({ success: true });
  } else {
    res.status(401).json({ success: false, message: 'Invalid credentials' });
  }
});

// Approve deposit
app.post('/api/deposits/approve/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const dep = deposits.find(d => d.id === id);
  if (dep) {
    const user = users.find(u => u.id === dep.userId);
    if (user) user.balance += dep.amount;
    dep.status = 'approved';
    transactions.push({ type: 'deposit', ...dep });
    res.json({ success: true });
  } else {
    res.status(404).json({ success: false });
  }
});

// Similar for withdrawals, etc. (simplified)
app.post('/api/withdrawals/approve/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const wd = withdrawals.find(w => w.id === id);
  if (wd) {
    wd.status = 'approved';
    transactions.push({ type: 'withdrawal', ...wd });
    res.json({ success: true });
  }
});

app.post('/api/balance/update', (req, res) => {
  const { userId, amount } = req.body;
  const user = users.find(u => u.id === userId);
  if (user) {
    user.balance += parseFloat(amount);
    res.json({ success: true, newBalance: user.balance });
  }
});

app.get('/api/transactions', (req, res) => res.json(transactions));

app.listen(PORT, () => {
  console.log(`🚀 CryptoEarner Server running at http://localhost:${PORT}`);
  console.log(`Open index.html or go to http://localhost:${PORT}`);
});
