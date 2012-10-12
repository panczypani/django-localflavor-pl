=====================
django_localflavor_pl
=====================

Country-specific Django helpers for Poland.

What's in the Poland localflavor?
=================================

* forms.PLPESELField: A form field that validates input as a Polish national
  identification number (PESEL_).

* forms.PLNationalIDCardNumberField: A form field that validates input as a
  Polish National ID Card number. The valid format is AAAXXXXXX, where A is
  letter (A-Z), X is digit and left-most digit is checksum digit. More
  information about checksum calculation algorithm see `Polish identity card`_.

* forms.PLREGONField: A form field that validates input as a Polish National
  Official Business Register Number (REGON_), having either seven or nine
  digits. The checksum algorithm used for REGONs is documented at
  http://wipos.p.lodz.pl/zylla/ut/nip-rego.html.

* forms.PLPostalCodeField: A form field that validates input as a Polish postal
  code. The valid format is XX-XXX, where X is a digit.

* forms.PLNIPField: A form field that validates input as a Polish Tax Number
  (NIP). Valid formats are XXX-XXX-XX-XX, XXX-XX-XX-XXX or XXXXXXXXXX. The
  checksum algorithm used for NIPs is documented at
  http://wipos.p.lodz.pl/zylla/ut/nip-rego.html.

* forms.PLCountySelect: A ``Select`` widget that uses a list of Polish
  administrative units as its choices.

* forms.PLProvinceSelect: A ``Select`` widget that uses a list of Polish
  voivodeships (administrative provinces) as its choices.

.. _PESEL: http://en.wikipedia.org/wiki/PESEL
.. _`Polish identity card`: http://en.wikipedia.org/wiki/Polish_identity_card
.. _REGON: http://www.stat.gov.pl/bip/regon_ENG_HTML.htm

See the source code for full details.

About localflavors
==================

Django's "localflavor" packages offer additional functionality for particular
countries or cultures.

For example, these might include form fields for your country's postal codes,
phone number formats or government ID numbers.

This code used to live in Django proper -- in django.contrib.localflavor -- but
was separated into standalone packages in Django 1.5 to keep the framework's
core clean.

For a full list of available localflavors, see https://github.com/django/
