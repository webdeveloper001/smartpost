from django.core import serializers
from django.http import HttpResponse, JsonResponse

from django.db.models import F

from django.contrib.auth.models import User
from simply_posted_calendar.models import Publication
from simply_posted_accounts.models import Post, RejectedPost

from publishing import PublishingService
from select_posts import ContentSelectionService

import urllib2

def get_all(request):
    publications = to_dict(request, Publication.objects.filter(user=request.user))
    return JsonResponse(publications, safe=False)

def approve(request, pk):
    publication = Publication.objects.filter(pk=pk)
    publication.update(approved=True) 

    data = publication.values().first()
    return JsonResponse(data)

def publish(request, pk):
    publication = Publication.objects.filter(pk=pk)
    publication.update(approved=True) 

    profile = request.user.social_auth
    PublishingService(profile, publication.first().post).publish_post()
    publication.update(published=True)

    data = publication.values().first()
    return JsonResponse(data)

def reject(request, pk):
    publication = Publication.objects.filter(pk=pk)
    publication.update(reject_count=F('reject_count') + 1)
    request.user.rejected_posts.create(post=publication.first().post)

    substituted_post = substitute(publication.first())
    if substituted_post:
        data = to_dict([substituted_post])
    else:
      data = []

    return JsonResponse(data, safe=False)

def get_new(request):
    publications = ContentSelectionService(request.user).make_publications()
    return JsonResponse(to_dict(publications), safe=False)

def to_dict(request, publications):
    result = []
    for publication in publications:
        color = '#449d44' if publication.approved else '#c9302c' if publication.approved == False else '#337ab7'
        title = publication.post.corporate_title if publication.corporate_title else publication.post.playful_title

        # content = urllib2.urlopen(publication.post.blog_link).read()
        content = publication.post.blog_link
        image_link = publication.post.image_link

        publication_data = {
            'title': title, 
            'content': content, 
            'image': image_link, 
            'fb_groups': request.user.social_auth.get(provider="facebook").extra_data['groups'], 
            'fb_pages': request.user.social_auth.get(provider="facebook").extra_data['pages'], 
            'start': publication.publication_date.isoformat(), 
            'id': publication.id, 
            'color': color, 
            'reject_count': publication.reject_count, 
            'approved': publication.approved
        }
        result.append(publication_data)

    return result

def substitute(publication):
    if publication.reject_count >= 3:
        publication.approved = False
        publication.save()
        return False


    new_id = Post.objects.filter(category=publication.post.category).exclude(users=publication.user).exclude(id__in=publication.user.rejected_posts.values_list('post_id', flat=True)).first()
    publication.post_id = new_id
    publication.save()

    return publication
