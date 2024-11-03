This handles only Get request

url : http://127.0.0.1:8000/primary/entity/?category=<string>>&results=<int>

Note : category to be passed from the frontend, results in optional. If results is given then it fetches the top n results are fetched.

response : 

[
    {
        "id": "b548f9e0-32ae-42d1-aa36-7d4025f5d6a7",
        "name": "Ram Charan",
        "image_url": "/media/images/ram_charan.jpg"
    },
    {
        "id": "f353e980-a29d-4e79-8cd7-1326ba298da8",
        "name": "Allu Arjun",
        "image_url": "/media/images/allu_arjun.jfif"
    }
]



