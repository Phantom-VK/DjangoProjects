import React, { useState } from "react";
import { Link } from "react-router-dom";

function Users() {
    const [users, setUsers] = useState([{
        Name: "Vikramaditya",
        Email: "test@gmail.com",
        Age: 20
    }]);

    return (
        <div className="d-flex vh-100 bg-primary justify-content-center align-items-center">
            <div className="w-50 bg-white rounded p-3">
                <Link to="/create" className='btn btn-success'>Add +</Link>
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
                                    <button className="btn btn-success me-2">Edit</button>
                                    <button className="btn btn-danger">Delete</button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default Users; // Added this line