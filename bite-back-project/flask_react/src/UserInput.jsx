import FormFood from "./FormFood";
import { useState } from "react";
import axios from "axios";
import macroPieChart from "./images/macro_pie_chart.png"; // Import your image files
import overlappedBarChart from "./images/overlapped_bar_chart.png";

/*Axios setup inspired by this article
How to use Axios POST requests
Author: Chimexie Innocent
Access: https://blog.logrocket.com/how-to-use-axios-post-requests/ */

function UserInput() {
  const [uiData, setUIData] = useState({
    food1Name: "Milk, evaporated, whole",
    food1Serving: "1",
    food2Name: "Pasta, vegetable, cooked",
    food2Serving: "2",
    food3Name: "Tomato juice cocktail",
    food3Serving: "3",
    food4Name: "Ice cream cone, soft serve, chocolate",
    food4Serving: "4",
    food5Name: "Licorice",
    food5Serving: "5",
  });
  const [profileData, setProfileData] = useState(null);
  //make object to fill in foods eaten
  //autofill object with premade data
  //add submit button
  //add object that prints out submitted data

  const handleChange = (event) => {
    const { name, value } = event.target;
    setUIData({
      ...uiData,
      [name]: value,
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
          suggestion1G: res.suggestion1G,
          suggestion2G: res.suggestion2G,
          suggestion3G: res.suggestion3G,
          suggestion4G: res.suggestion4G,
          suggestion5G: res.suggestion5G,
          graphTime: res.graphTime,
          suggestion1H: res.suggestion1H,
          suggestion2H: res.suggestion2H,
          suggestion3H: res.suggestion3H,
          suggestion4H: res.suggestion4H,
          suggestion5H: res.suggestion5H,
          hashTime: res.hashTime,
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
    <div className="uiDesign">
      <form onSubmit={handleSubmit}>
        <table>
          <tbody>
            <tr>
              <td>
                <label>
                  Food 1 Name
                  <input
                    type="text"
                    name="food1Name"
                    value={uiData.food1Name}
                    onChange={handleChange}
                  />
                </label>
                <p>Input Value: {uiData.food1Name}</p>
                <label>
                  Food 1 Serving
                  <input
                    type="text"
                    name="food1Serving"
                    value={uiData.food1Serving}
                    onChange={handleChange}
                  />
                </label>
                <p>Input Value: {uiData.food1Serving}</p>
              </td>

              <td>
                <label>
                  Food 2 Name
                  <input
                    type="text"
                    name="food2Name"
                    value={uiData.food2Name}
                    onChange={handleChange}
                  />
                </label>
                <p>Input Value: {uiData.food2Name}</p>
                <label>
                  Food 2 Serving
                  <input
                    type="text"
                    name="food2Serving"
                    value={uiData.food2Serving}
                    onChange={handleChange}
                  />
                </label>
                <p>Input Value: {uiData.food2Serving}</p>
              </td>

              <td>
                <label>
                  Food 3 Name
                  <input
                    type="text"
                    name="food3Name"
                    value={uiData.food3Name}
                    onChange={handleChange}
                  />
                </label>
                <p>Input Value: {uiData.food3Name}</p>
                <label>
                  Food 3 Serving
                  <input
                    type="text"
                    name="food3Serving"
                    value={uiData.food3Serving}
                    onChange={handleChange}
                  />
                </label>
                <p>Input Value: {uiData.food3Serving}</p>
              </td>

              <td>
                <label>
                  Food 4 Name
                  <input
                    type="text"
                    name="food4Name"
                    value={uiData.food4Name}
                    onChange={handleChange}
                  />
                </label>
                <p>Input Value: {uiData.food4Name}</p>
                <label>
                  Food 4 Serving
                  <input
                    type="text"
                    name="food4Serving"
                    value={uiData.food4Serving}
                    onChange={handleChange}
                  />
                </label>
                <p>Input Value: {uiData.food4Serving}</p>
              </td>

              <td>
                <label>
                  Food 5 Name
                  <input
                    type="text"
                    name="food5Name"
                    value={uiData.food5Name}
                    onChange={handleChange}
                  />
                </label>
                <p>Input Value: {uiData.food5Name}</p>
                <label>
                  Food 5 Serving
                  <input
                    type="text"
                    name="food5Serving"
                    value={uiData.food5Serving}
                    onChange={handleChange}
                  />
                </label>
                <p>Input Value: {uiData.food5Serving}</p>
              </td>
            </tr>
          </tbody>
        </table>

        <button type="submit">Submit</button>
      </form>
      {profileData && (
        <><div id="container">
          <div className="first">
            <h2>Graph Suggestions</h2>
            <p>1: {profileData.suggestion1G}</p>
            <p>2: {profileData.suggestion2G}</p>
            <p>3: {profileData.suggestion3G}</p>
            <p>4: {profileData.suggestion4G}</p>
            <p>5: {profileData.suggestion5G}</p>
          </div>
          <div className="second">
            <h2>Hash Suggestions</h2>
            <p>1: {profileData.suggestion1H}</p>
            <p>2: {profileData.suggestion2H}</p>
            <p>3: {profileData.suggestion3H}</p>
            <p>4: {profileData.suggestion4H}</p>
            <p>5: {profileData.suggestion5H}</p>
          </div>
          <div>
            <h2>RunTime Comparison</h2>
            <p>Graph runtime: {profileData.graphTime} Seconds</p>
            <p>Hash runtime: {profileData.hashTime} Seconds</p>
            <br></br>
          </div>
        </div>
        <div id="container-green" >
        <div className="first">
            <img src={macroPieChart} alt="Macro Pie Chart" />
          </div>
          <div className="second">
            <img src={overlappedBarChart} alt="Overlapped Bar Chart" />
          </div>
        </div></>
      
      )}

    </div>
  );
}



export default UserInput;
