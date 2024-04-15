# Enhancing Bot Responses in Rasa


### Text Responses

**From `domain.yml`**
```
responses:
  utter_greet:
    - text: "Greetings and Welcome! May I know your name please? 😊"
```

**From `actions.py`**
```
dispatcher.utter_message(text = "Greetings and Welcome! May I know your name please? 😊")
```


### Button Responses

**From `domain.yml`**
```
responses:

  utter_greet:
    - text: "Hello! Nice to have you {name}. What can I do for you?"
      buttons:  
        - title: "About Us"
          payload: "about us"
        - title: "Our Products"
          payload: "Our Products"
        - title: "Track Order"
          payload: "track order"
        - title: "Contact Us"
          payload: "contanct us"
```

**From `actions.py`**
```
button_response = [
    {"title": "About Us", "payload": "about us"},
    {"title": "Our Products", "payload": "our products"},
    {"title": "Track Order", "payload": "track order"},
    {"title": "Contact Us", "payload": "contanct us"}
  ]

dispatcher.utter_message(text="Hello! Nice to have you {name}. What can I do for you?", buttons = button_response)
```


### Quick Reply Responses

**From `domain.yml`**
```
responses:

  utter_cuisine:
    - text: "Please Choose a Cuisine"
      custom:
        payload: quickReplies
        data:
          - title: "North Indian"
            payload: "north indian"
          - title: "South Indian"
            payload: "south indian"
          - title: "Chinese"
            payload: "chinese"
          - title: "Italian"
            payload: "italian"
```

**From `actions.py`**
```
data = [
    {"title": "North Indian", "payload": "north indian"},
    {"title": "South Indian", "payload": "south indian"},
    {"title": "Chinese", "payload": "chinese"},
    {"title": "Italian", "payload": "italian"}
  ]

message = {"payload": "quickReplies", "data": data}

dispatcher.utter_message(text="Please Choose a Cuisine", json_message = message)
```


### Dropdown Responses

**From `domain.yml`**
```
responses:
  utter_menu:
    - text: "Please Select a Dish"
      custom:
        payload: dropDown
        data:
          - label: ""
            value: "Option 1"
          - label: "Option 2"
            value: "Option 2"
          - label: "Option 3"
            value: "Option 3"
```

**From `actions.py`**
```
data = [
    {"label": "Option 1", "value": "Option 1"},
    {"label": "Option 2", "value": "Option 2"},
    {"label": "Option 3", "value": "Option 3"}
  ]

message = {"payload": "dropDown", "data": data}

dispatcher.utter_message(text="Please select an option", json_message = message)
```

### Collapsible Responses

**From `domain.yml`**
```
responses:
  utter_askLeaveTypes:
    - text: "You can apply for the following types of leaves"
      custom:
        payload: "collapsible"
        data:
          - title: "Sick Leave"
            description: "Time off from work for health and safety needs without losing pay."
          - title: "Earned Leave"
            description: "Leaves earned in the previous year and enjoyed in the following years."
          - title: "Casual Leave"
            description: "Granted for unforeseen situations or personal matters for one or two days."
          - title: "Flexi Leave"
            description: "Optional leave that can be applied for directly in the system at least a week before."
```

**From `actions.py`**
```
data = [
    {"title": "Sick Leave", "description": "Time off from work for health and safety needs without losing pay."},
    {"title": "Earned Leave", "description": "Leaves earned in the previous year and enjoyed in the following years."},
    {"title": "Casual Leave", "description": "Granted for unforeseen situations or personal matters for one or two days."},
    {"title": "Flexi Leave", "description": "Optional leave that can be applied for directly in the system at least a week before."}
  ]

message = {"payload": "collapsible", "data": data}

dispatcher.utter_message(text="You can apply for the following types of leaves", json_message = message)
```

### Image Responses

**From `domain.yml`**
```
responses:
  utter_image:
    - text: "I've found an adorable dog image for you!"
      image: "static/img/Labrador Retriever.jpeg"
```

**From `actions.py`**
```
dispatcher.utter_message(text = "I've found an adorable dog image for you!", image = "static/img/Labrador Retriever.jpeg")
```


### Video Responses

**From `domain.yml`**
```
responses:
  utter_video:
    - text: "Presinting Revitalizing Video Reatring Amazon Forest."
      attachment: {"type":"video", "payload":{"title":"Amazon Forest","src":"https://www.youtube.com/watch?v=jOUPAMyOPl0"}}
```

**From `actions.py`**
```
msg = {"type":"video", "payload":{"title":"Amazon Forest","src":"https://www.youtube.com/watch?v=jOUPAMyOPl0"}}

dispatcher.utter_message(text= "Presinting Revitalizing Video Reatring Amazon Forest.", attachment = msg)
```


### Card Carousel Response

**From `domain.yml`**
```
responses:
  utter_cardsCarousel:
    - text: "I have following suggestions for you."
      custom:
        payload: cardsCarousel
        data:
          - image: "/static/img/Leh.jpg"
            title: "Leh"
            description: "<a href='https://www.makemytrip.com/tripideas/places/manali' target='_blank'>Click to View Details</a>"
          - image: "/static/img/Manali.jpg"
            title: "Manali"
            description: "<a href='https://www.makemytrip.com/tripideas/places/leh' target='_blank'>Click to View Details</a>"
          - image: "/static/img/Mussoorie.jpg"
            title: "Mussoorie"
            description: "<a href='https://www.makemytrip.com/tripideas/places/mussoorie' target='_blank'>Click to View Details</a>"
          - image: "/static/img/Ooty.jpg"
            title: "Ooty"
            description: "<a href='https://www.makemytrip.com/tripideas/places/ooty' target='_blank'>Click to View Details</a>"
          - image: "/static/img/Srinagar.jpg"
            title: "Srinagar"
            description: "<a href='https://www.makemytrip.com/tripideas/places/srinagar' target='_blank'>Click to View Details</a>"
```

**From `actions.py`**
```
data = {
    "payload": 'cardsCarousel',
    "data": [{"image": "/static/img/Leh.jpg","title": "Leh","description": "<a href='https://www.makemytrip.com/tripideas/places/manali' target='_blank'>Click to View Details</a>"},
             {"image": "/static/img/Manali.jpg","title": "Manali","description": "<a href='https://www.makemytrip.com/tripideas/places/leh' target='_blank'>Click to View Details</a>"},
             {"image": "/static/img/Mussoorie.jpg","title": "Mussoorie","description": "<a href='https://www.makemytrip.com/tripideas/places/mussoorie' target='_blank'>Click to View Details</a>"},
             {"image": "/static/img/Ooty.jpg","title": "Ooty","description": "<a href='https://www.makemytrip.com/tripideas/places/ooty' target='_blank'>Click to View Details</a>"},
             {"image": "/static/img/Srinagar.jpg","title": ""Srinagar"","description": "<a href='https://www.makemytrip.com/tripideas/places/srinagar' target='_blank'>Click to View Details</a>"}
             ]
  }

dispatcher.utter_message(text = "I have following suggestions for you.", json_message = data)
```


### PDF Attachment Response

**From `domain.yml`**
```
responses:
  utter_pdf:
    - text: "I have found a Novel for you."
      custom:
        payload: pdf_attachment
        title: "The Secret"
        url: "http://192.168.20.106:30001/static/files/The%20Secret.pdf"
```

**From `actions.py`**
```
data = {
    "payload": "pdf_attachment",
    "title": "The Secret",
    "url": "http://192.168.20.106:30001/static/files/The%20Secret.pdf"
  }

dispatcher.utter_message(text = "I have found a Novel for you.", json_message = data)
```

### Chart Responses

**From `domain.yml`**
```
responses:
  utter_chart:
    - text: "Your Leave Balance Details"
      custom:
        payload: chart
        data:
          title: "Leaves"
          labels:
            - "Sick Leave"
            - "Casual Leave"
            - "Earned Leave"
            - "Flexi Leave"
          backgroundColor:
            - "#36a2eb"
            - "#ffcd56"
            - "#ff6384"
            - "#009688"
          chartsData:
            - 5
            - 10
            - 22
            - 3
          chartType: "pie"
          displayLegend: 'true'
```

**From `actions.py`**
```
data = {
    "title": "Leaves",
    "labels": ["Sick Leave", "Casual Leave", "Earned Leave", "Flexi Leave"],
    "backgroundColor": ["#36a2eb", "#ffcd56", "#ff6384", "#009688"],
    "chartsData": [5, 10, 22, 3],
    "chartType": "pie",
    "displayLegend": "true"
  }

message = {"payload": "chart", "data": data}

dispatcher.utter_message(text = "Your Leave Balance Details", json_message = message)
```


### Location Access Response

**From `domain.yml`**
```
responses:
  utter_ask_location:
    - text: "Sure, Please allow me to access your location 🧐."
      custom:
        payload: location
```

**From `actions.py`**
```
message = {"payload": "location"}

dispatcher.utter_message( text = "Sure, Please allow me to access your location 🧐"., json_message = message)
```