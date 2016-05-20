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

    # 查看ihuhao.com记录列表
    python dpcli.py record list domain=ihuhao.com

    # 给ihuhao.com添加一条记录
    python dpcli.py record create domain=ihuhao.com sub_domain=www \
        record_type=A record_line=默认 value=8.8.8.8
   
    # 显示ihuhao.com下所有记录，记录属性放在一行内，方便进行grep, awk等过滤 
    python dpcli.py record list domain=ihuhao.com -inline 

    # 显示ihuhao.com下所有记录，记录属性放在一行内，且只显示记录类型和记录值
    python dpcli.py record list domain=ihuhao.com -inline -fields=type,value

    #查看ihuhao.com下所有A记录去重后的ip列表
    python dpcli.py record list domain=ihuhao.com -fields=type,value -inline \
        | grep "records.type: A" | awk '{print $4}' | sort | uniq

    # 探测ihuhoa.com下所有A记录IP的80端口能否访问通
    python dpcli.py record list domain=ihuhao.com -fields=type,value -inline \
        | grep "records.type: A" | awk '{print $4}' | sort | uniq \
        | xargs -I {} nc -v -w 1 {} -z 80
