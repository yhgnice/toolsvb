#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nice... on '2017/3/9 11:00'

from django import forms

class LoginForm(forms.Form):
	Username = forms.CharField(required=True)
	Password = forms.CharField(required=True,min_length=6)

 