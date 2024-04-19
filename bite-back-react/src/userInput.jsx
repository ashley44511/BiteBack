import autofilledData from "./autofilledData";
import form from "./form";

function userInput(props) {
  //make object to fill in foods eaten
  //autofill object with premade data
  //add submit button
  //add object that prints out submitted data
  const [count, setCount] = useState(0);

  return (
    <div>
      <div>
        <form formTitle="Food 1:" />
        <form formTitle="Food 2:" />
      </div>
      <div>
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
      </div>
    </div>
  );
}

export default userInput