# Calendar-Maker

API is hosted at PythonAnywhere.

Inspired by <a href="https://calendarsthatwork.com" target="_blank">Calendars That Work</a>

Allows you to create printable calendars in the docx format.

Example (JavaScript)

```
response = await fetch('/make_calendar/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ template:"MonthlyLandscape.docx", year:2020,month:10,day:1,cnt:1,start_day:0})
    })
  ```
