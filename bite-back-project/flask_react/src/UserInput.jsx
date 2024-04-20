
import FormFood from "./FormFood";
import { useState } from "react";

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
  //make object to fill in foods eaten
  //autofill object with premade data
  //add submit button
  //add object that prints out submitted data

  return (
    <div>
      <div>
        <FormFood formTitle={"Food 1 Name"} formValue={uiData.food1Name} />
        <FormFood
          formTitle={"Food 1 Serving"}
          formValue={uiData.food1Serving}
        />
        <FormFood formTitle={"Food 2 Name"} formValue={uiData.food2Name} />
        <FormFood
          formTitle={"Food 2 Serving"}
          formValue={uiData.food2Serving}
        />
        <FormFood formTitle={"Food 3 Name"} formValue={uiData.food3Name} />
        <FormFood
          formTitle={"Food 3 Serving"}
          formValue={uiData.food3Serving}
        />
        <FormFood formTitle={"Food 4 Name"} formValue={uiData.food4Name} />
        <FormFood
          formTitle={"Food 4 Serving"}
          formValue={uiData.food4Serving}
        />
        <FormFood formTitle={"Food 5 Name"} formValue={uiData.food5Name} />
        <FormFood
          formTitle={"Food 5 Serving"}
          formValue={uiData.food5Serving}
        />
      </div>
    </div>
  );
}

export default UserInput;
