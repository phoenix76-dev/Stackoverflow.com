from django.shortcuts import render_to_response


def render_main_page(request):
    return render_to_response('questions_block.html')
