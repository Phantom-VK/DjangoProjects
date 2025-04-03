import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function CreateUser() {
    const [inputs, setInputs] = useState({
        Name: '',
        Email: '',
        Age: ''
    });
    const navigate = useNavigate();

    const handleChange = (e) => {
        setInputs(prev => ({
            ...prev,
            [e.target.name]: e.target.value
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('http://localhost:5000/api/users', inputs);
            navigate('/');
        } catch (err) {
            console.error(err);
        }
    };

    return (
        <div className="d-flex vh-100 bg-primary justify-content-center align-items-center">
            <div className="w-50 bg-white rounded p-3">
                <form onSubmit={handleSubmit}>
                    <h2>Add User</h2>
                    <div className="mb-2">
                        <label htmlFor="name">Name</label>
                        <input 
                            type="text" 
                            id="name" 
                            name="Name" 
                            className="form-control" 
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className="mb-2">
                        <label htmlFor="email">Email</label>
                        <input 
                            type="email" 
                            id="email" 
                            name="Email" 
                            className="form-control" 
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className="mb-2">
                        <label htmlFor="age">Age</label>
                        <input 
                            type="number" 
                            id="age" 
                            name="Age" 
                            className="form-control" 
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <button type="submit" className="btn btn-success">Submit</button>
                </form>
            </div>
        </div>
    );
}

export default CreateUser;