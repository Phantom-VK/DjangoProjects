const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const path = require('path'); 
const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// API Routes
const userRoutes = require('./routes/userRoutes');
app.use('/api/users', userRoutes);

mongoose.connect('mongodb+srv://2022bit052:OOad5MumuWkJfh02@cluster0.noxkp4q.mongodb.net/your-database-name?retryWrites=true&w=majority')
    .then(() => console.log('Connected to MongoDB'))
    .catch(err => console.error('MongoDB connection error:', err));




// Basic route
app.get('/', (req, res) => {
  res.send('MERN CRUD Backend Running!');
});

// Start server
const PORT = process.env.PORT || 5000;
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server running on port ${PORT}`);
});