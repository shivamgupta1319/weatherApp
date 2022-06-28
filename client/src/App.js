
import './App.css';
import { useState } from 'react'
import BasicCard from './components/card';
const req = require('axios');
function App() {


  const [cityName, setCityname] = useState('')
  const [data, setData] = useState({})
  const fun = (event) => {
    setCityname(event.target.value);
    
  }

  const handleSubmit = () => {
    req.post('http://127.0.0.1:5000/data/' + cityName).then((response) => {
        setData(response.data);
    })
  }

  return (
    <div className="App">
      <header className="App-header">

        <h1>Weather Report</h1>
        <input type="text" onChange={fun} value={cityName} name='city_name' placeholder='Enter city name' /><br></br><br></br><br></br>
        <button className="button-29" role="button" type='submit' value={"submit"} onClick={() => {handleSubmit()}} >submit</button>
      </header>
      <br></br><br></br><br></br>
      { Object.keys(data).length > 0 && <BasicCard weatherDetails={data}/>}
    </div>


  );
}

export default App;
