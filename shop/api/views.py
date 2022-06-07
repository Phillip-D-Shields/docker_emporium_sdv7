from rest_framework.decorators import api_view
from rest_framework.response import Response
from shop.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


# gets ===============================================================
@api_view(['GET'])
def get_routes(request):
    """
    This function will return all the routes in the API
    """
    routes = [
        'GET /api',
        'GET /api/categories',
        'GET /api/category/:id',
        'GET /api/category/:name',
        'GET /api/products',
        'GET /api/product/:id',
        'GET /api/product/:name',
        'POST /api/post_product',
    ]
    return Response(routes)


@api_view(['GET'])
def get_categories(request):
    """
    This function will return all the categories in the API
    """
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_category_by_id(request, id):
    """
    This function will return a category by id
    """
    category = Category.objects.get(id=id)
    serializer = CategorySerializer(category)
    return Response(serializer.data)


@api_view(['GET'])
def get_category_by_name(request, name):
    """
    This function will return a category by name
    """
    category = Category.objects.get(name=name)
    serializer = CategorySerializer(category)
    return Response(serializer.data)


@api_view(['GET'])
def get_products(request):
    """
    This function will return all the products in the API
    """
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product_by_id(request, id):
    """
    This function will return a product by id
    """
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def get_product_by_name(request, name):
    """
    This function will return a product by name
    """
    product = Product.objects.get(name=name)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


# posts ===============================================================
@api_view(['POST'])
def new_product(request):
    """
    This function will create a new product in the API
    """
    name = request.data['name']
    price = request.data['price']
    category = request.data['category']
    product = Product.objects.create(name=name, price=price, category=category)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


# puts ===============================================================
@api_view(['PUT'])
def update_product(request, id, name, price, category_id):
    """
    This function will update a product in the API
    """
    product = Product.objects.get(id=id)
    product.name = name
    product.price = price
    product.category_id = category_id
    product.save()
    serializer = ProductSerializer(product)
    return Response(serializer.data)

# deletes ===============================================================
@api_view(['DELETE'])
def delete_product(request, id):
    """
    This function will delete a product in the API
    """
    product = Product.objects.get(id=id)
    product.delete()
    return Response('Product deleted')