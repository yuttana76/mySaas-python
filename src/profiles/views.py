from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def profile_list_view(request):
    context = {
        "user": request.user,
        "object_list": User.objects.filter(is_active=True)
    }
    return render(request, "profiles/list.html", context)


# @login_required
# def profile_view(request, username=None,*args, **kwargs):

#     user = request.user

#     # Authentication and Authorization | user | Can view user

#     profile_user_obj = User.objects.get(username=username)
#     # profile_user_obj = get_object_or_404(User, username=user)

#     # has_premission = profile_user_obj.has_perm("Authentication and Authorization | user | Can delete user")
#     # app_label.view_<modelname>
#     # app_label.add_<modelname>
#     # app_label.change_<modelname>
#     # app_label.delete_<modelname>
#     has_premission = profile_user_obj.has_perm("auth.view_user")
#     has_premission = profile_user_obj.has_perm("visits.view_pagevisit")
#     is_me = user == profile_user_obj

#     # Example check for permission
#     # if is_me:
#     #     if user.has_perm("visits.view_pagevisit"):
#     #         pass

#     return HttpResponse( f"Hello ! {profile_user_obj}- {profile_user_obj.id} - is ME:{is_me} - perm:"+str(has_premission))

@login_required
def profile_detail_view(request, username=None, *args, **kwargs):
    user = request.user
    print(
        user.has_perm("subscriptions.basic"),
        user.has_perm("subscriptions.basic_ai"),
        user.has_perm("subscriptions.pro"),
        user.has_perm("subscriptions.advanced"),    
    )
    # user_groups = user.groups.all()
    # print("user_groups", user_groups)
    # if user_groups.filter(name__icontains='basic').exists():
    #     return HttpResponse("Congrats")
    profile_user_obj = get_object_or_404(User, username=username)
    is_me = profile_user_obj == user
    context = {
        "object": profile_user_obj,
        "instance": profile_user_obj,
        "owner": is_me,
    }
    return render(request, "profiles/detail.html", context)