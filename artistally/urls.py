from django.conf.urls import include, url
from django.contrib import admin

import django.views.defaults
import aa_app.views.site
import aa_app.views.api.convention
import aa_app.views.api.event
import aa_app.views.api.fandom
import aa_app.views.api.item
import aa_app.views.api.kind
import aa_app.views.api.miscCost
import aa_app.views.api.user
import aa_app.views.api.util
import aa_app.views.api.writeup

import datetime


urlpatterns = [
    url(r"^$", aa_app.views.site.root),
    url(r"^404$", django.views.defaults.page_not_found),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^about$", aa_app.views.site.about),
    url(r"^signup$", aa_app.views.site.signup),
    url(r"^login$", aa_app.views.site.login),
    url(r"^forgot$", aa_app.views.site.forgot),
    url(r"^confirm$", aa_app.views.site.confirm),
    url(r"^inventory$", aa_app.views.site.inventory),
    url(r"^inventory/([0-9]+)?$", aa_app.views.site.inventory),
    url(r"^myconventions$", aa_app.views.site.myconventions),
    url(r"^mywriteups$", aa_app.views.site.mywriteups),
    url(r"^addconvention$", aa_app.views.site.addconvention),
    url(r"^addevent/([0-9]+)$", aa_app.views.site.addevent),
    url(r"^editconvention/([0-9]+)$", aa_app.views.site.editconvention),
    url(r"^editevent/([0-9]+)$", aa_app.views.site.editevent),
    url(r"^user/([0-9A-Za-z_\-]+)$", aa_app.views.site.user),
    url(r"^edituser$", aa_app.views.site.edituser),
    url(r"^convention/([0-9]+)$", aa_app.views.site.convention),
    url(r"^event/([0-9]+)$", aa_app.views.site.event),
    url(r"^eventreviews/([0-9]+)$", aa_app.views.site.eventreviews),
    url(r"^writeup/([0-9]+)$", aa_app.views.site.writeup),
    url(r"^search$", aa_app.views.site.search),
    url(r"^search/(.*)$", aa_app.views.site.search),
    url(r"^api/user/newUser$", aa_app.views.api.user.newUser),
    url(r"^api/user/login$", aa_app.views.api.user.login),
    url(r"^api/user/logout$", aa_app.views.api.user.logout),
    url(r"^api/user/resendConfirmEmail$", aa_app.views.api.user.resendConfirmEmail),
    url(r"^api/user/checkConfirmToken$", aa_app.views.api.user.checkConfirmToken),
    url(r"^api/user/requestReset$", aa_app.views.api.user.requestReset),
    url(r"^api/user/checkResetToken$", aa_app.views.api.user.checkResetToken),
    url(r"^api/user/setEmail$", aa_app.views.api.user.setEmail),
    url(r"^api/user/setPassword$", aa_app.views.api.user.setPassword),
    url(r"^api/user/setStartYear$", aa_app.views.api.user.setStartYear),
    url(r"^api/user/setImage$", aa_app.views.api.user.setImage),
    url(r"^api/user/setDescription$", aa_app.views.api.user.setDescription),
    url(r"^api/user/setWebsite1$", aa_app.views.api.user.setWebsite1),
    url(r"^api/user/setWebsite2$", aa_app.views.api.user.setWebsite2),
    url(r"^api/user/setWebsite3$", aa_app.views.api.user.setWebsite3),
    url(r"^api/item/newItem$", aa_app.views.api.item.newItem),
    url(r"^api/item/deleteItem$", aa_app.views.api.item.deleteItem),
    url(r"^api/item/setNumSold$", aa_app.views.api.item.setNumSold),
    url(r"^api/item/setNumLeft$", aa_app.views.api.item.setNumLeft),
    url(r"^api/item/setName$", aa_app.views.api.item.setName),
    url(r"^api/item/setImage$", aa_app.views.api.item.setImage),
    url(r"^api/item/setPrice$", aa_app.views.api.item.setPrice),
    url(r"^api/item/setCost$", aa_app.views.api.item.setCost),
    url(r"^api/item/setFandom$", aa_app.views.api.item.setFandom),
    url(r"^api/item/setKind$", aa_app.views.api.item.setKind),
    url(r"^api/writeup/newWriteup$", aa_app.views.api.writeup.newWriteup),
    url(r"^api/writeup/setRating$", aa_app.views.api.writeup.setRating),
    url(r"^api/writeup/setReview$", aa_app.views.api.writeup.setReview),
    url(r"^api/writeup/deleteWriteup$", aa_app.views.api.writeup.deleteWriteup),
    url(r"^api/miscCost/newMiscCost$", aa_app.views.api.miscCost.newMiscCost),
    url(r"^api/miscCost/deleteMiscCost$", aa_app.views.api.miscCost.deleteMiscCost),
    url(r"^api/miscCost/setName$", aa_app.views.api.miscCost.setName),
    url(r"^api/miscCost/setAmount$", aa_app.views.api.miscCost.setAmount),
    url(r"^api/fandom/newFandom$", aa_app.views.api.fandom.newFandom),
    url(r"^api/fandom/setName$", aa_app.views.api.fandom.setName),
    url(r"^api/kind/newKind$", aa_app.views.api.kind.newKind),
    url(r"^api/kind/setName$", aa_app.views.api.kind.setName),
    url(r"^api/convention/newConvention$", aa_app.views.api.convention.newConvention),
    url(r"^api/convention/setName$", aa_app.views.api.convention.setName),
    url(r"^api/convention/setWebsite$", aa_app.views.api.convention.setWebsite),
    url(r"^api/convention/setImage$", aa_app.views.api.convention.setImage),
    url(r"^api/event/newEvent$", aa_app.views.api.event.newEvent),
    url(r"^api/event/setName$", aa_app.views.api.event.setName),
    url(r"^api/event/setNumAttenders$", aa_app.views.api.event.setNumAttenders),
    url(r"^api/event/setLocation$", aa_app.views.api.event.setLocation),
    url(r"^api/event/setStartDate$", aa_app.views.api.event.setStartDate),
    url(r"^api/event/setEndDate$", aa_app.views.api.event.setEndDate),
    url(r"^api/event/copyInventory$", aa_app.views.api.event.copyInventory),
    url(r"^api/event/recopyInventory$", aa_app.views.api.event.recopyInventory),
    url(r"^api/event/spillInventory$", aa_app.views.api.event.spillInventory),
    url(r"^api/event/respillInventory$", aa_app.views.api.event.respillInventory),
    url(r"^api/event/setUser$", aa_app.views.api.event.setUser),
    url(r"^api/event/unsetUser$", aa_app.views.api.event.unsetUser),
    url(r"^api/util/uploadFile$", aa_app.views.api.util.uploadFile),
    url(r"^api/util/findFandom$", aa_app.views.api.util.findFandom),
    url(r"^api/util/findKind$", aa_app.views.api.util.findKind),
    url(r"^api/util/contactUs$", aa_app.views.api.util.contactUs),
]
