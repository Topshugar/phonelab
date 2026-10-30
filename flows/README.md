# Flows

JSON test flows for PhoneLab.

## Location
flows/ - All flow JSON files go here. python_controller/farm.py reads them.

## Format
{
  "flow": "login_flow",
  "steps": [
    { "action": "tap", "x": 500, "y": 800 },
    { "action": "swipe", "from": [500, 1000], "to": [500, 200] },
    { "action": "wait", "seconds": 2 },
    { "action": "screenshot", "name": "result" }
  ]
}

## Actions
- tap - x, y
- swipe - from, to
- wait - seconds
- screenshot - name[x][y]

## Run
python python_controller/farm.py --test flows/login_flow.json

## Output
- Videos -> ./recordings/
- Reports -> ./recordings/
- Logs -> ./reports/