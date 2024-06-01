#!/bin/bash
set -e

# 默认服务出网网卡地址：访问Pilot服务的IP地址
net_ip=127.0.0.1

# 默认服务映射端口：前端/后端/数据库
nginx_port=8088
web_port=8089
mysql_port=3306
pgsql_port=5432
mssql_port=1433

# 默认数据库用户密码：mysql:root/mssql:sa/pgsql:postgres
mysql_password=fanqie
mssql_password=Fanqie.1433
pgsql_password=fanqie


### 以下部分不可修改
docker_compose_file="./docker-compose.yml"
nginx_dockerfile="./pilot-client/Dockerfile.pilot"
web_dockerfile="./pilot-server/Dockerfile.app"
mysql_dockerfile="./sqldata/Dockerfile.mysql"
pgsql_dockerfile="./sqldata/Dockerfile.pgsql"
mssql_dockerfile="./sqldata/Dockerfile.mssql"

init_help=false
clean_docker_services=false
run_docker_services=false

for arg in "$@"; do
  key="${arg%%=*}" 
  value="${arg#*=}" 
  case $key in
    -h|help)
    init_help=true
    ;;
    -up)
    run_docker_services=true
    ;;
    -cld)
    clean_docker_services=true
    ;;
    net_ip|-ip)
    net_ip="$value"
    ;;
    web_port|-wpt)
    web_port="$value"
    ;;
    nginx_port|-npt)
    nginx_port="$value"
    ;;
    mysql_port|-mypt)
    mysql_port="$value"
    ;;
    pgsql_port|-pgpt)
    pgsql_port="$value"
    ;;
    mssql_port|-mspt)
    mssql_port="$value"
    ;;
    mysql_password|-mypd)
    mysql_password="$value"
    ;;
    mssql_password|-mspd)
    mssql_password="$value"
    ;;
    pgsql_password|-pgpd)
    pgsql_password="$value"
    ;;
    *)
    init_help=true
    ;;
  esac
done

if $init_help; 
then
echo "
██████╗ ██╗██╗      █████╗ ████████╗       ██╗       ██╗███████╗██████╗ 
██╔══██╗██║██║     ██╔══██╗╚══██╔══╝       ██║  ██╗  ██║██╔════╝██╔══██╗
██████╔╝██║██║     ██║  ██║   ██║   █████╗ ╚██╗████╗██╔╝█████╗  ██████╦╝
██╔═══╝ ██║██║     ██║  ██║   ██║   ╚════╝  ████╔═████║ ██╔══╝  ██╔══██╗
██║     ██║███████╗╚█████╔╝   ██║           ╚██╔╝ ╚██╔╝ ███████╗██████╦╝
╚═╝     ╚═╝╚══════╝ ╚════╝    ╚═╝            ╚═╝   ╚═╝  ╚══════╝╚═════╝  
"
    echo "当前启动配置："
    echo "--WEB页面地址/靶场访问地址：http://${net_ip}:${nginx_port}"
    echo "--API地址：http://${net_ip}:${web_port}"
    echo ""
    echo "--MySQL服务地址：${net_ip}:${mysql_port}"
    echo "--MySQL账户/密码：root/${mysql_password}"
    echo ""
    echo "--PostgreSQL服务地址：${net_ip}:${pgsql_port}"
    echo "--PostgreSQL账户/密码：postgres/${pgsql_password}"
    echo ""
    echo "--MSSQL服务地址：${net_ip}:${mssql_port}"
    echo "--MSSQL账户/密码：sa/${mssql_password}"
    echo ""
    echo "Pilot靶场init.sh安装脚本参数说明："
    echo "    -h | help：显示帮助信息"
    echo "    -up：初始化后自动编译与启动Docker容器，请确保Docker与Docker-compose环境正常"
    echo "    -cld：初始化后自动清理Docker容器与镜像，请确保Docker与Docker-compose环境正常"
    echo ""
    echo "    -ip | net_ip：自定义服务访问IP地址"
    echo "    -npt | nginx_port：自定义Pilot服务访问端口"
    echo "    -wpt | web_port：自定义API端口"
    echo "    -mypt | mysql_port：自定义MySQL端口"
    echo "    -pgpt | pgsql_port：自定义PostgreSQL端口"
    echo "    -mspt | mssql_port：自定义MSSQL端口"
    echo ""
    echo "    -mypd | mysql_password：自定义MySQL服务密码"
    echo "    -pgpd | pgsql_password：自定义PostgreSQL服务密码"
    echo "    -mspd | mssql_password：自定义MSSQL服务密码（MSSQL对密码有一定要求，请勿任意修改！）"
    echo ""
    echo "    不添加任何参数，脚本会以默认配置进行初始化，默认参数可以在脚本中修改。"
    echo ""
    exit 0    
fi

sed -i -r "s/([\"']?)([0-9]+)(:[0-9]+[\"']?\s*#.web_port@)/\1${web_port}\3/g" "$docker_compose_file"
sed -i -r "s/([\"']?)([0-9]+)(:[0-9]+[\"']?\s*#.nginx_port@)/\1${nginx_port}\3/g" "$docker_compose_file"
sed -i -r "s/([\"']?)([0-9]+)(:[0-9]+[\"']?\s*#.mysql_port@)/\1${mysql_port}\3/g" "$docker_compose_file"
sed -i -r "s/([\"']?)([0-9]+)(:[0-9]+[\"']?\s*#.pgsql_port@)/\1${pgsql_port}\3/g" "$docker_compose_file"
sed -i -r "s/([\"']?)([0-9]+)(:[0-9]+[\"']?\s*#.mssql_port@)/\1${mssql_port}\3/g" "$docker_compose_file"

sed -i "s/ENV NET_IP=.*/ENV NET_IP=${net_ip}/" $nginx_dockerfile
sed -i "s/ENV NGINX_PORT=.*/ENV NGINX_PORT=${nginx_port}/" $nginx_dockerfile
sed -i "s/ENV FLASK_PORT=.*/ENV FLASK_PORT=${web_port}/" $nginx_dockerfile

sed -i "s/ENV NET_IP=.*/ENV NET_IP=${net_ip}/" $web_dockerfile
sed -i "s/ENV MYSQL_PORT=.*/ENV MYSQL_PORT=${mysql_port}/" $web_dockerfile
sed -i "s/ENV MYSQL_PASSWORD=.*/ENV MYSQL_PASSWORD=${mysql_password}/" $web_dockerfile
sed -i "s/ENV MSSQL_PORT=.*/ENV MSSQL_PORT=${mssql_port}/" $web_dockerfile
sed -i "s/ENV MSSQL_PASSWORD=.*/ENV MSSQL_PASSWORD=${mssql_password}/" $web_dockerfile
sed -i "s/ENV POSTGRES_PORT=.*/ENV POSTGRES_PORT=${pgsql_port}/" $web_dockerfile
sed -i "s/ENV POSTGRES_PASSWORD=.*/ENV POSTGRES_PASSWORD=${pgsql_password}/" $web_dockerfile

sed -i "s/ENV MYSQL_ROOT_PASSWORD=.*/ENV MYSQL_ROOT_PASSWORD=${mysql_password}/" $mysql_dockerfile
sed -i "s/ENV SA_PASSWORD=.*/ENV SA_PASSWORD=${mssql_password}/" $mssql_dockerfile
sed -i "s/ENV POSTGRES_PASSWORD=.*/ENV POSTGRES_PASSWORD=${pgsql_password}/" $pgsql_dockerfile

echo "--> Pilot靶场初始化完成，请清理旧镜像与容器后重新编译开启，或在调用脚本时直接追加 -up -cld 参数！"

if $clean_docker_services; 
then
    echo ""
    echo "--> 正在清理旧Docker容器与镜像..."
    docker-compose stop
    docker rm $(docker ps -a | grep "pilot" | awk '{print $1}')
    docker rmi $(docker images | grep "pilot" | awk '{print $3}')
    echo ""
    echo "--> 清理完成"
fi

if $run_docker_services; 
then
    echo ""
    echo "--> 开始编译并尝试打开Docker容器与镜像..."
    echo "--> docker-compose up -d"
    docker-compose up -d
    echo ""
    echo "--> 靶场环境搭建完成，Happy hacking!"
fi
echo "
██████╗ ██╗██╗      █████╗ ████████╗       ██╗       ██╗███████╗██████╗ 
██╔══██╗██║██║     ██╔══██╗╚══██╔══╝       ██║  ██╗  ██║██╔════╝██╔══██╗
██████╔╝██║██║     ██║  ██║   ██║   █████╗ ╚██╗████╗██╔╝█████╗  ██████╦╝
██╔═══╝ ██║██║     ██║  ██║   ██║   ╚════╝  ████╔═████║ ██╔══╝  ██╔══██╗
██║     ██║███████╗╚█████╔╝   ██║           ╚██╔╝ ╚██╔╝ ███████╗██████╦╝
╚═╝     ╚═╝╚══════╝ ╚════╝    ╚═╝            ╚═╝   ╚═╝  ╚══════╝╚═════╝  
"
echo ""
echo "靶场配置信息："
echo "--WEB页面地址/靶场访问地址：http://${net_ip}:${nginx_port}"
echo "--API地址：http://${net_ip}:${web_port}"
echo ""
echo "--MySQL服务地址：${net_ip}:${mysql_port}"
echo "--MySQL账户/密码：root/${mysql_password}"
echo ""
echo "--PostgreSQL服务地址：${net_ip}:${pgsql_port}"
echo "--PostgreSQL账户/密码：postgres/${pgsql_password}"
echo ""
echo "--MSSQL服务地址：${net_ip}:${mssql_port}"
echo "--MSSQL账户/密码：sa/${mssql_password}"
echo ""