from django.shortcuts import render, get_object_or_404, redirect
from .models import Stock, Supplier, Order
from .forms import OrderForm
from django.contrib import messages

# Create your views here.
def home_page(request):
    return render(request, template_name='index.html')

def add_stock(request):
    message = ''
    if request.method == "POST":
        formdata = request.POST
        if formdata:
            try:
                supplier_id_id = request.POST.get("suppliers")
                supplier_id = Supplier.objects.get(id = supplier_id_id)

                stock = Stock.objects.create(
                    name=formdata.get('name'),
                    description=formdata.get('description'),
                    minqty_required=formdata.get('minqty_required'),
                    maxqty_required=formdata.get('maxqty_required'),
                    cost_per_unit=formdata.get('cost_per_unit'),
                    usage_level=formdata.get('usage_level'),
                    reorder_duration=formdata.get('reorder_duration'),
                    supplier_id=supplier_id,
                )
                message = "Stock Saved successfully...!"
            except Exception as e:
                message = f"Error saving Stock record: {str(e)}"
    return render(request, template_name="stock.html", context={"result": message, "suppliers":Supplier.objects.all()})

def add_supplier(request):
    message = ''
    if request.method == "POST":
        formdata = request.POST
        if formdata:
            try:
                supplier = Supplier.objects.create(
                    name=formdata.get('name'),
                    address=formdata.get('address'),
                    location=formdata.get('location'),
                    contact=formdata.get('contact'),
                    stock_name=formdata.get('stock_name'),
                    gst_no=formdata.get('gst_no'),
                    rating=formdata.get('rating'),
                )
                message = "Supplier Record Saved successfully...!"
            except Exception as e:
                message = f"Error saving Supplier record: {str(e)}"
    return render(request, template_name="supplier.html", context={"result": message})

def list_of_supplier(request):
    query = request.GET.get('search')
    if query:
        suppliers = Supplier.objects.filter(name__icontains=query)
    else:
        suppliers = Supplier.objects.all()

    return render(request, template_name="supplier_list.html", context={'suppliers': suppliers})

def supplier_detail(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    return render(request, 'supplier_detail.html', {'supplier': supplier})

def list_of_stock(request):
    stocks = Stock.objects.all()
    return render(request, template_name="stock_list.html", context={'stocks': stocks})


def stock_detail(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)
    return render(request, 'stock_detail.html', {'stock': stock})

def stock_and_supplier_control_card(request):
    stocks = Stock.objects.all()
    selected_stock = None
    selected_supplier = None

    if request.method == 'POST':
        selected_stock_id = request.POST.get('stock_selector')
        selected_stock = get_object_or_404(Stock, id=selected_stock_id)
        selected_supplier = selected_stock.supplier_id

    return render(request, 'stock_and_supplier_detail.html', {'stocks': stocks, 'selected_stock': selected_stock, 'selected_supplier': selected_supplier})

def supplier_with_stock(request):
    suppliers = Supplier.objects.all()
    selected_supplier = None
    selected_stocks = None

    if request.method == 'POST':
        selected_supplier_id = request.POST.get('supplier_selector')
        selected_supplier = get_object_or_404(Supplier, id=selected_supplier_id)
        selected_stocks = Stock.objects.filter(supplier_id=selected_supplier.id)

    return render(request, 'supplier_stock.html', {'suppliers': suppliers, 'selected_supplier': selected_supplier, 'selected_stocks': selected_stocks})

def stock_control(request):
    stocks = Stock.objects.all()
    return render(request, template_name="stock_control.html", context={'stocks': stocks})

def place_order(request, stock_id):
    stock = Stock.objects.get(pk=stock_id)

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order_quantity = form.cleaned_data['order_quantity']

            Order.objects.create(stock=stock, order_quantity=order_quantity, is_confirmed=False)

            return redirect('stock_control')
    else:
        form = OrderForm()

    return render(request, 'place_order.html', {'form': form, 'stock': stock})


def order_confirmation(request):
    unconfirmed_orders = Order.objects.filter(is_confirmed=False).order_by('-id')

    if unconfirmed_orders.exists():
        if request.method == "POST":
            order_id = request.POST.get('order_id')
            current_order = get_object_or_404(Order, id=order_id, is_confirmed=False)
            
            action = request.POST.get('action')
            if action == 'accept':
                stock = current_order.stock
                stock.maxqty_required += current_order.order_quantity
                stock.save()

                current_order.is_confirmed = True
                current_order.save()

                messages.info(request, 'Order confirmed.')
                return redirect('order_confirmation')
            elif action == 'cancel':
                current_order.delete()
                messages.info(request, 'Order has been canceled.')
                return redirect('order_confirmation')

        return render(request, 'order_confirmation.html', {'orders': unconfirmed_orders})

    messages.info(request, 'No orders available.')
    return redirect('home_supplier')



def show_orders(request):
    orders = Order.objects.filter(is_confirmed=True)
    return render(request, 'show_orders.html', {'orders': orders})