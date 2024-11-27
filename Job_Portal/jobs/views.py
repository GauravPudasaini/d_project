from django.shortcuts import render

def browse_jobs(request):
    return render(request, 'jobs/browse_jobs.html')  # Renders the browse jobs page

def about_us(request):
    return render(request, 'jobs/about.html')  # Renders the about page
