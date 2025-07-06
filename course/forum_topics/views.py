from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .services import (
    create_forum_topic,
    get_forum_topic_by_id,
    get_forum_topics_by_forum_id,
    get_forum_topics_by_user_id,
    get_all_forum_topics,
    update_forum_topic,
    delete_forum_topic,
)

class ForumTopicListView(APIView):
    def get(self, request):
        try:
            if 'forum_id' in request.query_params:
                forum_id = request.query_params.get('forum_id')
                forum_topics = get_forum_topics_by_forum_id(forum_id)
                return Response(forum_topics, status=status.HTTP_200_OK)
            elif 'user_id' in request.query_params:
                user_id = request.query_params.get('user_id')
                forum_topics = get_forum_topics_by_user_id(user_id)
                return Response(forum_topics, status=status.HTTP_200_OK)
            elif 'topic_id' in request.query_params:
                topic_id = request.query_params.get('topic_id')
                forum_topic = get_forum_topic_by_id(topic_id)
                return Response(forum_topic, status=status.HTTP_200_OK)
            else:
                forum_topics = get_all_forum_topics()
                return Response(forum_topics, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            forum_topic = create_forum_topic(request.data)
            return Response(forum_topic, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, topic_id):
        try:
            updated_forum_topic = update_forum_topic(topic_id, request.data)
            return Response(updated_forum_topic, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, topic_id):
        try:
            result = delete_forum_topic(topic_id)
            return Response(result, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_404_NOT_FOUND)