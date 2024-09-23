from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Preference

@api_view(['POST'])
def post_user(request):
    data = request.data
    preferences = data.get('preferences', '').split(',')

    # Validación de preferencias
    has_even = any(int(p) % 2 == 0 for p in preferences)
    has_odd = any(int(p) % 2 != 0 for p in preferences)

    if not has_even or not has_odd:
        return Response({'error': 'Invalid preferences'}, status=400)
    

    # Creación de usuario y preferencias
    try:
        user = User.objects.create(
            name=data['name'], 
            email=data['email'], 
            affiliate=data['affiliate'] == 'true'
        )
        for pref in preferences:
            Preference.objects.create(user=user, preference=pref)
    except Exception as e:
        return Response({'error': str(e)}, status=400)

    return Response({'message': 'User created successfully'})

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    user_list = []
    
    for user in users:
        preferences = Preference.objects.filter(user=user).values_list('preference', flat=True)
        user_data = {
            'name': user.name,
            'email': user.email,
            'preferences': sorted(list(preferences)),  # Orden alfabético
            'affiliate': user.affiliate,
        }
        user_list.append(user_data)
    
    return Response({'users': user_list})