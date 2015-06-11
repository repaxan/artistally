from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r"^$", "aa_app.views.root")
    url(r"^admin/", include(admin.site.urls)),
    url(r"^signup$", "aa_app.views.signup",
    url(r"^login$", "aa_app.views.login",

    url(r'^user/([0-9A-Za-z_\-]+)$', "aa_app.views.user"),
    url(r'^convention/([0-9]+)$', "aa_app.views.convention"),
    url(r'^item/([0-9]+)$', "aa_app.views.item"),

    url(r"^api/user/newUser$", "aa_app.views.api.user.newUser"),
    url(r"^api/user/login$", "aa_app.views.api.user.login"),
    url(r"^api/user/logout$", "aa_app.views.api.user.logout"),
    url(r"^api/user/setEmail$", "aa_app.views.api.user.setEmail"),
    url(r"^api/user/setPassword$", "aa_app.views.api.user.setPassword"),
    url(r"^api/user/setUsername$", "aa_app.views.api.user.setUsername"),
    url(r"^api/item/newItem$", "aa_app.views.api.item.newItem"),
    url(r"^api/item/setNumSold$", "aa_app.views.api.item.setNumSold"),
    url(r"^api/item/setNumLeft$", "aa_app.views.api.item.setNumLeft"),
    url(r"^api/writeup/newWriteup$", "aa_app.views.api.writeup.newWriteup"),
    url(r"^api/writeup/setRating$", "aa_app.views.api.writeup.setRating"),
    url(r"^api/writeup/setReview$", "aa_app.views.api.writeup.setReview"),
    url(r"^api/writeup/setMiscCosts$", "aa_app.views.api.writeup.setMiscCosts"),
    url(r"^api/fandom/newFandom$", "aa_app.views.api.fandom.newFandom"),
    url(r"^api/fandom/setName$", "aa_app.views.api.fandom.setName"),
    url(r"^api/kind/newKind$", "aa_app.views.api.kind.newKind"),
    url(r"^api/kind/setName$", "aa_app.views.api.kind.setName"),
    url(r"^api/convention/newConvention$", "aa_app.views.api.convention.newConvention"),
    url(r"^api/convention/setName$", "aa_app.views.api.convention.setName"),
    url(r"^api/convention/setNumAttenders$", "aa_app.views.api.convention.setNumAttenders"),
    url(r"^api/convention/setLocation$", "aa_app.views.api.convention.setLocation"),
    url(r"^api/convention/setStartDate$", "aa_app.views.api.convention.setStartDate"),
    url(r"^api/convention/setEndDate$", "aa_app.views.api.convention.setEndDate"),
]
