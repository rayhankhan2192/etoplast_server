import numpy as np
import tensorflow as tf
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from PIL import Image
from decouple import config  
from rest_framework import status
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
import uuid
import requests
import cv2
from dotenv import load_dotenv
from ultralytics import YOLO
import base64
#from .generative import generate_road_damage_report, generate_stream
from django.http import StreamingHttpResponse


load_dotenv()
model_path = os.getenv("MODEL_PATH")
model = YOLO(model_path)
