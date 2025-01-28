import { useEffect, useState } from 'react'
import './Login.css'
import axios from 'axios'

function Login(){

    // Use state for get user data
    const [getUser,setUser] = useState({
        username:'',
        password:''
    })

    
    const handleFormLogin = (e) => {
        const {username,password} = e.target;
        setUser((prevUser) => ({
            ...prevUser, [username]:password
        }));
    }

    // doLogin for login user
    const doLogin = async (e) => {
        e.preventDefault();


        try{
            const response = await axios.post(process.env.REACT_APP_API_URL,"auth/login_api/",{
                username : getUser.username,
                password : getUser.password
            });

            console.log(response.msg)
        }catch(error){
            console.log(error.msg)
        }

    }


    return(
        <>
            <section>
                <div id="login">
                    <p>SISTEMA DE PAGO DE IMPUESTO PREDIALES</p>
                    <p>INICIO DE SESIÓN</p>
                    <form onSubmit={doLogin}>
                        <input type="text" placeholder="Usuario" value={getUser.username} onChange={handleFormLogin}/>
                        <input type="text" placeholder="Contraseña" value={getUser.password} onChange={handleFormLogin}/>
                        <button type="submit">Iniciar Sesión</button>
                    </form>
                    <a href="">Olvidaste tu contraseña?</a>
                </div>
                <div id="background">
                    <div>
                        <figure>
                            <img src="https://minatitlan.gob.mx/img/logoMina.png" alt="" />
                        </figure>
                    </div>
                </div>
            </section>
        </>
    )
}

export default Login