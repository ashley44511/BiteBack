import { useState } from "react";
import axios from "axios";
import "./App.css";

import UserInput from "./UserInput"; //five foods user input
import FormFood from "./FormFood";
//other components to add: header, food fact, footer

function App() {
  // new line start
  const [profileData, setProfileData] = useState(null);
  //const [submitted, setSubmitted] = useState(false);
  //const [autofilled, setAutofilled] = useState(autofilledData.foodOne);
  //const [inputValue, setInputValue] = useState("");
  /*
  const handleChange = (event) => {
    setInputValue(event.target.value);
  }; */

  function getData() {
    axios({
        method: "POST",
        url: "/profile/",
      })
      .then((response) => {
        const res = response.data;
        setProfileData({
          profile_name: res.name,
          about_me: res.about,
        });
      })
      .catch((error) => {
        if (error.response) {
          console.log(error.response);
          console.log(error.response.status);
          console.log(error.response.headers);
        }
      });
  }
  //end of new line

  return (
    <div className="App">
      <header className="App-header">
        <h1>Bite Back</h1>
        <p>
          This tool suggests food items to add to your meals to improve overall
          nutrition value
        </p>
        {/* new line start*/}
        <p>Enter items from your meal below:</p>
        <UserInput />
        <button onClick={getData}>Submit</button>
        {profileData && (
          <div>
            <p>Profile name: {profileData.profile_name}</p>
            <p>About me: {profileData.about_me}</p>
          </div>
        )}
        {/* end of new line */}
      </header>
    </div>
  );
}

export default App;
