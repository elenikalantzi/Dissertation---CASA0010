## An integrated Land-Use Transport-Interaction model for predicting transport patterns and urban activities applied to the case study of Attica Region.
Eleni Kalantzi <br />
23/08/21 <br />
This GitHub repository contains the code used for the dissertation of the MSc in Smart Cities and Urban Analytics at CASA UCL. The following descriptions explain the way each file functions in order to create a working model. <br />
**Note:** This repository does not include the data used in the model as it is not open data and must not be publicly available. <br />
### File Description
1) **main.py** <br />
This workbook contains the main code that runs in order to generate the model results. <br />

2) **globals.py** <br />
This workbook reads all the data used to build the model.<br />

3) **quantlhmodel.py** <br />
This workbook is based on Lakshmanan's and Hansen's retail model and contains the functions used as a base for the main code.<br />

4) **analytics.py** <br />
This workbook produces analytic data for debugging and visualisation.<br />

5) **LUTI_API.py** <br />
This workbook contains accessor functions for getting probabilities of trips from workplaces to residential zones and creates Geojson files with flows for visualisation.<br />

6) **utils.py** <br />
This workbook contains data building utilities.<br />
