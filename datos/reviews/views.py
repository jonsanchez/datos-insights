from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from datasets.models import Dataset
from models.models import Model
from reviews.forms import DatasetReviewForm, ModelReviewForm
from .models import DatasetReview, ModelReview


# Create your views here.
def review_dataset_view(request, pk, template_name='reviews/review_dataset_view.html'):
    dataset_review = get_object_or_404(DatasetReview, pk=pk)
    return render(request=request, template_name=template_name, context={'dataset_review': dataset_review})


@login_required
def review_dataset_create(request, pk, template_name='reviews/review_dataset_form.html'):
    form = DatasetReviewForm(request.POST or None)
    if form.is_valid():
        if request.user.is_authenticated:
            form.instance.author = request.user
            form.instance.dataset = Dataset.objects.get(pk=pk)
            form.save()
            return redirect('datasets:dataset_view', pk=pk)
    return render(request=request, template_name=template_name, context={'form': form})


def review_dataset_update(request, pk, template_name='reviews/review_dataset_form.html'):
    dataset = get_object_or_404(DatasetReview, pk=pk)
    form = DatasetReviewForm(request.POST or None, instance=dataset)
    if form.is_valid():
        form.save()
        return redirect('datasets:dataset_view', pk=pk)
    return render(request=request, template_name=template_name, context={'form': form})


# class DatasetReviewDelete(DeleteView):
#     model = DatasetReview
#     success_url = reverse_lazy('profile_view')


def review_model_view(request, pk, template_name='reviews/review_model_view.html'):
    model_review = get_object_or_404(ModelReview, pk=pk)
    return render(request=request, template_name=template_name, context={'model_review': model_review})


@login_required
def review_model_create(request, pk, template_name='reviews/review_model_form.html'):
    form = ModelReviewForm(request.POST or None)
    if form.is_valid():
        if request.user.is_authenticated:
            form.instance.author = request.user
            form.instance.model = Model.objects.get(pk=pk)
            form.save()
            return redirect('models:model_view', pk=pk)
    return render(request=request, template_name=template_name, context={'form': form})


def review_model_update(request, pk, template_name='reviews/review_model_form.html'):
    model_review = get_object_or_404(ModelReview, pk=pk)
    form = ModelReviewForm(request.POST or None, instance=model_review)
    if form.is_valid():
        form.save()
        return redirect('models:model_view', pk=model_review.model.pk)
    return render(request=request, template_name=template_name, context={'form': form})


class ModelReviewDelete(DeleteView):
    template_name = 'reviews/review_model_confirm_del.html'

    model = ModelReview
    success_url = reverse_lazy('subscriptions:subscription_list_view')

# def dataset_delete(request, pk, template_name='datasets/dataset_confirm_delete.html'):
#     dataset = get_object_or_404(Dataset, pk=pk)
#     if request.method == 'POST':
#         dataset.delete()
#         return redirect('dataset_list')
#     return render(request, template_name, {'object': dataset})
