import { useState } from "react";

//https://www.freecodecamp.org/news/how-to-build-forms-in-react/

export default function FormFood({ formTitle, formValue }) {
  const [inputValue, setInputValue] = useState("");

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  return (
    <></>
  );
}
