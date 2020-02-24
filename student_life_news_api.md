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


### **News**

Get the news around campus.

- **URL**

  /news

- **Method:**

  `GET` & `POST`

- **Success Response:**

  - **Code:** 200
    **Content:** 

    ```json
    [
	    {
		     "_id": "5e542cc331d968366ab3f416",
		     "body": "Drop-in academic advising during lunch hours in the Goldberg rm141",
		     "comments": [
			     {
				     "body": "What time?",
				     "date": "Mon, 24 Feb 2020 16:54:55 GMT",
				     "user": "Nick"
				 },
			 ],
			 "date": "Mon, 24 Feb 2020 16:06:27 GMT",
			 "title": "Test2",
			 "user": "James"
		},
		{
		     "_id": "5e5438a9bd8079c44a462df0",
		     "body": "Free pizza in the SUB today",
		     "comments": [
			     {
				     "body": "Beverages?",
				     "date": "Mon, 24 Feb 2020 16:57:42 GMT",
				     "user": "Fahmida"
				 },
				 {
				     "body": "Veggie pizza?",
				     "date": "Mon, 24 Feb 2020 16:58:16 GMT",
				     "user": "Dr. Dimatteo"
				 },
				 {
				     "body": "Cheese pizza?",
				     "date": "Mon, 24 Feb 2020 17:01:16 GMT",
				     "user": "Iron Man"
				 }
			 ],
			 "date": "Mon, 24 Feb 2020 16:57:13 GMT",
			 "title": "Test1",
			 "user": "Connor"
		},
	]
    ```

- **Error Response:**

  - **Code:** 405 METHOD NOT ALLOWED

  - **Cause:** Using a HTML method other than GET or POST

    **Content:**

    ```html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>405 Method Not Allowed</title>
    <h1>Method Not Allowed</h1>
    <p>The method is not allowed for the requested URL.</p>
    ```

  OR

  - **Code:** 400 BAD REQUEST

  - **Cause:** Trying to post news with too many fields

    **Content:**

    ````html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>400 Bad Request</title>
    <h1>Bad Request</h1>
    <p>Too many fields in entry.</p>
    ````
  
  OR

  - **Code:** 400 BAD REQUEST

  - **Cause:** Trying to post news of type: None

    **Content:**

    ````html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>400 Bad Request</title>
    <h1>Bad Request</h1>
    <p>'Error: None type is not acceptable as news.'</p>
    ````
    
    OR

  - **Code:** 400 BAD REQUEST

  - **Cause:** One of the fields of the entry is missing

    **Content:**

    ````html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>400 Bad Request</title>
    <h1>Bad Request</h1>
    <p>'Field 'body', 'user', or 'title' not found.'</p>
    ````

	OR

  - **Code:** 400 BAD REQUEST

  - **Cause:** 'body' field is the wrong type

    **Content:**

    ````html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>400 Bad Request</title>
    <h1>Bad Request</h1>
    <p>'Error: 'body' of entry is not of valid type.'</p>
    ````
    
	OR

  - **Code:** 400 BAD REQUEST

  - **Cause:** 'user' field is the wrong type

    **Content:**

    ````html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>400 Bad Request</title>
    <h1>Bad Request</h1>
    <p>'Error: 'user' of entry is not of valid type.'</p>
    ````
    
	OR

  - **Code:** 400 BAD REQUEST

  - **Cause:** 'title' field is the wrong type

    **Content:**

    ````html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>400 Bad Request</title>
    <h1>Bad Request</h1>
    <p>'Error: 'title' of entry is not of valid type.'</p>
    ````

- **Sample Call:**

  ```javascript
    $.ajax({
      url: "/news",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```


### **News by ID**

Get a certain entry of news around campus.

- **URL**

  /news

- **Method:**

  `GET` & `Delete` & `PUT`

- **Success Response:**

  - **Code:** 200
    **Content:** 

    ```json
	{
		"_id": "5e542cc331d968366ab3f416",
		"body": "Drop-in academic advising during lunch hours in the Goldberg rm141",
		"comments": [
			{
				"body": "What time?",
				"date": "Mon, 24 Feb 2020 16:54:55 GMT",
				"user": "Nick"
			},
		],
		"date": "Mon, 24 Feb 2020 16:06:27 GMT",
		"title": "Test2",
		"user": "James"
	}
    ```

	OR

	- **Code:** 200
	   **Content:** 
    
	```
	Delete Successful
	```
	
	OR

	- **Code:** 200
	   **Content:** 
    
	```
	Comment successful
	```


- **Error Response:**

  - **Code:** 405 METHOD NOT ALLOWED

  - **Cause:** Using a HTML method other than GET, DELETE, or PUT

    **Content:**

    ```html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>405 Method Not Allowed</title>
    <h1>Method Not Allowed</h1>
    <p>The method is not allowed for the requested URL.</p>
    ```

  OR

  - **Code:** 404 NOT FOUND

  - **Cause:** Could not find a news entry with given id

    **Content:**

    ````html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>400 Bad Request</title>
    <h1>Bad Request</h1>
    <p>Error: No news exists with the given id.</p>
    ````
  
  OR

  - **Code:** 400 BAD REQUEST

  - **Cause:** Trying to post comment of type: None

    **Content:**

    ````html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>400 Bad Request</title>
    <h1>Bad Request</h1>
    <p>'Error: None type is not an acceptable comment.'</p>
    ````
    
    OR

  - **Code:** 400 BAD REQUEST

  - **Cause:** One of the fields of the entry is missing

    **Content:**

    ````html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>400 Bad Request</title>
    <h1>Bad Request</h1>
    <p>'Error: Field 'user' or 'body' not found.'</p>
    ````

	OR

  - **Code:** 400 BAD REQUEST

  - **Cause:** 'user' field is the wrong type

    **Content:**

    ````html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>400 Bad Request</title>
    <h1>Bad Request</h1>
    <p>'Error: 'user' of entry is not of valid type.'</p>
    ````
    
	OR

  - **Code:** 400 BAD REQUEST

  - **Cause:** 'body' field is the wrong type

    **Content:**

    ````html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>400 Bad Request</title>
    <h1>Bad Request</h1>
    <p>'Error: 'body' of entry is not of valid type.'</p>
    ````
    
	OR

  - **Code:** 400 BAD REQUEST

  - **Cause:** Comment entry has too many fields

    **Content:**

    ````html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>400 Bad Request</title>
    <h1>Bad Request</h1>
    <p>'Error: Too many fields in entry.'</p>
    ````

- **Sample Call:**

  ```javascript
    $.ajax({
      url: "/news/65126351284871hgcwa7",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```



