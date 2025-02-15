import requests
import json

personality = ["extremely friendly", "friendly", "normal", "aggressive", "very aggressive"]


def get_ai_pick(input):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer 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",
            "Content-Type": "application/json",
            "HTTP-Referer": "<YOUR_SITE_URL>",
            "X-Title": "<YOUR_SITE_NAME>",
        },
        data=json.dumps(
            {
                "model": "google/gemini-2.0-pro-exp-02-05:free",
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": input},
                        ],
                    }
                ],
            }
        ),
    )
    return response


data = {
    "html_attributions": [],
    "results": [
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": 49.278226, "lng": -122.9103601},
                "viewport": {
                    "northeast": {"lat": 49.27946057989272, "lng": -122.9090467201073},
                    "southwest": {"lat": 49.27676092010728, "lng": -122.9117463798927},
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
            "icon_background_color": "#FF9E67",
            "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet",
            "name": "A&W Canada",
            "opening_hours": {"open_now": True},
            "photos": [
                {
                    "height": 600,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/112520828325065743547">A Google User</a>'
                    ],
                    "photo_reference": "AVzFdbmKopndrqpiYwCqpp6PX26MSjVY_idmVkb1KW6rHEq8NA0f0gyRCXLVytC73s2oZor0B0Etv8vpAXXfvtgMmHSQIQO3F3mYQmR1GT3jDYKFOnioau_v9V8jkU-uSivB3oR8-acj54ar3HTBafuqrc1LR85vTshTdxTapOKGV2riF5Je",
                    "width": 1080,
                }
            ],
            "place_id": "ChIJVRgRvb55hlQR0QCzaJDp5lQ",
            "plus_code": {"compound_code": "73HQ+7V Burnaby, British Columbia", "global_code": "84XV73HQ+7V"},
            "price_level": 1,
            "rating": 3.8,
            "reference": "ChIJVRgRvb55hlQR0QCzaJDp5lQ",
            "scope": "GOOGLE",
            "types": ["restaurant", "point_of_interest", "food", "establishment"],
            "user_ratings_total": 360,
            "vicinity": "9055 University High St, Burnaby",
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": 49.2781045, "lng": -122.9099774},
                "viewport": {
                    "northeast": {"lat": 49.27938482989272, "lng": -122.9087304201073},
                    "southwest": {"lat": 49.27668517010728, "lng": -122.9114300798927},
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
            "icon_background_color": "#FF9E67",
            "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet",
            "name": "Uncle Fatih's Pizza - SFU",
            "opening_hours": {"open_now": True},
            "photos": [
                {
                    "height": 3024,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/116464422407108071710">YP A</a>'
                    ],
                    "photo_reference": "AVzFdbmFnxFOnStXCyYO_vs-BgyGKxpjROynMEqOFlbLLEKHgyNX6Wc_aCnKQRLsQdil6X2miHrGfrJjA1Cn8l3t8Tpj3v0-0yKwrH1PDxAUB3n8aCMThihnCg1CnJ0eu07fRCTzgyeTwX32jeTVJy7y__Umj0drw6oncB7rihtRVDL1Kls4",
                    "width": 4032,
                }
            ],
            "place_id": "ChIJi8p8o755hlQRh6K4U6oMJ9c",
            "plus_code": {"compound_code": "73HR+62 Burnaby, British Columbia", "global_code": "84XV73HR+62"},
            "price_level": 1,
            "rating": 4.1,
            "reference": "ChIJi8p8o755hlQRh6K4U6oMJ9c",
            "scope": "GOOGLE",
            "types": ["meal_takeaway", "meal_delivery", "restaurant", "point_of_interest", "food", "establishment"],
            "user_ratings_total": 359,
            "vicinity": "9055 University High St Unit 108, Burnaby",
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": 49.2779836, "lng": -122.9123347},
                "viewport": {
                    "northeast": {"lat": 49.27924807989272, "lng": -122.9110215701073},
                    "southwest": {"lat": 49.27654842010728, "lng": -122.9137212298927},
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
            "icon_background_color": "#FF9E67",
            "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet",
            "name": "BierCraft UniverCity",
            "opening_hours": {"open_now": True},
            "photos": [
                {
                    "height": 4080,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/103987496290565536892">Bob Bob</a>'
                    ],
                    "photo_reference": "AVzFdbntNclz0vG7KE0kGjat80qZNvXeBIUANnkiusENgc0n0ZFGYafSmneb9VeBzR7xkgl-hHDn_ngTCEFsoKSW0_T3vPTh_VUNG8H2K_rX6oZIo5LTrdupgPtX-iB-gxFbLkLtGXr0Y4X4BiCaNpKGLYfF5mJjmRONanZGhW5MtmME0MeB",
                    "width": 3072,
                }
            ],
            "place_id": "ChIJX6BpGed5hlQR_UiQwWXWxLA",
            "plus_code": {"compound_code": "73HQ+53 Burnaby, British Columbia", "global_code": "84XV73HQ+53"},
            "rating": 4.4,
            "reference": "ChIJX6BpGed5hlQR_UiQwWXWxLA",
            "scope": "GOOGLE",
            "types": ["restaurant", "night_club", "bar", "point_of_interest", "food", "establishment"],
            "user_ratings_total": 402,
            "vicinity": "8902 University High St, Burnaby",
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": 49.277811, "lng": -122.911918},
                "viewport": {
                    "northeast": {"lat": 49.27912612989272, "lng": -122.9105874201073},
                    "southwest": {"lat": 49.27642647010727, "lng": -122.9132870798927},
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
            "icon_background_color": "#FF9E67	",
            "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet",
            "name": "Donair Town",
            "opening_hours": {"open_now": True},
            "photos": [
                {
                    "height": 4032,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/109416225494689520237">Baharak B</a>'
                    ],
                    "photo_reference": "AVzFdbkNJDIJf7T0EeccfTONzNHh0kgR5r-Gcck-Ll2RoICp2S3HPpvjMns2DCIk_EpuP6HirGktm0zB-6MGrkS-lSm3BDQr7yOkMUWOH-42jzZmMiXqBW7z2WKPZNUTbnPwlbySwwVBTOukNhKj1luzPeDVcnBE1nSAqyMf4JiH6ju4Ft3l",
                    "width": 3024,
                }
            ],
            "place_id": "ChIJzaljwr55hlQR5aFUxiNgYDc",
            "plus_code": {"compound_code": "73HQ+46 Burnaby, British Columbia", "global_code": "84XV73HQ+46"},
            "price_level": 1,
            "rating": 3.8,
            "reference": "ChIJzaljwr55hlQR5aFUxiNgYDc",
            "scope": "GOOGLE",
            "types": ["restaurant", "point_of_interest", "food", "establishment"],
            "user_ratings_total": 172,
            "vicinity": "8923 Cornerstone Mews, Burnaby",
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": 49.2778123, "lng": -122.9117063},
                "viewport": {
                    "northeast": {"lat": 49.27911292989273, "lng": -122.9103954201072},
                    "southwest": {"lat": 49.27641327010728, "lng": -122.9130950798927},
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
            "icon_background_color": "#FF9E67",
            "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet",
            "name": "Plum Garden & CHAKURA",
            "opening_hours": {"open_now": True},
            "photos": [
                {
                    "height": 3024,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/117645172055826034475">James Xu</a>'
                    ],
                    "photo_reference": "AVzFdbmpuGAc-EuwyRNS9Da8k03_jTj2S0sN7kkF-S_jRzX1_zDzozPyetHIgp9lN39pmtZmOy9NNW61ymLj8DSNB_Ioie1AgqowRH2UaTk9iAHHh57vQNO2oTywFQYRtAhduDJ2erh0WXyvwAYXrj5P8PaIUqfJ_XT41uZ2pnoR32R_Argh",
                    "width": 4032,
                }
            ],
            "place_id": "ChIJocYBw755hlQROt4d5MxnJQQ",
            "plus_code": {"compound_code": "73HQ+48 Burnaby, British Columbia", "global_code": "84XV73HQ+48"},
            "rating": 3.3,
            "reference": "ChIJocYBw755hlQROt4d5MxnJQQ",
            "scope": "GOOGLE",
            "types": ["restaurant", "cafe", "point_of_interest", "food", "establishment"],
            "user_ratings_total": 43,
            "vicinity": "8939 and 8951 Cornerstone Mews, Burnaby",
        },
        {
            "business_status": "OPERATIONAL",
            "geometry": {
                "location": {"lat": 49.2799033, "lng": -122.9247656},
                "viewport": {
                    "northeast": {"lat": 49.28141847989271, "lng": -122.9231636201073},
                    "southwest": {"lat": 49.27871882010727, "lng": -122.9258632798928},
                },
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
            "icon_background_color": "#FF9E67",
            "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet",
            "name": "SFU Dining Commons",
            "opening_hours": {"open_now": True},
            "photos": [
                {
                    "height": 2268,
                    "html_attributions": [
                        '<a href="https://maps.google.com/maps/contrib/114153623354248934417">Amarthya Kaushik</a>'
                    ],
                    "photo_reference": "AVzFdbnWOWeznCdXbeuikP3paSrVbRkvBtKu2NJBPExuueXiTV_-aeNmRXgB2hr-G8vsVGdXPyMxW2T8TuKoTwv5PeOCUJ7XsHma1YFvSmc9yh44AbxBkLRuQKkzT2C9yU5QjukKooIIAuE0v63lMMDmpWObP6NtWUpd524MRENW6wxZBXMQ",
                    "width": 4032,
                }
            ],
            "place_id": "ChIJSyxOuOp5hlQRbmCgbE6M5VA",
            "plus_code": {"compound_code": "73HG+X3 Burnaby, British Columbia", "global_code": "84XV73HG+X3"},
            "price_level": 1,
            "rating": 3.9,
            "reference": "ChIJSyxOuOp5hlQRbmCgbE6M5VA",
            "scope": "GOOGLE",
            "types": ["restaurant", "point_of_interest", "food", "establishment"],
            "user_ratings_total": 590,
            "vicinity": "8888 University Dr W, Burnaby",
        },
    ],
    "status": "OK",
}

results = data["results"]

sorted_results = sorted(results, key=lambda x: x["rating"], reverse=True)
picked = sorted_results[0]

prompt = f"Tell a user with a {personality[4]} tone that they should go to {picked['name']} (that you picked) for a meal. The restaurant is located at {picked['vicinity']}. The restaurant has a rating of {picked['rating']}."

data_json = get_ai_pick(prompt).json()
content = data_json["choices"][0]["message"]["content"]
print(content)
