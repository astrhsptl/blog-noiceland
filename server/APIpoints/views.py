from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist

from pages.models import Likes

from pages.models import Likes, Post, Subscribe, Comment
from authsystem.models import User


@api_view(['POST', "GET"])
def add_comment(request):
    try:
        return Response(*_get_interlayer_result(
            Comment, 
            author=User.objects.get(pk=request.GET.get('user_id')),
            post=Post.objects.get(pk=request.GET.get('post_id')),
        ))
    except:
        return Response({'detail': 'does not exist'}, status.HTTP_204_NO_CONTENT)

@api_view(['POST', 'GET'])
def get_post_comments(request):
    try:
        return Response(
            Comment.objects.filter(
                post=Post.objects.get(pk=request.GET.get('post_id')),
            ).select_related(), status=status.HTTP_200_OK) # .order_by('-crea')
    except:
        return Response({'detail': 'does not exist'}, status.HTTP_204_NO_CONTENT)



@api_view(['POST',])
def add_like(request):
    try:
        return Response(*_get_interlayer_result(
            Likes, 
            user=User.objects.get(pk=request.GET.get('user_id')),
            post=Post.objects.get(pk=request.GET.get('post_id')),
        ))
    except:
        return Response({'detail': 'does not exist'}, status.HTTP_204_NO_CONTENT)

@api_view(['POST',])
def get_post_likes(request):
    return Response(
        *_get_post_likes(request)
    )


@api_view(['POST', 'GET'])
def add_subscriber(request):
    try:
        return Response(*_get_interlayer_result(
            Subscribe, 
            author=User.objects.get(pk=request.GET.get('author_id')),
            subscriber=User.objects.get(pk=request.GET.get('subscriber_id')),
        ))
    except:
        return Response({'detail': 'does not exist'}, status.HTTP_204_NO_CONTENT)

@api_view(['POST', 'GET'])
def get_subscribers_or_subscribes(request):

    get_users = lambda author, subscriber: Subscribe.objects.filter(author=author) if author else Subscribe.objects.filter(subscriber=subscriber)   

    try:
        return Response(get_users(
            author=request.GET.get('author_id'), 
            subscriber=request.GET.get('subscriber_id')), status=status.HTTP_200_OK)
    except:
        return Response({'detail': 'does not exist'}, status.HTTP_204_NO_CONTENT)





def _get_post_likes(request):
    try:
        return {'likes': Likes.objects.filter(post=Post.objects.get(pk=request.GET.get('post_id'))).count()}, status.HTTP_200_OK
    except:
        return {'likes': 0}, status.HTTP_204_NO_CONTENT

def _get_interlayer_result(interlayer, **kwargs):
    obj, is_created = interlayer.objects.get_or_create(**kwargs)

    if is_created:
        obj.save()
        return {'detail': 'successful created'}, status.HTTP_201_CREATED
    else:
        obj = interlayer.objects.get(**kwargs)
        obj.delete()
        return {'detail': 'successful delete'}, status.HTTP_202_ACCEPTED

"""@api_view(['POST'])
def like_managet(request):
    ...

def _manage_likes(request):
    try:
        return {'likes': Likes.objects.filter(post=Post.objects.get(pk=request.GET.get('post_id'))).count()}, status.HTTP_200_OK
    except:
        return {'likes': 0}, status.HTTP_204_NO_CONTENT
"""