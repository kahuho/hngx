from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import StageOneData
from .serializers import StageOneDataSerializer

@api_view(['GET'])
def stage_one_endpoint(request):
    slack_name = request.GET.get('slack_name', '')
    track = request.GET.get('track', '')
    current_day = timezone.now().strftime('%A')
    utc_time = timezone.now()
    github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"
    github_repo_url = "https://github.com/username/repo"
    
    # Save data to the database
    data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time,
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
    }
    serializer = StageOneDataSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data, status=200)
