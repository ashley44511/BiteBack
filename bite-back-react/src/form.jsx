import {useState} from 'react';

//https://www.freecodecamp.org/news/how-to-build-forms-in-react/
 
export default function  form({formTitle})  {
	const  [inputValue, setInputValue] =  useState('');

	const  handleChange = (event) => {
		setInputValue(event.target.value);
	};

return  (
<form>
	<label>{formTitle}
	<input  type="text"  value={inputValue} onChange={handleChange} />
	</label>
	<p>Input Value: {inputValue}</p>
</form>
)};