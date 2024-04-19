import { useState } from 'react'
import './App.css'

import autofilledData from "./autofilledData"; //create autofilled data
import userInput from "./userInput"; //five foods user input
import form from "./form";
//other components to add: header, food fact, footer


function App() {
  
  //const [submitted, setSubmitted] = useState(false);
  //const [autofilled, setAutofilled] = useState(autofilledData.foodOne);
  const  [inputValue, setInputValue] =  useState('');

  const  handleChange = (event) => {
		setInputValue(event.target.value);
	};

  return (
    <>
      <h1 color="black">test</h1>
      <form>
	      <label>formTitle
	      <input  type="text"  value={inputValue} onChange={handleChange} />
	      </label>
	      <p>Input Value: {inputValue}</p>
      </form>
      <p>
        Output:
      </p>
    </>
  )
}

export default App


//https://www.freecodecamp.org/news/how-to-build-forms-in-react/
