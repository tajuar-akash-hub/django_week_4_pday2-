from django.shortcuts import render
from musicians.models import musician_Model
from albums.models import albums_Model


def home(request):
    musican_data = musician_Model.objects.all()
    album_data = albums_Model.objects.all()

    combined_data=[]
    for musician, album in zip(musican_data, album_data):
        
        musician_Album_data = {
            'Musician_id': musician.id,
            'album_id': album.id,
            'Musician_Name': musician.first_name,
            'Email': musician.email,
            'Album_Rating': album.album_rating,
            'Instrument_Type': musician.instrument_type,
            'Album_Name': album.album_name,
            'Release_Date': album.album_release_date,
        }
        combined_data.append(musician_Album_data)
        
        
    return render(request,"./home.html",{'combined_data':combined_data})
