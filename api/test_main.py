from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

null = None


def test_read_all_jokes():
    response = client.get("/jokes")
    assert response.status_code == 200
    assert response.json() == {
        "data": [
            {
                "id": 20,
                "prompt": "How do you say 'Yes, I would like some' in Spanish?",
                "reply": {
                    "first": "Si..",
                    "second": "(quickly interupt), see deez nuts!",
                },
            },
            {
                "id": 1,
                "prompt": "How much did your trip to Dubai cost?",
                "reply": {
                    "first": "It was pretty expensive.",
                    "second": "To buy deez nuts!",
                },
            },
            {
                "id": 2,
                "prompt": "Excuse me but do you like Wendys?",
                "reply": {
                    "first": "Yes why?",
                    "second": "Because you are going to love when deez nuts hit you in the face.",
                },
            },
            {
                "id": 3,
                "prompt": "Excuse me but do you Bofa?",
                "reply": {
                    "first": "Bofa? I don't think so?",
                    "second": "Bofa deez nuts!",
                },
            },
            {
                "id": 4,
                "prompt": "Hey, are you familar with Landon?",
                "reply": {
                    "first": "Landon who?",
                    "second": "Slip, fall then landon deez nuts.",
                },
            },
            {
                "id": 5,
                "prompt": "Do you remember that guy Willya?",
                "reply": {
                    "first": "Willya who?",
                    "second": "Willya put deez nuts on your chin.",
                },
            },
            {
                "id": 6,
                "prompt": "Hi there, I heard that you are a huge fan of Dee.",
                "reply": {"first": "Dee who?", "second": "Deez nuts!"},
            },
            {
                "id": 7,
                "prompt": "Excuse me but do you like pudding?",
                "reply": {
                    "first": "Yes, of course.",
                    "second": "Well how about pudding deez nuts in your mouth.",
                },
            },
            {
                "id": 8,
                "prompt": "Do you enjoy parodies?",
                "reply": {
                    "first": "Sure, why?",
                    "second": "Well how about you enjoy a pair of deez nuts on your chin.",
                },
            },
            {
                "id": 9,
                "prompt": "Have you seen the film Bofa?",
                "reply": {"first": "Bofa? Who is in it?", "second": "Bofa deez nuts."},
            },
            {
                "id": 10,
                "prompt": "Have you met my friend Phillip?",
                "reply": {"first": "Phillip who?", "second": "Phillip on deez nuts."},
            },
            {
                "id": 11,
                "prompt": "Hey there buddy, I have a bunch of old albums, would you like 2 cd's?",
                "reply": {"first": "Sure, thanks!", "second": "To see deez nutz."},
            },
            {
                "id": 12,
                "prompt": "Do you like Imagine Dragons?",
                "reply": {
                    "first": "Yeah sure.",
                    "second": "Imagine dragging deez nuts over your head.",
                },
            },
            {
                "id": 13,
                "prompt": "Do you know who is coming to our party later on?",
                "reply": {
                    "first": "Yeah Dee is.",
                    "third": "Deez nuts!",
                    "second": "Dee who?",
                },
            },
            {
                "id": 14,
                "prompt": "Have you considered leaving?",
                "reply": {
                    "first": "Leaving what?",
                    "second": "Leaving deez nuts in your mouth.",
                },
            },
            {
                "id": 15,
                "prompt": "Knock knock.",
                "reply": {
                    "first": "Who's there?",
                    "third": "Dee who?",
                    "fourth": "Deez nuts!",
                    "second": "Dee.",
                },
            },
            {
                "id": 16,
                "prompt": "I think you should be a goblin this halloween.",
                "reply": {
                    "first": "A goblin? Why is that?",
                    "second": "Goblin bofa deez nuts.",
                },
            },
            {
                "id": 22,
                "prompt": "Do you like Vanessa Paradis?",
                "reply": {
                    "first": "Yeah sure.",
                    "second": "How about a pair of deez nuts.",
                },
            },
            {
                "id": 23,
                "prompt": "Have you heard about this new breed of bunnies that have been emerging all over town?",
                "reply": {
                    "first": "Oh really?",
                    "third": "Slaw Bunnies? What are they?",
                    "fourth": "Slob on Deez Nuts.",
                    "second": "Yes, they are called Slaw Bunnies.",
                },
            },
            {
                "id": 17,
                "prompt": "Do you prefer the Yankees or the Expos?",
                "reply": {"first": "The Yankees.", "second": "Yank on deez nuts!"},
            },
            {
                "id": 18,
                "prompt": "Hey do you like Chef Boyardee?",
                "reply": {
                    "first": "I like their canned pasta.",
                    "second": "Chef BoyAreDeez nuts tasty!",
                },
            },
            {
                "id": 19,
                "prompt": "Do you know the new rapper Willya?",
                "reply": {
                    "first": "Willya who?",
                    "second": "Willya put deez nuts in your mouth.",
                },
            },
            {
                "id": 24,
                "prompt": "Have you heard about the news in Kenya today?",
                "reply": {
                    "first": "No, tell me more.",
                    "second": "Well, Kenya fit deez nuts in your mouth.",
                },
            },
            {
                "id": 25,
                "prompt": "In all your subjects I am giving you D's.",
                "reply": {
                    "first": "Well I am also going to be giving you D's.",
                    "third": "Deez nuts!",
                    "second": "What do you mean?",
                },
            },
            {
                "id": 26,
                "prompt": "Have you played that Xbox game 'Sea Of Thieves'?",
                "reply": {
                    "first": "Yes why?",
                    "second": "Well Sea Of Thieves Nuts fit in your mouth.",
                },
            },
            {
                "id": 27,
                "prompt": "I was shopping at the local farmers market and purchased some fermented succondese.",
                "reply": {
                    "first": "Fermented succondese?",
                    "second": "Yeah, fermented succondese nuts.",
                },
            },
            {
                "id": 28,
                "prompt": "I am so sick of this, it sucks!",
                "reply": {"first": "What sucks?", "second": "You suck on deez nuts."},
            },
            {
                "id": 29,
                "prompt": "Hey Mike, is Phil there?",
                "reply": {"first": "Phil who?", "second": "Fill up on deez nuts!"},
            },
            {
                "id": 30,
                "prompt": "Have you seen Dr. Botha?",
                "reply": {
                    "first": "Who's Dr. Botha?",
                    "second": "Botha deez nuts in your mouth!",
                },
            },
            {
                "id": 31,
                "prompt": "Excuse me but do you know Candice?",
                "reply": {
                    "first": "Candice who?",
                    "second": "Candice set of nuts fit in your mouth?",
                },
            },
            {
                "id": 32,
                "prompt": "How do you pronounce amoood spelled backwards?",
                "reply": {
                    "first": "Uhhh...doooma?",
                    "second": "Do my balls fit in ya mouth?",
                },
            },
            {
                "id": 33,
                "prompt": "My girlfriend Jenny got diagnosed with DN",
                "reply": {
                    "first": "Oh, man, sorry. What's DN?",
                    "second": "Deez nuts!",
                },
            },
            {
                "id": 34,
                "prompt": "I can't believe that Sophia speaks Ligondese.",
                "reply": {"first": "Ligondese?", "second": "Yeah, Lick on deez nuts!"},
            },
            {
                "id": 35,
                "prompt": "Do you like tulips?",
                "reply": {
                    "first": "Sure, why?",
                    "second": "Because you are going to love your two lips on deez nuts!",
                },
            },
            {
                "id": 36,
                "prompt": "Are you planning to go to SAWCON this year?",
                "reply": {
                    "first": "SAWCON? What's that?",
                    "second": "Suck on deez nuts!",
                },
            },
            {
                "id": 37,
                "prompt": "You need to shut up before you end up like Ken",
                "reply": {
                    "first": "Ken, who?",
                    "second": "Can deez nuts fit in your mouth?",
                },
            },
            {
                "id": 38,
                "prompt": "Have you heard of E10, that new space ship?",
                "reply": {"first": "E10? No.", "second": "Eating deez nuts!"},
            },
            {
                "id": 39,
                "prompt": "Did you hear about what happened in Norway?",
                "reply": {
                    "first": "No, what happened?",
                    "second": "Norway deez nuts can fit in your mouth.",
                },
            },
            {
                "id": 40,
                "prompt": "Have you heard of the Sugondese transfer student?",
                "reply": {
                    "first": "Sugondese transfer student?",
                    "second": "Suck on deez nuts!",
                },
            },
            {
                "id": 41,
                "prompt": "You ever played wipe sumo?",
                "reply": {
                    "first": "What's wipe sumo?",
                    "second": "Wipe some of deez nuts across your face.",
                },
            },
            {
                "id": 42,
                "prompt": "I need you to work on Field E today.",
                "reply": {"first": "What's Field E?", "second": "Feel deez nuts!"},
            },
            {
                "id": 43,
                "prompt": "Have you tried that new burget with the jalapeños?",
                "reply": {
                    "first": "No, what's it called?",
                    "second": "All up in your face with deez nuts!",
                },
            },
            {
                "id": 44,
                "prompt": "What's the name of the current Rusian president?",
                "reply": {
                    "first": "Vladimir Putin.",
                    "second": "Putting deez nuts in your mouth!",
                },
            },
            {
                "id": 45,
                "prompt": "Did you see the news with the South China Sea?",
                "reply": {
                    "first": "No, what happened?",
                    "second": "Trying to see if deez nuts will fit in your mouth!",
                },
            },
            {
                "id": 46,
                "prompt": "What's the male actor in the Penthouse K-Drama?",
                "reply": {"first": "Joo Seok-hoon", "second": "Suck on deez nuts!"},
            },
            {
                "id": 21,
                "prompt": "Dee was asking after you the other day.",
                "reply": {"first": "Who is Dee?", "second": "Deez Nuts!"},
            },
            {
                "id": 47,
                "prompt": "Do you want to head out to get some boba?",
                "reply": {"first": "Yeah sure!", "second": "Both of deez nuts!"},
            },
        ],
        "count": null,
    }


def test_read_all_jokes_max_results():
    response = client.get("/jokes?max_results=5")
    assert response.status_code == 200
    assert response.json() == {
        "data": [
            {
                "id": 20,
                "prompt": "How do you say 'Yes, I would like some' in Spanish?",
                "reply": {
                    "first": "Si..",
                    "second": "(quickly interupt), see deez nuts!",
                },
            },
            {
                "id": 1,
                "prompt": "How much did your trip to Dubai cost?",
                "reply": {
                    "first": "It was pretty expensive.",
                    "second": "To buy deez nuts!",
                },
            },
            {
                "id": 2,
                "prompt": "Excuse me but do you like Wendys?",
                "reply": {
                    "first": "Yes why?",
                    "second": "Because you are going to love when deez nuts hit you in the face.",
                },
            },
            {
                "id": 3,
                "prompt": "Excuse me but do you Bofa?",
                "reply": {
                    "first": "Bofa? I don't think so?",
                    "second": "Bofa deez nuts!",
                },
            },
            {
                "id": 4,
                "prompt": "Hey, are you familar with Landon?",
                "reply": {
                    "first": "Landon who?",
                    "second": "Slip, fall then landon deez nuts.",
                },
            },
        ],
        "count": null,
    }


def test_read_search_jokes():
    response = client.get("/joke/search?keyword=tulip")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 35,
            "prompt": "Do you like tulips?",
            "reply": {
                "first": "Sure, why?",
                "second": "Because you are going to love your two lips on deez nuts!",
            },
        }
    ]


def test_read_search_jokes_bad_query():
    response = client.get("/joke/search?keyword=ben")
    assert response.status_code == 404
    assert response.json() == {"message": "No matches found for 'ben'"}


# TODO
# def test_read_random_jokes():
#     response = client.get("/joke/random")
#     assert response.status_code == 200
#     assert response.json() == {
#         "data": [
#             {
#                 "id": 21,
#                 "prompt": "Dee was asking after you the other day.",
#                 "reply": {"first": "Who is Dee?", "second": "Deez Nuts!"},
#             }
#         ],
#         "count": null,
#     }


def test_read_id_jokes():
    response = client.get("/joke/4")
    assert response.status_code == 200
    assert response.json() == {
        "data": [
            {
                "id": 4,
                "prompt": "Hey, are you familar with Landon?",
                "reply": {
                    "first": "Landon who?",
                    "second": "Slip, fall then landon deez nuts.",
                },
            }
        ],
        "count": null,
    }


def test_read_id_jokes_bad_id():
    response = client.get("/joke/49")
    assert response.status_code == 404
    assert response.json() == {"message": "No joke found with id 49"}
