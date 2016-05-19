## DNSPod命令行版

DNSPod命令行版, 需要申请login_token，参考：https://support.dnspod.cn/Kb/showarticle/tsid/227/

帮助

    python dpcli.py --help
    python dpcli.py domain --help
    python dpcli.py record --help

示例
    
    # 设置login_token环境变量
    export DP_LOGIN_TOKEN='10000,e31588236fe82510c7'
    # 查看域名列表
    python dpcli.py domain list
    # 查看mydomain.com记录列表
    python dpcli.py record list domain=mydomain.com
    # 给mydomain.com添加一条记录
    python dpcli.py record create domain=mydomain.com sub_domain=www record_type=A record_line=默认 value=8.8.8.8

