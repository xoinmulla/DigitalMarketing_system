from .models import Campaign
from .forms import CampaignForm
from .models import Ad
from .forms import AdForm
from django.shortcuts import render, redirect, get_object_or_404

from .models import Ad, Campaign

from django.shortcuts import render, redirect
from .models import Campaign, Ad

def create_ad(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        campaign_id = request.POST.get('campaign_id')
        image = request.FILES.get('image')
        link = request.POST.get('link')

        if title and campaign_id and image and link:
            campaign = Campaign.objects.get(id=campaign_id)
            Ad.objects.create(
                title=title,
                image=image,
                link=link,
                campaign=campaign
            )
            return redirect('ad_list')  # or your view name

    ads = Ad.objects.all()
    campaigns = Campaign.objects.all()  # ✅ this is what fills the select box
    return render(request, 'marketing/create_ad.html', {'ads': ads, 'campaigns': campaigns})



def ad_list(request):
    ads = Ad.objects.all()
    
    # Increment views each time the page is loaded
    for ad in ads:
        ad.increment_views()
    
    return render(request, 'marketing/ad_list.html', {'ads': ads})



def track_click(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    ad.increment_clicks()
    return redirect(ad.link)  # Redirect to the ad's link

def ad_list(request):
    ads = Ad.objects.all()
    print("Number of ads:", ads.count())  # Debugging
    return render(request, 'marketing/ad_list.html', {'ads': ads})


def campaign_list(request):
    campaigns = Campaign.objects.all()
    return render(request, 'marketing/campaign_list.html', {'campaigns': campaigns})

from django.shortcuts import render, redirect
from .forms import CampaignForm  # Import your form
from .models import Campaign  # Import your model

def create_campaign(request):
    if request.method == "POST":
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save(commit=False)  # Don't save yet
            campaign.created_by = request.user  # Assign logged-in user
            campaign.save()  # Now save
            return redirect('campaign_list')  # Redirect after success
    else:
        form = CampaignForm()
    
    return render(request, 'marketing/create_campaign.html', {'form': form})


# accounts/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'accounts/home.html')  # Create a template named 'home.html'


# accounts/views.py
# accounts/views.py
from django.shortcuts import render

def profile(request):
    # Add context if necessary
    return render(request, 'accounts/profile.html')


