from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .models import Review,Product
from .forms import ReviewCreateForm
# Create your views here.

# class ReviewCreate(CreateView):
#     model = Review
#     fields = ['rating','comment','image']


def ReviewCreate(request):
    product_id = request.POST['product']
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = ReviewCreateForm(request.POST,request.FILES)
        
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # 현재 로그인된 사용자
            review.product = product
            if 'rating' not in request.POST:
                return render(request, '리뷰 작성 템플릿 경로', {'form': form, 'product': product, 'error_message': 'Rating 값을 선택해주세요.'})
            review.rating = float(request.POST['rating'])
            # if 'image' in request.FILES:
            #     review.image = request.FILES['image']
            review.save()
            
            return HttpResponse('처리완료')
    else:
        form = ReviewCreateForm()

    return render(
        request,
        'reviews/review_form.html',
        {'form':form,
         'product':product,
        }
    )

# from django.shortcuts import get_object_or_404
# def ReviewCreate(request,order_id):
#     obj = get_object_or_404(Order, id=order_id, user=request.user)

#     if request.method == 'POST':
#         form = ReviewCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('처리완료')
#     else:
#         form = ReviewCreateForm()

#     return render(
#         request,
#         'reviews/review_form.html',
#         {'form':form,
#          'product':product
#         }
#     )
  
# 리뷰작성 유효성 검사 '/reviews/create/<int:order_id>' or '/product_detail/product_id/' 리다이렉트
# views.detail
# def review_create_from(request):
#     if request.user.is_authenticated:
#         user=request.user
#         product_id = request.POST['product']
        # order_id = Order.objects.fillter(user=request.user,product_id=product_id)
        # product = Product.objects.get(pk=product_id)
        # if not order_id:
        #      return redirect('/product_detail/product_id/') 
        # if Review.objects.filter(order_id=order_id).exists():
        #      return redirect('/product_detail/product_id/') 
        # return redirect('/reviews/create/<int:order_id>')
        # return redirect('/create/')
  