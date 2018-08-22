# Bus System Project
## A data logging prototype for buses trips for a better public transportation
###                               (implemented in a Raspberry Pi 2)

This is the code for my final paper - bachelor's thesis required in order to obtain my B.S. degree in Control and Automation.

This project uses the following features:
- Python
- Django
- Django Rest Framework
- React (Transpilled to ES5)
- Google API
- JavaScript
- jQuery


The project comprehended a in depth analysis of the problems that the public transportation in Brazil is currently facing - such as a decrease in number of users of 17% in the past 4 years. The paper also contrats both scenarios found in US and Europe (Western and Central) with the Brazilian (mostly Sorocaba, my hometown) scenario.

In order to design the features and understanding better the final user requirements and perception, the foundation paper used was the **Passengers' Perception of and Behavioral Adaptation to Unreliability in Public Transportation**, by *Carrel et al* (2013). This paper covers what are the causes of public transport users rejection towards buses, as well as the improvements factors.

Therefore, this project focused in developing a prototype that could be implemented in a real bus, focusing in the following:
1. Data logging;
2. A public JSON API of the vehicle and the stops;
3. Time prediction with Google Maps;
4. Significative improvements in the communication between the vehicle/bus, service provider and final user.

**This project obtained a score of:10/10**

It is important to notice that the score does not takes into account how well the code was written, but rather the final result.

## My review about this project - code wise:
1. I should've avoided Django and React - it was a simple webserver/interface and I overkilled it:
   - Django: Too many unused features: Auth, Session and also middlewares. I would have swapped to Flask;
   - React: Same as above. However, I decided to go for React as I'd like to make a quite modular interface with different components and being able to treat them independently, and mostly being able to refresh different components without bothering the full page. Could have done with vanilla JavaScript. Besides, the fact that Django+React requires a significative number of plugins (webpack, babel rc etc) is quite unfortunate for such a simple project.
2. I must comment more - I think I ended with a enormous number of helper functions which will be hard to make any maintenance;
3. Google Maps does the work, but it is not a flawless feature;
4. Should have wrote better DAO files in order to built a better and less redundant code.

I didn't have much time (2 months while working full time) to develop a quite big system and research - so I ended up with a more functional system rather than clean and good written. Put a lot of thought into what were my main mistakes in a speeded project and I'd like to keep these marked here. 
   
## Setup:
==============================

*npm install (requires node)

*pip install -r requirements.txt (requires python/pip)

*./node_modules/.bin/webpack --config webpack.config.js OR the created webpack script: "npm run build"

*python manage.py runserver (runs the server)

*you will need to setup the coordinates and auxiliary .txt files by yourself.

==============================
