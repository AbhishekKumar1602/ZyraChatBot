from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests 



class AactionRestartConversation(Action):
    def name(self):
        return 'action_restart_conversation'

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slots_to_clear = ['name']
        events = [SlotSet(slot, None) for slot in slots_to_clear]
        dispatcher.utter_message(response="utter_bot_start_conversation")
        return events


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("I'm sorry, I didn't understand that. Can you please rephrase or provide more information?")
        return []


class ActionLeaveBalance(Action):
    def name(self):
        return 'action_leave_balance'
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        userID = tracker.get_slot("user_id")
        password = tracker.get_slot("password")

        json_data = {
            "User ID": userID,
            "Password": password
        }

        requests.get('http://192.168.10.100/ExpHrmsApi/UserLogin?userid='+json_data.userID+'&password='+password,)

        data = {
                "title": "Leaves",
                "labels": ["Casual Leave", "Privilesed Leave", "Client Visit (OD)", "Leave Without Pay","Donation Leaves","Short Leave","Maternity Leave"],
                "backgroundColor": ["#FF5733","#4CAF50","#3498DB","#FFC300","#E74C3C","#9B59B6","#2ECC71"],
                "chartsData": [8, 10, 25, 88, 2, 9, 7],
                "chartType": "pie",
                "displayLegend": "true"
                }

        message = {"payload": "chart", "data": data}

        dispatcher.utter_message(text="Your Leave Balance Details:", json_message=message)
        
        return []