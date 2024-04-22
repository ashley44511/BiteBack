<h1>Hello! Welcome to BiteBack. This full-stack project aims to improve the nutrition choices of our users.</h1>

<p>Proposal: https://docs.google.com/document/d/1n-0uhMOCrZ74qeJcQnSx6GGP20M0qRgrIPWWQG3i-1M/edit?usp=sharing</p>
<p>Planning: https://docs.google.com/document/d/16jeHNHj802-zguv49YW67QjcspoXpWC0BTI9WfnULJI/edit?usp=sharing</p>
<p>Data sources: https://think.cs.vt.edu/corgis/csv/food/ https://think.cs.vt.edu/corgis/python/food/</p>
<p>Final Report: https://docs.google.com/document/d/1uiY8fuBUwxjSFu4GX8bloH63Rh8TuoJourvERnBV6Ac/edit?usp=sharing</p>

<h2>Before running any scripts (especially main.py), please use the following commands:</h2>
<p>cd bite-back-project</p>
<p>cd flask_react</p>
<p>cd backend</p>
<p>For mac/unix users: python3 -m venv env</p>
<p>For windows users: py -m venv env</p>
<p>For mac/unix users: source env/bin/activate</p>
<p>For windows users: .\env\Scripts\activate</p>
<p>pip install flask python-dotenv plotly pandas flask_cors kaleido</p>

<p>cd bite-back-project</p>
<p>cd flask_react</p>
<p>npm install</p>


<h2>To run for the first time after cloning:</h2>
<h4>Open a new terminal.</h4>
<p>cd bite-back-project</p>
<p>cd flask_react</p>
<p>npm install</p>
<p>npm start</p>
<h4>The frontend should now be set up. Open another terminal.</h4>
<p>cd bite-back-project</p>
<p>cd flask_react</p>
<p>cd backend</p>
<h4>Create a virtual environment.</h4>
<p>For mac/unix users: python3 -m venv env</p>
<p>For windows users: py -m venv env</p>
<h4>Activate the virtual environment. When restarting the project, you only need to activate from now on.</h4>
<p>For mac/unix users: source env/bin/activate</p>
<p>For windows users: .\env\Scripts\activate</p>
<p>pip install flask python-dotenv plotly pandas flask_cors kaleido</p>
<p>flask run</p>
<h4>The backend is now running, and the submit button on the website will now work.</h4>


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
