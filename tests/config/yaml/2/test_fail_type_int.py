# The MIT License (MIT)
#
# Copyright (c) 2020 Philippe Proulx <pproulx@efficios.com>
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

def test_align_0(request, config_fail_test):
    config_fail_test(request, 'type-int/align-0')


def test_align_3(request, config_fail_test):
    config_fail_test(request, 'type-int/align-3')


def test_align_invalid_type(request, config_fail_test):
    config_fail_test(request, 'type-int/align-invalid-type')


def test_base_invalid_type(request, config_fail_test):
    config_fail_test(request, 'type-int/base-invalid-type')


def test_base_invalid(request, config_fail_test):
    config_fail_test(request, 'type-int/base-invalid')


def test_bo_invalid_type(request, config_fail_test):
    config_fail_test(request, 'type-int/bo-invalid-type')


def test_bo_invalid(request, config_fail_test):
    config_fail_test(request, 'type-int/bo-invalid')


def test_pm_invalid_type(request, config_fail_test):
    config_fail_test(request, 'type-int/pm-invalid-type')


def test_pm_property_invalid(request, config_fail_test):
    config_fail_test(request, 'type-int/pm-property-invalid')


def test_pm_type_invalid(request, config_fail_test):
    config_fail_test(request, 'type-int/pm-type-invalid')


def test_pm_unknown_clock(request, config_fail_test):
    config_fail_test(request, 'type-int/pm-unknown-clock')


def test_signed_invalid_type(request, config_fail_test):
    config_fail_test(request, 'type-int/signed-invalid-type')


def test_size_0(request, config_fail_test):
    config_fail_test(request, 'type-int/size-0')


def test_size_65(request, config_fail_test):
    config_fail_test(request, 'type-int/size-65')


def test_size_invalid_type(request, config_fail_test):
    config_fail_test(request, 'type-int/size-invalid-type')


def test_size_no(request, config_fail_test):
    config_fail_test(request, 'type-int/size-no')


def test_unknown_prop(request, config_fail_test):
    config_fail_test(request, 'type-int/unknown-prop')
