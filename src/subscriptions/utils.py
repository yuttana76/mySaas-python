import helpers.billing

from django.db.models import Q
from customers.models import Customer
from subscriptions.models import Subscription, UserSubscription,SubscriptionStatus

def refresh_user_subscriptions(
          user_ids=None,
          active_only=True,
          day_start=0,
          day_end=0,
          days_left=0,
          days_ago=0,
          verbose=False):
    """
    Sync user subscriptions with Stripe
    """
    # qs = UserSubscription.objects.all()
    # METHOD 1
    # active_qs = qs.filter(status= SubscriptionStatus.ACTIVE)
    # trialing_qs = qs.filter(status= SubscriptionStatus.TRIALING)
    # qs = (active_qs | trialing_qs).distinct()

    # METHOD 2
    # active_qs_lookup = (
    #      Q(status=SubscriptionStatus.ACTIVE) |
    #      Q(status=SubscriptionStatus.TRIALING)
    # )
    # qs = qs.filter(active_qs_lookup).distinct().filter(user_id__in=user_ids)

    # METHOD 3
    # active_qs_lookup = (
    #      Q(status=SubscriptionStatus.ACTIVE) |
    #      Q(status=SubscriptionStatus.TRIALING)
    # )
    # qs = UserSubscription.objects.filter(active_qs_lookup).distinct()
    # # print(user_ids)
    # if isinstance(user_ids, list) and len(user_ids) > 0:
    #     qs = qs.filter(user_id__in=user_ids)
    # elif isinstance(user_ids, int):
    #     qs = qs.filter(user_id=[user_ids])
    # elif isinstance(user_ids, str):
    #     qs = qs.filter(user_id=[user_ids])

    # METHOD 4 use queryset

    qs = UserSubscription.objects.all()
    if active_only:
        qs = qs.by_active_trialing()
    if user_ids is not None:
         qs = qs.by_user_ids(user_ids=user_ids)
    if days_ago > 0:
        qs = qs.by_days_ago(days_ago=days_ago)
    if days_left > 0:
        qs = qs.by_days_left(days_left=days_left)
    if day_start > 0 and day_end > 0:
        qs = qs.by_range(day_start=day_start, day_end=day_end)

    # print(qs.query)

    compile_count = 0
    qs_count = qs.count()
    for obj in qs:
        if verbose:
            print("*** Updating user: " ,obj.user, obj.subscription,obj.current_period_end)
        if obj.stripe_id:
                sub_data = helpers.billing.get_subscription(obj.stripe_id,raw=False)
                for k,v in sub_data.items():
                    setattr(obj, k, v)
                obj.save()
                compile_count += 1
    return compile_count == qs_count

def clear_dangling_subs():
    qs = Customer.objects.filter(
        stripe_id__isnull=False,
        user__isnull=False
    ).prefetch_related(
        "user",
    )
    for customer_obj in qs:
        user = customer_obj.user
        customer_stripe_id = customer_obj.stripe_id
        print(f"*** Syncing  {user} - {customer_stripe_id} subs and remove old ones ***")

        subs = helpers.billing.get_customer_active_subscriptions(
            customer_stripe_id
        )
        # print("subs:",subs)
        for sub in subs:
            existing_user_subs_qs = UserSubscription.objects.filter(
                stripe_id__iexact=f"{sub.id}".strip(),
                user=user
            )

            if existing_user_subs_qs.exists():
                continue

            helpers.billing.cancel_subscription(
                sub.id,
                cancel_at_period_end=True,
                reason="Dangling active subscription",
            )
            print("sub:",sub.id, existing_user_subs_qs.exists())


def sync_subs_group_permissions():
        print("hello world")
        qs = Subscription.objects.filter(active=True)
        for obj in qs:
            # print(obj.name)
            # print(obj.groups.all())
            # print(obj.Subscription.all())
            sub_perms = obj.permissions.all()
            for group in obj.groups.all():
                group.permissions.set(sub_perms)