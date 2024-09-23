import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
    const [userData, setUserData] = useState({
        name: '',
        email: '',
        preferences: '',
        affiliate: false
    });
    const [responseMessage, setResponseMessage] = useState('');
    const [users, setUsers] = useState([]);

    // Obtener usuarios desde el backend
    useEffect(() => {
        async function fetchUsers() {
            const response = await fetch('http://127.0.0.1:8000/api/get_users/');
            const data = await response.json();
            setUsers(data.users || []);
        }
        fetchUsers();
    }, []);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setUserData({ ...userData, [name]: value });
    };

    const handleCheckboxChange = () => {
        setUserData({ ...userData, affiliate: !userData.affiliate });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch('http://127.0.0.1:8000/api/post_user/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(userData),
        });
        const data = await response.json();
        setResponseMessage(data.message || data.error);

        // Actualizar la lista de usuarios después de crear uno nuevo
        const usersResponse = await fetch('http://127.0.0.1:8000/api/get_users/');
        const usersData = await usersResponse.json();
        setUsers(usersData.users || []);
    };

    return (
        <div className="container mt-5">
            <h2 className="text-center">Formulario de Usuario</h2>
            <form onSubmit={handleSubmit} className="mb-5 p-4 bg-light shadow-sm rounded">
                <div className="mb-3">
                    <label className="form-label">Nombre</label>
                    <input
                        type="text"
                        className="form-control"
                        name="name"
                        value={userData.name}
                        onChange={handleChange}
                        placeholder="Ingresa tu nombre"
                    />
                </div>
                <div className="mb-3">
                    <label className="form-label">Email</label>
                    <input
                        type="email"
                        className="form-control"
                        name="email"
                        value={userData.email}
                        onChange={handleChange}
                        placeholder="Ingresa tu email"
                    />
                </div>
                <div className="mb-3">
                    <label className="form-label">Preferencias (separadas por comas)</label>
                    <input
                        type="text"
                        className="form-control"
                        name="preferences"
                        value={userData.preferences}
                        onChange={handleChange}
                        placeholder="Ejemplo: 1,2,7"
                    />
                </div>
                <div className="form-check mb-3">
                    <input
                        className="form-check-input"
                        type="checkbox"
                        name="affiliate"
                        checked={userData.affiliate}
                        onChange={handleCheckboxChange}
                    />
                    <label className="form-check-label">Afiliado</label>
                </div>
                <button type="submit" className="btn btn-primary w-100">Enviar</button>
            </form>

            {responseMessage && (
                <div className="alert alert-info text-center">
                    {responseMessage}
                </div>
            )}

            <h3 className="mt-5 text-center">Lista de Usuarios</h3>
            <div className="row">
                {users.map((user, index) => (
                    <div className="col-md-4" key={index}>
                        <div className={`card mb-4 shadow-sm ${user.affiliate ? 'border-success' : 'border-secondary'}`}>
                            <div className="card-body">
                                <h5 className="card-title">{user.name}</h5>
                                <p className="card-text">
                                    <a href={`mailto:${user.email}`} className="text-decoration-none">{user.email}</a>
                                </p>
                                <p className="card-text">
                                    <strong>Preferencias:</strong> {user.preferences.join(', ')}
                                </p>
                                <p className={`card-text ${user.affiliate ? 'text-success' : 'text-muted'}`}>
                                    {user.affiliate ? 'Afiliado' : 'No afiliado'}
                                </p>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default App;
