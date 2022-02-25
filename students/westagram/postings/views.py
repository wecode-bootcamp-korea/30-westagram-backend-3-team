import json

from django.http  import JsonResponse
from django.views import View

from users.models    import User
from postings.models import Posting, Image, Comment, Like
from users.utils     import login_decorator

class PostingView(View):
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)
        try:
            user_id = request.user.id
            content = data['content']

            Posting.objects.create(
                user     = User.objects.get(id = user_id),
                content  = content
            )
            
            return JsonResponse({'message':'SUCCESS'}, status=201) 
    
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

    @login_decorator
    def get(self, request):
        postings = Posting.objects.all()
        results  = [] 

        for posting in postings:
            image_lists = []
            images      = posting.image_set.all()
            for image in images:
                image_lists.append(
                    {
                    "image_url" : image.image_url
                    }
                )
            results.append(
               {
                   "user"       : User.objects.get(id = posting.user_id).username,
                   "image_url"  : image_lists,
                   "content"    : posting.content,
                   "created_at" : posting.created_at
               }
           )
       
        return JsonResponse({'resutls':results}, status=200)

class ImageView(View):
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)
        try:
            post_id   = data['post_id']
            image_url = data['image_url']

            if not Posting.objects.filter(id = post_id).exists(): 
                return JsonResponse({'message': "Posting Does Not Exist"}, status=404)

            Image.objects.create(
                post_id   = post_id,
                image_url = image_url
            )
            
            return JsonResponse({'message':'SUCCESS'}, status=201) 
    
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

    @login_decorator
    def get(self, request):
        images = Image.objects.all()
        results  = [] 

        for image in images:
           results.append(
               {
                   "posting_id" : Posting.objects.get(id = image.post_id).id,
                   "image_url"    : image.image_url
               }
           )
       
        return JsonResponse({'resutls':results}, status=200)

class CommentView(View):
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)
        try:
            user_id    = request.user.id
            post_id    = data['post_id']
            content    = data['content']

            if not Posting.objects.filter(id = post_id).exists(): 
                return JsonResponse({'message': "Posting Does Not Exist"}, status=404)

            Comment.objects.create(
                user_id = user_id,
                post_id = post_id,
                content = content
            )
            
            return JsonResponse({'message':'SUCCESS'}, status=201) 
    
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'},status=400)

    @login_decorator
    def get(self, request):
        comments = Comment.objects.all()
        results  = [] 

        for comment in comments:
           results.append(
               {
                   "user"       : User.objects.get(id = comment.user_id).username,
                   "posting_id" : Posting.objects.get(id = comment.post_id).id,
                   "content"    : comment.content,
                   "created_at" : comment.created_at
               }
           )
       
        return JsonResponse({'resutls':results}, status=200)

class LikeView(View):
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)
        try:
            user_id    = request.user.id
            post_id    = data['post_id']

            if not Posting.objects.filter(id = post_id).exists(): 
                return JsonResponse({'message': "Posting Does Not Exist"}, status=404)

            if Like.objects.filter(user = user_id, post = post_id).exists():
                return JsonResponse({'message': "You've already pressed like"}, status=404)

            Like.objects.create(
                user_id = user_id,
                post_id = post_id
            )
            
            return JsonResponse({'message':'SUCCESS'}, status=201) 
    
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'},status=400)