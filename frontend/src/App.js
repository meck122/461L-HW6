import React, { useState } from "react";

function App() {
  const [last_name, setLastName] = useState("Off");
  // const [data, setData]=useState(null)

  function getData(val)
  {
    // setData(val.target.value)
    console.warn(val.target.value)
    fetch("http://127.0.0.1:5000/textbox/" + val.target.value)
          .then(response => 
              response.json()
          )
          .then(data => {
              setLastName(data.last_name)
              console.log(last_name)
          })
          .catch(error => {
              console.log(error)
          })
  }

  return (
    <div className="App">
      <div>
            <input
                onChange={getData}
            />
            <p>{last_name}</p>
        </div>
    </div>
  );
}

export default App;
