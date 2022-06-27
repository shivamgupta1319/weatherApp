
import './App.css';
import {useEffect, useState} from 'react'
const req = require('axios');
function App() {
  useEffect(()=>{
    req.get('http://localhost:8080/data/'+cityName).then((response)=>{
      console.log(response.data);
  })})
  const [cityName,setCityname] = useState('')
  const fun = (event) => {
      setCityname(event.target.value);
      console.log(event.target.value);
  }
  return (
    <div className="App">
      <header className="App-header">
   
        <h1>Weather Report</h1>
        <input type="text" onChange={fun} value={cityName} name='city_name' placeholder='Enter city name'/><br></br><br></br><br></br>
        <button  class="button-29" role="button" type='submit' value={"submit"} >submit</button>
      </header>
    </div>
  );
}

export default App;
