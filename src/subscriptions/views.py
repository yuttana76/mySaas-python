from django.shortcuts import render

from subscriptions.models import SubscriptionPrice

def subscription_price_view(request, *args, **kwargs):
    """
    Subscription Price View
    """

    qs = SubscriptionPrice.objects.filter(
        featured=True,
    ).order_by("-order")

    montyly_qs = qs.filter(
        interval=SubscriptionPrice.IntervalChoices.MONTHLY,
    ).order_by("subscription__order")
    yearly_qs = qs.filter(
        interval=SubscriptionPrice.IntervalChoices.YEARLY,
    )

    return render(request, "subscriptions/pricing.html", {
        "monthly_qs": montyly_qs,
        "yearly_qs": yearly_qs,
    })