import FormFood from "./FormFood";
import { useState } from "react";
import axios from "axios";

/*Axios setup inspired by this article
How to use Axios POST requests
Author: Chimexie Innocent
Access: https://blog.logrocket.com/how-to-use-axios-post-requests/ */

function UserInput() {
  const [uiData, setUIData] = useState({
    food1Name: "Milk",
    food1Serving: "1",
    food2Name: "Pasta",
    food2Serving: "2",
    food3Name: "Tomato",
    food3Serving: "3",
    food4Name: "Carne Asada",
    food4Serving: "4",
    food5Name: "Rice",
    food5Serving: "5",
  });
  const [profileData, setProfileData] = useState(null);
  //make object to fill in foods eaten
  //autofill object with premade data
  //add submit button
  //add object that prints out submitted data

  const handleChange = (event) => {
    const value = event.target.value;
    setUIData({
      [event.target.name]: value,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const userData = {
      food1Name: uiData.food1Name,
      food1Serving: uiData.food1Serving,
      food2Name: uiData.food2Name,
      food2Serving: uiData.food2Serving,
      food3Name: uiData.food3Name,
      food3Serving: uiData.food3Serving,
      food4Name: uiData.food4Name,
      food4Serving: uiData.food4Serving,
      food5Name: uiData.food5Name,
      food5Serving: uiData.food5Serving,
    };
    axios
      .post("/profile/", userData)
      .then((response) => {
        const res = response.data;
        setProfileData({
          profile_name: res.name,
          about_me: res.about,
          result: res.result,
        });
      })
      .catch((error) => {
        if (error.response) {
          console.log(error.response);
          console.log(error.response.status);
          console.log(error.response.headers);
        }
      });
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Food1 Name
          <input type="text" value={uiData.food1Name} onChange={handleChange} />
        </label>
        <p>Input Value: {uiData.food1Name}</p>
        <label>
          Food1 Serving
          <input
            type="text"
            value={uiData.food1Serving}
            onChange={handleChange}
          />
        </label>
        <p>Input Value: {uiData.food1Serving}</p>
        <button type="submit">SubmitTest</button>
        {profileData && (
          <div>
            <p>Profile name: {profileData.profile_name}</p>
            <p>About me: {profileData.about_me}</p>
            <p>Result: {profileData.result}</p>
          </div>
        )}
      </form>
    </div>
  );
}

export default UserInput;
