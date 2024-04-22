import FormFood from "./FormFood";
import { useState } from "react";
import axios from "axios";

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
  /**
   * suggestion1H: res.suggestion1H,
          suggestion2H: res.suggestion2H,
          suggestion3H: res.suggestion3H,
          suggestion4H: res.suggestion4H,
          suggestion5H: res.suggestion5H,
          hashTime: res.hashTime,
   */

  return (
    <div className="uiDesign">
      <form onSubmit={handleSubmit}>
        <table>
          <tbody>
            <tr>
              <td>
                <label>
                  Food1 Name
                  <input
                    type="text"
                    name="food1Name"
                    value={uiData.food1Name}
                    onChange={handleChange}
                  />
                </label>
                <p>Input Value: {uiData.food1Name}</p>
                <label>
                  Food1 Serving
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
                  Food2 Name
                  <input
                    type="text"
                    name="food2Name"
                    value={uiData.food2Name}
                    onChange={handleChange}
                  />
                </label>
                <p>Input Value: {uiData.food2Name}</p>
                <label>
                  Food2 Serving
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
                  Food3 Name
                  <input
                    type="text"
                    name="food3Name"
                    value={uiData.food3Name}
                    onChange={handleChange}
                  />
                </label>
                <p>Input Value: {uiData.food3Name}</p>
                <label>
                  Food3 Serving
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
                  Food4 Name
                  <input
                    type="text"
                    name="food4Name"
                    value={uiData.food4Name}
                    onChange={handleChange}
                  />
                </label>
                <p>Input Value: {uiData.food4Name}</p>
                <label>
                  Food4 Serving
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
                  Food5 Name
                  <input
                    type="text"
                    name="food5Name"
                    value={uiData.food5Name}
                    onChange={handleChange}
                  />
                </label>
                <p>Input Value: {uiData.food5Name}</p>
                <label>
                  Food5 Serving
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
        <div>
          <p>Suggestion1G: {profileData.suggestion1G}</p>
          <p>Suggestion2G: {profileData.suggestion2G}</p>
          <p>Suggestion3G: {profileData.suggestion3G}</p>
          <p>Suggestion4G: {profileData.suggestion4G}</p>
          <p>Suggestion5G: {profileData.suggestion5G}</p>
          <p>graphTime: {profileData.graphTime}</p>
        </div>
      )}
    </div>
  );
}

/**
 * <p>Suggestion1H: {profileData.suggestion1H}</p>
          <p>Suggestion2H: {profileData.suggestion2H}</p>
          <p>Suggestion3H: {profileData.suggestion3H}</p>
          <p>Suggestion4H: {profileData.suggestion4H}</p>
          <p>Suggestion5H: {profileData.suggestion5H}</p>
          <p>hashTime: {profileData.hashTime}</p>
 */

export default UserInput;
