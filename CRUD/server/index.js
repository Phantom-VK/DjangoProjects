const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const app = express();

// Middleware
app.use(cors());
app.use(express.json()); 

const userRoutes = require('./routes/userRoutes');
app.use('/api/users', userRoutes);

// MongoDB Connection
mongoose.connect('mongodb://127.0.0.1:27017/mern_crud')
    .then(() => console.log('Connected to MongoDB'))
    .catch(err => console.error('MongoDB connection error:', err));

// Basic route
app.get('/', (req, res) => {
    res.send('MERN CRUD Backend Running!');
});

// Start server
const PORT = 5000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});