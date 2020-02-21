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

