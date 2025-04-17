import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';

function CreateUser() {
    const [inputs, setInputs] = useState({
        name: '',
        email: '',
        age: '',
        phone: '',
        address: '',
        role: 'user'
    });
    const [error, setError] = useState(null);
    const [isSubmitting, setIsSubmitting] = useState(false);
    const navigate = useNavigate();

    const handleChange = (e) => {
        setInputs({
            ...inputs,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsSubmitting(true);
        try {
            await axios.post('http://localhost:5000/api/users', inputs);
            navigate('/');
        } catch (err) {
            setError(err.response?.data?.error || 'Failed to create user');
            setIsSubmitting(false);
        }
    };

    return (
        <div className="min-vh-100 bg-tech-gradient text-light">
            <div className="container py-5">
                <div className="row justify-content-center">
                    <div className="col-lg-8">
                        <div className="card bg-dark-800 border-viper-green">
                            <div className="card-header bg-dark-700">
                                <div className="d-flex justify-content-between align-items-center">
                                    <h2 className="mb-0 gradient-text">
                                        <i className="fas fa-user-plus me-2"></i>
                                        Create New User
                                    </h2>
                                    <Link to="/" className="btn btn-sm btn-outline-tech-blue">
                                        <i className="fas fa-arrow-left me-2"></i>
                                        Back to Users
                                    </Link>
                                </div>
                            </div>
                            <div className="card-body">
                                {error && (
                                    <div className="alert alert-danger mb-4">
                                        <i className="fas fa-exclamation-circle me-2"></i>
                                        {error}
                                    </div>
                                )}

                                <form onSubmit={handleSubmit}>
                                    <div className="mb-4">
                                        <label className="form-label text-viper-green">
                                            <i className="fas fa-user me-2"></i>Full Name
                                        </label>
                                        <div className="input-group">
                                            <span className="input-group-text bg-dark-700 border-tech-blue">
                                                <i className="fas fa-id-badge text-tech-blue"></i>
                                            </span>
                                            <input
                                                type="text"
                                                name="name"
                                                className="form-control-light"
                                                value={inputs.name}
                                                onChange={handleChange}
                                                required
                                                placeholder="Enter full name"
                                            />
                                        </div>
                                    </div>

                                    <div className="mb-4">
                                        <label className="form-label text-viper-green">
                                            <i className="fas fa-envelope me-2"></i>Email
                                        </label>
                                        <div className="input-group">
                                            <span className="input-group-text bg-dark-700 border-tech-blue">
                                                <i className="fas fa-at text-tech-blue"></i>
                                            </span>
                                            <input
                                                type="email"
                                                name="email"
                                                className="form-control-light"
                                                value={inputs.email}
                                                onChange={handleChange}
                                                required
                                                placeholder="Enter email"
                                            />
                                        </div>
                                    </div>

                                    <div className="mb-5">
                                        <label className="form-label text-viper-green">
                                            <i className="fas fa-birthday-cake me-2"></i>Age
                                        </label>
                                        <div className="input-group">
                                        <span className="input-group-text bg-dark-700 border-tech-blue">
                                        <i className="fas fa-id-badge text-tech-blue"></i>
                                            </span>
                                            <input
                                                type="number"
                                                name="age"
                                                className="form-control-light"
                                                value={inputs.age}
                                                onChange={handleChange}
                                                required
                                                placeholder="Enter age"
                                                min="1"
                                                max="120"
                                            />
                                        </div>
                                    </div>

                                    <div className="mb-4">
    <label className="form-label text-viper-green">
        <i className="fas fa-phone me-2"></i>Phone
    </label>
    <div className="input-group">
        <span className="input-group-text bg-dark-700 border-tech-blue">
            <i className="fas fa-mobile-alt text-tech-blue"></i>
        </span>
        <input
            type="tel"
            name="phone"
            className="form-control-light"
            value={inputs.phone}
            onChange={handleChange}
            required
            placeholder="Enter phone number"
        />
    </div>
</div>

<div className="mb-4">
    <label className="form-label text-viper-green">
        <i className="fas fa-map-marker-alt me-2"></i>Address
    </label>
    <div className="input-group">
        <span className="input-group-text bg-dark-700 border-tech-blue">
            <i className="fas fa-home text-tech-blue"></i>
        </span>
        <input
            type="text"
            name="address"
            className="form-control-light"
            value={inputs.address}
            onChange={handleChange}
            required
            placeholder="Enter address"
        />
    </div>
</div>

<div className="mb-5">
    <label className="form-label text-viper-green">
        <i className="fas fa-user-tag me-2"></i>Role
    </label>
    <div className="input-group">
        <span className="input-group-text bg-dark-700 border-tech-blue">
            <i className="fas fa-users-cog text-tech-blue"></i>
        </span>
        <select
            name="role"
            className="form-control-light"
            value={inputs.role}
            onChange={handleChange}
            required
        >
            <option value="user">User</option>
            <option value="admin">Admin</option>
            <option value="editor">Editor</option>
        </select>
    </div>
</div>

                                    <div className="d-flex justify-content-end gap-3">
                                        <button
                                            type="button"
                                            onClick={() => navigate('/')}
                                            className="btn btn-outline-tech-blue px-4"
                                        >
                                            <i className="fas fa-times-circle me-2"></i>
                                            Cancel
                                        </button>
                                        <button
                                            type="submit"
                                            className="btn btn-viper-green px-4"
                                            disabled={isSubmitting}
                                        >
                                            {isSubmitting ? (
                                                <>
                                                    <span className="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
                                                    Processing...
                                                </>
                                            ) : (
                                                <>
                                                    <i className="fas fa-save me-2"></i>
                                                    Create User
                                                </>
                                            )}
                                        </button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default CreateUser;