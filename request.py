import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--experience", type=int, required=True)
parser.add_argument("--interview", type=int, required=True)
parser.add_argument("--test", type=int, required=True)
args = parser.parse_args()


url = 'http://127.0.0.1:8080/predict_api'
r = requests.post(url,json={'experience':args.experience, 'test_score':args.test, 'interview_score': args.interview})

print(r.json())