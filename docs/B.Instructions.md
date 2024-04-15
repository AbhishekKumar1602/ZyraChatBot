# Instructions

## Setup Instructions

### Installation Procedure 

1. **Install Python and PIP**
```
sudo apt update && sudo apt install python3 python3-venv python3-pip
```

2. **Create and Activative Python Virtual Environment**
- Create a Python Virtual Environment in the directory where you want to install RASA And Activate it.
```
python3 -m venv ./VE_Name && source VE_Name/bin/activate
```

3. **Install and Initalize RASA**
- In the same directory where python virtual environment is present install and initialize RASA
```
pip3 install rasa && rasa init
```
- Please enter a path where the project will be created [default: current directory]: Press Entre Key
- Directory '/home/expadmin/Downloads' is not empty. Continue? (Y/n): Y
- Do you want to train an initial model? 💪🏽 (Y/n) : n


### Basic Configration
1. While using RASA Action Server for RASA SDK (actions.py) uncomment the following line in endpoints.yml
```
action_endpoint:
 url: "http://localhost:5055/webhook"
```
 **NOTE**: Ensure to modify the port if the RASA Action Server is running on a different port.


### Basic RASA Commands
1. **Train Model**
```
rasa train
```

2. **Start RASA Core Server with Trained Model**
```
rasa run
```
- On Specific Port
```
rasa run --port [port_number]
```
**`NOTE`**: Default Port: 5005

3. **Start RASA Action Server Using the Rasa SDK.**
```
rasa run actions	
```
- On Specific Port
```
rasa run actions --port [port_number]
```
**`NOTE`**: Defrault Port: 5055

4. **Load Trained Model and Talk to Bot on the Command Line.**
```
rasa shell
```
- On Specific Port
```
rasa shell -p port_number
```
**`NOTE`**: Default Port: 5005  
- To close the Chat Enter "/stop" in Response.

## Integration Instructions

**Ensure Rasa Setup on Your System or Server.**

### Procedure:

**Step 1**: Enable communication between this Chat UI and the Rasa server via the rest channel. Update the credentials.yml file to include the rest channel.

**Step 2**: When ready to integrate your bot with the UI, initiate the Rasa server using the following command:
```
rasa run -m models --enable-api --cors "*" --debug
```
**Step 3**: If you have custom actions, launch the action server with the command:
```
rasa run actions --cors "*" --debug
```
**Step 4**: For Rasa Server hosted remotely (e.g., on an EC2 instance), modify the "constants.js" by replacing "localhost" with the public IP address of the server.

**Step 5**: Once the Rasa Server is operational, test the bot by executing the app.py file using the following command:
```
python3 app.py
```

## Asynchronous Actions
Implementing asynchronous (async) actions in Rasa enhances the efficiency of your assistant, particularly when dealing with concurrent tasks or time-consuming operations. Follow these steps to seamlessly integrate async actions into your Rasa assistant:

1. **Install Required Libraries**
- Ensure that the necessary libraries are present by running:
```
pip install rasa-sdk[async]
```
2. **Update Your Action Code**
- Modify custom action code to make it asynchronous. Here's an example using Python's asyncio library:

    **# actions.py**
```
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class MyCustomAction(Action):
    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Your async logic goes here
        result = await self.async_operation()

        # Dispatch the result to the user
        dispatcher.utter_message(text=f"Async result: {result}")

        return []
    
    async def async_operation(self) -> Any:
        # Perform your asynchronous operation here e.g., call an external API, database operation, etc.
        return "Async operation completed!"
```

3. **Enable Async Mode in Rasa**
- Ensure  Rasa Server is Configured for Async Mode. Update `endpoints.yml` File With:
```
action_endpoint:
  url: "http://localhost:5055/webhook"
  wait_time_between_pulls: 2
  max_retries: 6
```

4. **Run Rasa Server**
- Start Rasa Server with Async Support.
```
rasa run --enable-api --cors "*" --debug --port portNumber
```

5. **Test Async Action**
- Trigger the conversation that calls the async action, and observe the improved efficiency, especially under high loads.