#!/usr/bin/env bash

PORT=8888
echo "Port: $PORT"

# POST method predict
curl -d '{  
   "EXPERIENCE": 5,
   "TEST": 5,
   "INTERVIEW": 5
}'\
     -H "Content-Type: application/json" \
     -X POST http://ec2-3-142-230-226.us-east-2.compute.amazonaws.com:$PORT/predict_api
