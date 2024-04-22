<h1>Hello! Welcome to BiteBack. This full-stack project aims to improve the nutrition choices of our users.</h1>

<p>Proposal: https://docs.google.com/document/d/1n-0uhMOCrZ74qeJcQnSx6GGP20M0qRgrIPWWQG3i-1M/edit?usp=sharing</p>
<p>Planning: https://docs.google.com/document/d/16jeHNHj802-zguv49YW67QjcspoXpWC0BTI9WfnULJI/edit?usp=sharing</p>
<p>Data sources: https://think.cs.vt.edu/corgis/csv/food/ https://think.cs.vt.edu/corgis/python/food/</p>
<p>Final Report: https://docs.google.com/document/d/1uiY8fuBUwxjSFu4GX8bloH63Rh8TuoJourvERnBV6Ac/edit?usp=sharing</p>

<p>Before running any scripts (especially main.py), please use the following commands:</p>
cd bite-back-project
cd flask_react
cd backend
For mac/unix users: python3 -m venv env
For windows users: py -m venv env
For mac/unix users: source env/bin/activate
For windows users: .\env\Scripts\activate
pip install flask python-dotenv plotly pandas flask_cors kaleido


cd bite-back-project
cd flask_react
npm install


<p>To run for the first time after cloning:</p>
Open a new terminal.
cd bite-back-project
cd flask_react
npm install
npm start
The frontend should now be set up.
Open another terminal.
cd bite-back-project
cd flask_react
cd backend
Create a virtual environment.
For mac/unix users: python3 -m venv env
For windows users: py -m venv env
Activate the virtual environment. When restarting the project, you only need to activate from now on.
For mac/unix users: source env/bin/activate
For windows users: .\env\Scripts\activate
pip install flask python-dotenv plotly pandas flask_cors kaleido
flask run
The backend is now running, and the submit button on the website will now work.


<h2>To run through the UI:</h2>
<h4>Open a terminal window</h4>
<p>run: cd bite-back-project/flask_react/backend </p>
<p>(on mac) run: source env/bin/activate</p>
<p>(on windows) run: .\env\Scripts\activate</p>
<p>run: npm run start-backend</p>
<h4>Open another terminal window</h4>
<p>run: cd bite-back-project/flask_react</p>
<p>run: npm start</p>
<h3>The window should open on http://localhost:3000/</h3>

<p> if you have issues, try troubleshooting with this article: https://dev.to/nagatodev/how-to-connect-flask-to-reactjs-1k8i</p>


<h2>To run just the backend Scripts:</h2>
<p>open mainTest.py and change the input variable</p>
<p>comment out all flask/api related lines in main.py (11-15 & 191-208) </p>
<p>run mainTest.py</p>
