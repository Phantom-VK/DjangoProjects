import React, { useState, useEffect } from "react";
import axios from 'axios';
import { Link } from 'react-router-dom';

function Users() {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        fetchUsers();
    }, []);

    const fetchUsers = async () => {
        try {
            const res = await axios.get('http://localhost:5000/api/users');
            setUsers(res.data);
        } catch (err) {
            console.error(err);
        }
    };

    const handleDelete = async (id) => {
        try {
            await axios.delete(`http://localhost:5000/api/users/${id}`);
            fetchUsers();
        } catch (err) {
            console.error(err);
        }
    };

    return (
        <div className="d-flex vh-100 bg-primary justify-content-center align-items-center">
            <div className="w-50 bg-white rounded p-3">
                <Link to="/create" className="btn btn-success mb-3">Add +</Link>
                <table className="table">
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Email</th>
                            <th>Age</th>
                            <th>Action</th>           
                        </tr>
                    </thead>
                    <tbody>
                        {users.map((user, index) => (
                            <tr key={index}>
                                <td>{user.Name}</td>
                                <td>{user.Email}</td>
                                <td>{user.Age}</td>
                                <td>
                                    <Link to={`/update/${user._id}`} className="btn btn-primary me-2">Edit</Link>
                                    <button 
                                        onClick={() => handleDelete(user._id)} 
                                        className="btn btn-danger"
                                    >
                                        Delete
                                    </button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default Users;