from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from .models import Board
from .forms import BoardForm
from django.views import generic


class Lists_board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        # 페이지당 게시물
        PAGE_ROW_COUNT = 10

        PAGE_DIS_COUNT = 5;
        result_list = Board.objects.all()

        # result_list = result_line()
        total_len = len(result_list)
        page = request.GET.get('page', 1)
        paginator = Paginator(result_list, PAGE_ROW_COUNT)
        try:
            lines = paginator.page(page)
        except PageNotAnInteger:
            lines = paginator.page(1)
        except EmptyPage:
            lines = paginator.page(paginator.num_pages)

        index = lines.number - 1
        max_index = len(paginator.page_range)
        start_index = index - 2 if index >= 2 else 0
        if index < 2:
            end_index = 5 - start_index
        else:
            end_index = index + 3 if index <= max_index - 3 else max_index

        page_range = list(paginator.page_range[start_index:end_index])

        template_name = 'lists_board/lists_board.html'

        return render(
            request,
            template_name,
            {
                'lists': result_list,
                'result_list': lines,
                'page_range': page_range,
                'total_len': total_len,
                'max_index': max_index - 2
            }
        )


class Lists_board_detail(generic.DetailView):
    model = Board
    template_name = 'lists_board/detail.html'
    context_object_name = 'list'

class Lists_board_update(generic.UpdateView):
    model = Board
    fields = ('title', 'content')
    template_name = 'lists_board/update.html'
    success_url = '/lists_board/'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'lists_board/success.html', {"message": "게시물을 수정하였습니다."})

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)


class Lists_board_delete(generic.DeleteView):
    model = Board
    success_url = '/lists_board/'
    context_object_name = 'list'


@login_required
def check_post(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        new_post = form.save(commit=False)
        new_post.save()
        messages.info(request, '게시되었습니다')
        return HttpResponseRedirect(reverse_lazy('lists_board:lists_board'))
    else:
        form = BoardForm()

    return render(request, 'lists_board/insert.html', {'form': form})
