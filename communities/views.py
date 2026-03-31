from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Q
from .models import Community
from issues.models import Issue

def communities_list(request):
    """Display all communities and access to local information."""
    communities = Community.objects.filter(active=True)
    
    # Get issue statistics for each community
    communities_stats = []
    for community in communities:
        stats = {
            'community': community,
            'total_issues': Issue.objects.filter(location__icontains=community.location).count(),
            'resolved_issues': Issue.objects.filter(location__icontains=community.location, status='resolved').count(),
            'pending_issues': Issue.objects.filter(location__icontains=community.location).exclude(status='resolved').count(),
        }
        communities_stats.append(stats)
    
    context = {'communities_stats': communities_stats}
    return render(request, 'communities/communities_list.html', context)

def community_detail(request, community_id):
    """Display detailed information about a specific community and its issues."""
    community = get_object_or_404(Community, id=community_id, active=True)
    
    # Get issues related to this community
    issues = Issue.objects.filter(location__icontains=community.location)
    
    # Statistics
    stats = {
        'total_issues': issues.count(),
        'resolved': issues.filter(status='resolved').count(),
        'in_progress': issues.filter(status='in_progress').count(),
        'reported': issues.filter(status='reported').count(),
        'rejected': issues.filter(status='rejected').count(),
    }
    
    context = {
        'community': community,
        'issues': issues,
        'stats': stats,
    }
    return render(request, 'communities/community_detail.html', context)
