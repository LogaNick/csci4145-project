### **Snow Day Prediction**

Get the percent probability (an integer) that tomorrow will be a snowday given a valid Canadian Postal Code without spaces. If tomorrow is not a school day, the response will be -1.  

- **URL**

  /snowday/<postal_code>

- **Method:**

  `GET`

- **Success Response:**

  - **Code:** 200
    **Content:** 

    ```javascript
    43
    ```

- **Error Response:**

  - **Code:** 405 METHOD NOT ALLOWED

  - **Cause:** Using a HTML method other than GET 

    **Content:**

    ```html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>405 Method Not Allowed</title>
    <h1>Method Not Allowed</h1>
    <p>The method is not allowed for the requested URL.</p>
    ```

  OR

  - **Code:** 400 BAD REQUEST

  - **Cause:** Making a query with an invalid postal code

    **Content:**

    ````html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>400 Bad Request</title>
    <h1>Bad Request</h1>
    <p>Postal Code is not valid.</p>
    ````

- **Sample Call:**

  ```javascript
    $.ajax({
      url: "/snowday/B3H3H4",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```

### **Weather**

Get the weather forecast summary for a specific day. Any date within the next 16 days can be forecasted. This requires the YYYY-MM-DD input format.

- **URL**

  /weather/<date_string>

- **Method:**

  `GET`

- **Success Response:**

  - **Code:** 200
    **Content:** 

    ```json
    {
      "daily": {
        "data": [
          {
            "apparentTemperatureHigh": 12.85, 
            "apparentTemperatureHighTime": 1599674760, 
            "apparentTemperatureLow": 7.32, 
            "apparentTemperatureLowTime": 1599726960, 
            "apparentTemperatureMax": 12.85, 
            "apparentTemperatureMaxTime": 1599674760, 
            "apparentTemperatureMin": 7.47, 
            "apparentTemperatureMinTime": 1599640560, 
            "cloudCover": 0.61, 
            "cloudCoverError": 0.36, 
            "dewPoint": 6.93, 
            "dewPointError": 9.66, 
            "humidity": 0.78, 
            "moonPhase": 0.74, 
            "pressure": 1015.8, 
            "pressureError": 6.6, 
            "sunriseTime": 1599644880, 
            "sunsetTime": 1599691020, 
            "temperatureHigh": 13.13, 
            "temperatureHighError": 9.93, 
            "temperatureHighTime": 1599674760, 
            "temperatureLow": 8.63, 
            "temperatureLowError": 9.92, 
            "temperatureLowTime": 1599726840, 
            "temperatureMax": 13.13, 
            "temperatureMaxError": 9.94, 
            "temperatureMaxTime": 1599674760, 
            "temperatureMin": 8.74, 
            "temperatureMinError": 9.93, 
            "temperatureMinTime": 1599640440, 
            "time": 1599620400, 
            "uvIndex": 5, 
            "uvIndexTime": 1599667800, 
            "windBearing": 106, 
            "windBearingError": 32, 
            "windSpeed": 12.43, 
            "windSpeedError": 7.36
          }
        ]
      }, 
      "latitude": 44.64249, 
      "longitude": -63.5718, 
      "offset": -3, 
      "timezone": "America/Halifax"
    }
    ```

- **Error Response:**

  - **Code:** 405 METHOD NOT ALLOWED

  - **Cause:** Using a HTML method other than GET 

    **Content:**

    ```html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>405 Method Not Allowed</title>
    <h1>Method Not Allowed</h1>
    <p>The method is not allowed for the requested URL.</p>
    ```

  OR

  - **Code:** 400 BAD REQUEST

  - **Cause:** Making a query with an incorrect date format

    **Content:**

    ````html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>400 Bad Request</title>
    <h1>Bad Request</h1>
    <p>The specified date format was incorrect (should be YYYY-MM-DD).</p>
    ````
  
  OR

  - **Code:** 400 BAD REQUEST

  - **Cause:** Making a query with an out-of-range date

    **Content:**

    ````html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>400 Bad Request</title>
    <h1>Bad Request</h1>
    <p>'The specified date format was outside of the 16 day range.'</p>
    ````

- **Sample Call:**

  ```javascript
    $.ajax({
      url: "/weather/2020-02-25",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```



