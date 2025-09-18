from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Message
from .forms import NicknameForm, MessageForm

def set_nickname(request):
    if request.method == "POST":
        form = NicknameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            # Check uniqueness
            if Message.objects.filter(username=username).exists():
                return render(request, "chat/set_nickname.html", {
                    "form": form,
                    "error": "Username already taken, choose another."
                })
            request.session["username"] = username
            return redirect("chatroom")
    else:
        form = NicknameForm()
    return render(request, "chat/set_nickname.html", {"form": form})

# def chatroom(request):
#     if "username" not in request.session:
#         return redirect("set_nickname")

#     username = request.session["username"]

#     if request.method == "POST":
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             Message.objects.create(
#                 username=username,
#                 text=form.cleaned_data["text"],
#                 timestamp=timezone.now()
#             )
#             return redirect("chatroom")
#     else:
#         form = MessageForm()

#     messages = Message.objects.order_by("-timestamp")[:20]  # last 20 msgs
#     return render(request, "chat/chatroom.html", {"messages": messages, "form": form, "username": username})


def chatroom(request):
    if "username" not in request.session:
        return redirect("set_nickname")

    username = request.session["username"]

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(
                username=username,
                text=form.cleaned_data["text"],
                timestamp=timezone.now()
            )
            return redirect("chatroom")
    else:
        form = MessageForm()

    # Get all messages, oldest → newest
    messages = Message.objects.order_by("timestamp")

    return render(request, "chat/chatroom.html", {"messages": messages, "form": form, "username": username})

