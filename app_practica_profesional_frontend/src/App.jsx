//Import react-router-dom
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'; // Asegúrate de importar Routes
import './App.css'
import Login from './components/login/Login';

function App() {

  return (
    <>
      <Router>
        <Routes>
          <Route path='/' element={<Login/>}/>
        </Routes>
      </Router>
    </>
  )
}

export default App
