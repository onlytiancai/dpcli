#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
DNSPod命令行版
'''
import os
import sys
import json
import string
import urllib
import urllib2
import argparse

BASE_URI = 'https://dnsapi.cn'
DP_LOGIN_TOKEN = os.environ.get('DP_LOGIN_TOKEN')

if not DP_LOGIN_TOKEN:
    print u'DP_LOGIN_TOKEN environment variable not found.'
    sys.exit()

cmd_groups = {
    'domain': ['create', 'list', 'remove', 'status', 'info'],
    'record': ['create', 'list', 'remove', 'modify', 'remark'],
}


def encode(obj):
    if not isinstance(obj, basestring):
        return str(obj)

    english = True
    for s in obj:
        if s not in string.printable:
            english = False

    return obj if english else repr(obj)

def print_fields(key, obj, args):
    sep = ' ' if args.inline else '\n'
    keys = obj.keys()
    if args.fields != 'all' and key != 'status':
        keys = [k.strip() for k in args.fields.split(',')]
        keys = [k for k in keys if k in obj.keys()]
    print sep.join(['%s.%s: %s' % (key, k, encode(obj[k])) for k in sorted(keys)])


def print_result(rsp, args):
    for key in rsp:
        if isinstance(rsp[key], dict):
            print '=' * 20, key
            print_fields(key, rsp[key], args)
        elif isinstance(rsp[key], list):
            for i, obj in enumerate(rsp[key]):
                print '=' * 20, key, i
                print_fields(key, obj, args)


def domain_api(cmd, subcmd, args):
    try:
        api = '%s/%s.%s' % (BASE_URI, cmd.capitalize(), subcmd.capitalize())
        data = dict(arg.split('=') for arg in args.args if arg.find('=') > 0)
        print api, data
        data.update({"login_token": DP_LOGIN_TOKEN, "format": "json"})
        rsp = urllib2.urlopen(url=api, data=urllib.urlencode(data))
        print_result(json.loads(rsp.read()), args)
    except Exception, ex:
        raise
        print ex

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description=__doc__)
sub_group = parser.add_subparsers(title='subcommands')
for group_name in cmd_groups:
    group = sub_group.add_parser(group_name)
    sub_cmd = group.add_subparsers()
    for cmd in cmd_groups[group_name]:
        p = sub_cmd.add_parser(cmd)
        p.add_argument('args', type=str, nargs='*')
        p.add_argument('-inline', default=False,  action='store_true')
        p.add_argument('-fields', default='all')


if __name__ == '__main__':
    args = parser.parse_args()
    domain_api(sys.argv[1], sys.argv[2], args)
