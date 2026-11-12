import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def load_events():
    file_path = BASE_DIR / "data" / "events.json"

    with open(file_path, "r", encoding="utf-8") as file:
        events = json.load(file)

    return events

events = load_events()

def classify_events(events): 
    quarterly_events = events["quarterly_events"]
    ongoing_events = events["ongoing_events"]
    return quarterly_events, ongoing_events

eventclass = classify_events(events)
quarterly_events = eventclass[0]
ongoing_events = eventclass[1]

def listmaking(quarterly_events, ongoing_events):
    quarterly_event_list = []
    ongoing_event_list = []
    pass

def final_event_probability(events):
    pass
