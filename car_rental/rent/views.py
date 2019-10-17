from rest_framework import viewsets
from .serializers import CarSerializer, TripSerializer, LenderSerializer
from .models import Car, Trip, Lender
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class CarListViewSet (viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def get(self, request, format=None):
        books = Car.objects.all()
        serializer = CarSerializer(books, many=True, context={"request": request})
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarViewSet (viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        book = self.get_object(id)
        serializer = CarSerializer(book, context={"request": request})
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        book = self.get_object(id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id, format=None):
        book = self.get_object(id)
        serializer = CarSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id, format=None):
        pass


class LenderListViewSet (viewsets.ModelViewSet):
    serializer_class = LenderSerializer
    queryset = Lender.objects.all()

    def get(self, request, format=None):
        books = Lender.objects.all()
        serializer = LenderSerializer(books, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LenderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LenderViewSet (viewsets.ModelViewSet):
    serializer_class = LenderSerializer
    queryset = Lender.objects.all()

    def get_object(self, pk):
        try:
            return Lender.objects.get(pk=pk)
        except Lender.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        book = self.get_object(id)
        serializer = LenderSerializer(book, context={"request": request})
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        book = self.get_object(id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id, format=None):
        book = self.get_object(id)
        serializer = LenderSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id, format=None):
        pass

class TripListViewSet (viewsets.ModelViewSet):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()

    def get(self, request, format=None):
        books = Trip.objects.all()
        serializer = TripSerializer(books, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TripViewSet (viewsets.ModelViewSet):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()

    def get_object(self, pk):
        try:
            return Trip.objects.get(pk=pk)
        except Trip.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        book = self.get_object(id)
        serializer = TripSerializer(book, context={"request": request})
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        book = self.get_object(id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id, format=None):
        book = self.get_object(id)
        serializer = TripSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id, format=None):
        pass

#******************************************************************************************************



# from .models import Car, Lender, Trip
# from .serializers import CarSerializer, TripSerializer, LenderSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.http import Http404
#
#
# class CarList(APIView):
#
#     def get(self, request, format=None):
#         books = Car.objects.all()
#         serializer = CarSerializer(books, many=True, context={"request": request})
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = CarSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class CarView(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Car.objects.get(pk=pk)
#         except Car.DoesNotExist:
#             raise Http404
#
#     def get(self, request, id, format=None):
#         book = self.get_object(id)
#         serializer = CarSerializer(book, context={"request": request})
#         return Response(serializer.data)
#
#     def delete(self, request, id, format=None):
#         book = self.get_object(id)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def put(self, request, id, format=None):
#         book = self.get_object(id)
#         serializer = CarSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def post(self, request, id, format=None):
#         pass
#
#
# class LenderList(APIView):
#
#     def get(self, request, format=None):
#         books = Lender.objects.all()
#         serializer = LenderSerializer(books, many=True, context={"request": request})
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = LenderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class LenderView(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Lender.objects.get(pk=pk)
#         except Lender.DoesNotExist:
#             raise Http404
#
#     def get(self, request, id, format=None):
#         book = self.get_object(id)
#         serializer = LenderSerializer(book, context={"request": request})
#         return Response(serializer.data)
#
#     def delete(self, request, id, format=None):
#         book = self.get_object(id)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def put(self, request, id, format=None):
#         book = self.get_object(id)
#         serializer = LenderSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def post(self, request, id, format=None):
#         pass
#
#
#
# class TripList(APIView):
#
#     def get(self, request, format=None):
#         books = Trip.objects.all()
#         serializer = TripSerializer(books, many=True, context={"request": request})
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = TripSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class TripView(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Trip.objects.get(pk=pk)
#         except Trip.DoesNotExist:
#             raise Http404
#
#     def get(self, request, id, format=None):
#         book = self.get_object(id)
#         serializer = TripSerializer(book, context={"request": request})
#         return Response(serializer.data)
#
#     def delete(self, request, id, format=None):
#         book = self.get_object(id)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def put(self, request, id, format=None):
#         book = self.get_object(id)
#         serializer = TripSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def post(self, request, id, format=None):
#         pass