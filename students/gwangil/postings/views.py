import json

from django.views import View
from django.http  import JsonResponse

from users.models import User
from .models      import Posting, Image, Comment, Like
from .util        import login_decorator

# 포스팅뷰(게시글 작성)
class PostingView(View):
    #포스팅 생성
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)

            user_id = data.get("user_id")

            # user_id 가 존재하지 않는다면 404에러 반환
            if not User.objects.filter(id = user_id).exists():
                return JsonResponse({ "MESSAGE" : "DOES_NOT_EXIST_USER" }, status = 404)

            # 이상 없으면 posts 테이블에 user_id 데이터 추가
            Posting.objects.create(
                user_id   = user_id
            )
            
            return JsonResponse({ "MESSAGE" : "SUCCESS" }, status = 201)
        except KeyError:  # 키에러
            return JsonResponse({ "MESSAGE" : "KEY_ERROR" }, status = 400)            

    #생성된 포스팅 보기 
    @login_decorator
    def get(self,request):
        posts  = Posting.objects.all()   # models.py > class Posting 내에 있는 모든 정보 불러오기

        result = []

        for post in posts:
            image_list = [] # image 를 담을 list 
            images     = post.imgs.all()  # post_id 를 가지고 있는 images 정보 모두 가져오기 (image_set)
            for image in images:
                image_list.append(image.image_url) # image_url를 빈 리스트에 추가하기

            comment_list  = [] # comment 를 담을 list
            comments      = post.comments.all() # post_id 를 가지고 있는 comments 정보 모두 가져오기 (comment_set)
            for comment in comments:
                comment_information = { 
                    "user_id" : comment.user_id, # 각 comment에 해당하는 user_id 값 불러오기
                    "content" : comment.content # 각 comment에 해당하는 content 값 불러오기
                }
                comment_list.append(comment_information) # comment_information 내용 빈 리스트에 추가하기

            like_count = 0
            likes      = post.likes.all() # post_id 를 가지고 있는 likes 정보 모두 가져오기 (like_set)
            for like in likes:
                like_count += 1
                # "posting_id" : like.posting_id,
                # like.user_id
                

            # 최종적으로 보여질 내용은 user_id, id(posting_id), image_list, comment_list
            post_information = {
                "posting_id"           : post.id,
                "user_id"      : post.user_id,
                "image_list"   : image_list,
                "comment_list" : comment_list,
                "like_list" : like_count
            }
            
            result.append(post_information)

        return JsonResponse({ "POSTINGS" : result }, status = 200)

# 이미지뷰 (게시글에 들어갈 이미지)
class ImageView(View):
    # posting_id와 그에 맞는 image_url 생성
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)

            img_url    = data["image_url"]
            posting_id = data["posting_id"]

            # posting_id가 db에 없으면 404 에러와 함꼐 메세지 반환
            if not Posting.objects.filter(id = posting_id).exists(): 
                return JsonResponse({ "MESSAGE" : "DOES_NOT_EXIST_POSTING" }, status = 404)

            # 위의 if 문에서 이상 없다면 images 테이블에 image_url, posting_id 추가 
            Image.objects.create(
                image_url  = img_url,
                posting_id = posting_id
            )
            return JsonResponse({ "MESSAGE" : "SUCCESS" }, status = 201)
        except KeyError:
            return JsonResponse({ "MESSAGE" : "KEY_ERROR" }, status = 400)
            
# 코멘트뷰(댓글)
class CommentView(View):
    # posting_id와 user_id, 그에 맞는 comment(댓글) 생성
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)

            content    = data["content"]
            posting_id = data["posting_id"]
            user_id    = data["user_id"]

            # user_id가 db에 없다면 404 에러와 함께 메세지 반환
            if not User.objects.filter(id = user_id).exists():
                return JsonResponse({ "MESSAGE" : "DOES_NOT_EXIST_USER" }, status = 404)
            
            # posting_id가 db에 없다면 404 에러와 함께 메세지 반환
            if not Posting.objects.filter(id = posting_id).exists():
                return JsonResponse({ "MESSAGE" : "DOES_NOT_EXIST_POSTING" }, status = 404)

            # 위의 if 문에서 이상 없다면 comments 테이블에 content, posting_id, user_id 추가 
            Comment.objects.create(
                content    = content,
                posting_id = posting_id,
                user_id    = user_id
            )
            
            return JsonResponse({ "MESSAGE" : "SUCCESS" }, status = 201)
        except KeyError:
            return JsonResponse({ "MESSAGE" : "KEY_ERROR" }, status = 400)
    # 생성된 댓글 보기
    @login_decorator
    def get(self, request):
        # db에 있는 comment 내용 모두 불러오기
        comments = Comment.objects.all()

        result = []
    
        for comment in comments:
            # content와 user_id 를 보여준다.
            comment_information = {
                "user_id" : comment.user_id,
                "content" : comment.content
            }
            result.append(comment_information)

        return JsonResponse({ "COMMENTS" : result }, status = 200)

# 라이크뷰(좋아요)
class LikeView(View):
    # 좋아요 누르기
    @login_decorator
    def post(self,request):
        try: 
            data = json.loads(request.body)

            user_id    = data["user_id"]
            posting_id = data["posting_id"]
            # user_id 가 없다면 404 에러와 함께 메세지 반환 
            if not User.objects.filter(id = user_id).exists():
                return JsonResponse({ "MESSAGE" : "DOES_NOT_EXIST_USER" }, status = 404)
            
            # posting_id 가 없다면 404 에러와 함께 메세지 반환 
            if not Posting.objects.filter(id = posting_id).exists():
                return JsonResponse({ "MESSAGE" : "DOES_NOT_EXIST_POSTING" }, status = 404)
            
            # if문이 길어지고, 중복된 내용이기 때문에 exist_user 변수에 저장
            exist_user = Like.objects.filter(posting_id = posting_id, user_id = user_id)
            # db 내에 입력된 user_id 와 posting_id 가 있다면 해당 줄은 지워버리고, 404 에러와 함께 메세지 반환
            if exist_user.exists(): 
                exist_user.delete()
                return JsonResponse({ "MESSAGE" : "LIKE_CANCEL" }, status = 404)

            # 위의 if 문에서 문제가 없다면 likes 테이블에 user_id와 posting_id 추가
            Like.objects.create(
                user_id = user_id,
                posting_id = posting_id
            )

            return JsonResponse({ "MESSAGE" : "SUCCESS" }, status = 201)
        except KeyError:
            return JsonResponse({ "MESSAGE" : "KEY_ERROR" }, status = 400)

    # # 포스팅별 좋아요 누른 유저 보기
    def get(self, request):
        posts = Posting.objects.all()
        result = []

        for post in posts:
            # post_list = []
            # post_list.append(like.posting_id)
            # Posting.objects.filter(user_id = user_id)
            # for post in post_list:
            #     user_list = [] # 하나의 포스팅에 들어갈 유저 리스트
            #     user_list.append(like.user_id) 
            user_list = []
            users = post.likes.all()
            for user in users:
                user_list.append(post.user_id)
                like_information = {
                "posting_id" : Posting.objects.get(id = like.posting_id).id,
                "user_id" : user_list
                }
            #     like_information = {
            #         "posting_id" : post,
            #         "user_list" : user_list
            #     }
            result.append(like_information)

        return JsonResponse({ "Like_list" : result }, status = 200)
