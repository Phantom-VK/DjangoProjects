import React, { useState, useEffect } from "react";
import axios from 'axios';
import { Link } from 'react-router-dom';

function Users() {
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [searchTerm, setSearchTerm] = useState("");

    useEffect(() => {
        fetchUsers();
    }, []);

    const fetchUsers = async () => {
        try {
            const res = await axios.get('http://localhost:5000/api/users');
            setUsers(res.data);
        } catch (err) {
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const handleDelete = async (id) => {
        if (window.confirm("Are you sure you want to delete this user?")) {
            try {
                await axios.delete(`http://localhost:5000/api/users/${id}`);
                fetchUsers();
            } catch (err) {
                console.error(err);
            }
        }
    };

    const filteredUsers = users.filter(user => 
        user.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        user.email.toLowerCase().includes(searchTerm.toLowerCase())
    );

    return (
        <div className="min-vh-100 bg-tech-gradient text-light">
            <div className="container py-5">
                <div className="d-flex justify-content-between align-items-center mb-4">
                    <h1 className="gradient-text">
                        <i className="fas fa-users me-2"></i>User Dashboard
                    </h1>
                    <Link to="/create" className="btn btn-tech-blue pulse-animation">
                        <i className="fas fa-plus-circle me-2"></i>Add User
                    </Link>
                </div>

                <div className="card bg-dark-800 border-viper-green mb-4">
                    <div className="card-body">
                        <div className="input-group">
                            <span className="input-group-text bg-dark-700 border-tech-blue text-tech-blue">
                                <i className="fas fa-search"></i>
                            </span>
                            <input 
                                type="text" 
                                className="form-control-light"
                                placeholder="Search users by name or email..."
                                value={searchTerm}
                                onChange={(e) => setSearchTerm(e.target.value)}
                            />
                        </div>
                    </div>
                </div>

                <div className="card bg-dark-800 border-viper-green">
                    <div className="card-body p-0">
                        {loading ? (
                            <div className="text-center py-5">
                                <div className="spinner-border text-viper-green" role="status">
                                    <span className="visually-hidden">Loading...</span>
                                </div>
                                <p className="mt-3 text-viper-green">Loading users data...</p>
                            </div>
                        ) : filteredUsers.length === 0 ? (
                            <div className="text-center py-5">
                                <i className="fas fa-user-slash text-tech-blue fa-3x mb-3"></i>
                                <p className="text-light">No users found. {searchTerm && 'Try a different search term or'} add a new user.</p>
                            </div>
                        ) : (
                            <div className="table-responsive">
                                <table className="table table-dark table-hover mb-0">
                                    <thead>
                                        <tr>
                                            <th className="ps-4">
                                                <i className="fas fa-user me-2 text-viper-green"></i>Name
                                            </th>
                                            <th>
                                                <i className="fas fa-envelope me-2 text-viper-green"></i>Email
                                            </th>
                                            <th>
                                                <i className="fas fa-birthday-cake me-2 text-viper-green"></i>Age
                                            </th>
                                            <th className="text-end pe-4">Actions</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {filteredUsers.map((user) => (
                                            <tr key={user._id} className="align-middle">
                                                <td className="ps-4 fw-bold">{user.name}</td>
                                                <td>{user.email}</td>
                                                <td>{user.age}</td>
                                                <td className="text-end pe-4">
                                                    <Link 
                                                        to={`/update/${user._id}`} 
                                                        className="btn btn-sm btn-viper-outline me-2"
                                                    >
                                                        <i className="fas fa-edit me-1"></i>Edit
                                                    </Link>
                                                    <button 
                                                        onClick={() => handleDelete(user._id)} 
                                                        className="btn btn-sm btn-danger"
                                                    >
                                                        <i className="fas fa-trash-alt me-1"></i>Delete
                                                    </button>
                                                </td>
                                            </tr>
                                        ))}
                                    </tbody>
                                </table>
                            </div>
                        )}
                    </div>
                </div>
                
                <div className="text-center mt-4 text-muted">
                    <p className="small">
                        <i className="fas fa-code me-2 text-tech-blue"></i>
                        Total Users: {filteredUsers.length}
                    </p>
                </div>
            </div>
        </div>
    );
}

export default Users;