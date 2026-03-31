from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from .models import Issue

def home(request):
    """Display home page with quick access to main features."""
    issues_count = Issue.objects.count()
    resolved_count = Issue.objects.filter(status='resolved').count()
    pending_count = Issue.objects.exclude(status='resolved').count()
    
    context = {
        'total_issues': issues_count,
        'resolved_issues': resolved_count,
        'pending_issues': pending_count,
    }
    return render(request, 'issues/home.html', context)

def issues_list(request):
    """Display all reported issues with filtering and sorting."""
    issues = Issue.objects.all()
    
    # Filter by status
    status = request.GET.get('status')
    if status:
        issues = issues.filter(status=status)
    
    # Filter by issue type
    issue_type = request.GET.get('type')
    if issue_type:
        issues = issues.filter(issue_type=issue_type)
    
    # Filter by priority
    priority = request.GET.get('priority')
    if priority:
        issues = issues.filter(priority=priority)
    
    context = {
        'issues': issues,
        'status_choices': Issue.STATUS_CHOICES,
        'type_choices': Issue.ISSUE_TYPES,
    }
    return render(request, 'issues/issue_list.html', context)

def issue_detail(request, issue_id):
    """Display detailed view of a single issue."""
    try:
        issue = Issue.objects.get(id=issue_id)
    except Issue.DoesNotExist:
        return render(request, '404.html', status=404)
    
    context = {'issue': issue}
    return render(request, 'issues/issue_detail.html', context)
