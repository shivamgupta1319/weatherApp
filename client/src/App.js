import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <form className="App-form" action='/store' role="form" method='post' enctype="multipart/form-data">
        <input type="text" name='city_name' placeholder='Enter city name'/>
        <button type='submit' value={submit}></button>
        </form>
      </header>
    </div>
  );
}

export default App;
