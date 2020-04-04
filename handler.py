import json
import random


def hello(event, context):
    body = {
        "message": "Hello Code + Coffee Lovers <3",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def coffeeOfDay(event, context):
    coffees = [ 
                "dark roast",
                "medium roast",
                "light roast",
                "decaf",
                "half calf",
                "java"
              ]
   
    try:
        name = event['queryStringParameters']['name']
    except:
        name = "You"

    todaysCoffee = f"Hey {name} Today's coffee is {random.choice(coffees)}"

    body = {
        "message": "Hello Code + Coffee Lovers <3",
        "coffeeOfTheDay": todaysCoffee
    }


    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def upcomingEvents(event, context):
    events = {
                "event_1": {
                    "event_name": "Python API's pt. 2",
                    "event_date": "April 18",
                    "event_host": "Joe T. and Nicole Z.",
                    "event_location": "https://twitch.tv/mastermndio"
                }
             }
   
    body = {
        "message": "Hello Code + Coffee Lovers <3, Here are upcoming Events!",
        "Upcoming Events": events
    }


    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
