from django.conf import settings
from django.conf.urls.static import static
from .views import YOLOSegmentAnalyzeView
from django.urls import path

urlpatterns = [
    path("detect-analyze/", YOLOSegmentAnalyzeView.as_view(), name="yolo-segment-analyze"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)