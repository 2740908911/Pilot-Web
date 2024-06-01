// 用于模板建设的 js

// 初始化
let body = document.body;
const baseUri = "http://{ENV:NET_IP}:{ENV:NGINX_PORT}/";
(() => {
    const Container = `<!-- Brand Logo -->
    <a href="index.html" class="brand-link">
      <img src="${baseUri}dist/img/pilot.png" alt="Pilot-fanqie" class="brand-image">
      <span class="brand-text font-weight-bold" style="font-size: 20px">Pilot-Web</span>
    </a>

    <!-- Sidebar -->
    <div class="sidebar" id="sidebar"></div>
    <!-- /.sidebar -->`
    const Sidebar_Menu = `<nav class="mt-2">
        <ul class="nav nav-pills nav-sidebar flex-column" data-widget="treeview" role="menu" data-accordion="true">
          <!-- Add icons to the links using the .nav-icon class
               with font-awesome or any other icon font library -->
          <li class="nav-item">
            <a href="${baseUri}index.html" class="nav-link">
              <i class="nav-icon fas fa-globe"></i>
              <p>
                主页
              </p>
            </a>
          </li>
          <li class="nav-item has-treeview" id="bruteforce">
            <a href="${baseUri}pages/bruteforce/index.html" class="nav-link">
              <i class="fas fa-fighter-jet nav-icon"></i>
              <p>
                暴力破解
                <i class="fas fa-angle-left right"></i>
              </p>
            </a>
            <ul class="nav nav-treeview">
              <li class="nav-item">
                <a href="${baseUri}pages/bruteforce/index.html" class="nav-link" id="bruteforce/index">
                  <i class="far nav-icon"></i>
                  <p>概述</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/bruteforce/bf_username.html" class="nav-link" id="bruteforce/bf_username">
                  <i class="far nav-icon"></i>
                  <p>用户名枚举</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/bruteforce/bf_password.html" class="nav-link" id="bruteforce/bf_password">
                  <i class="far nav-icon"></i>
                  <p>弱口令枚举</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/bruteforce/bf_token.html" class="nav-link" id="bruteforce/bf_token">
                  <i class="far nav-icon"></i>
                  <p>Token伪造</p>
                </a>
              </li>
            </ul>
          </li>
          <li class="nav-item has-treeview" id="vcdefect">
            <a href="${baseUri}pages/vcdefect/index.html" class="nav-link">
              <i class="fas fa-fighter-jet nav-icon"></i>
              <p>
                验证码缺陷
                <i class="fas fa-angle-left right"></i>
              </p>
            </a>
            <ul class="nav nav-treeview">
              <li class="nav-item">
                <a href="${baseUri}pages/vcdefect/index.html" class="nav-link" id="vcdefect/index">
                  <i class="far nav-icon"></i>
                  <p>概述</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/vcdefect/vc_bypass_c.html" class="nav-link" id="vcdefect/vc_bypass_c">
                  <i class="far nav-icon"></i>
                  <p>客户端验证码绕过</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/vcdefect/vc_bypass_s.html" class="nav-link" id="vcdefect/vc_bypass_s">
                  <i class="far nav-icon"></i>
                  <p>服务端验证码绕过</p>
                </a>
              </li>
            </ul>
          </li>
          <li class="nav-item has-treeview" id="infoleak">
            <a href="${baseUri}pages/infoleak/index.html" class="nav-link">
              <i class="fas fa-fighter-jet nav-icon"></i>
              <p>
                敏感信息泄露
                <i class="fas fa-angle-left right"></i>
              </p>
            </a>
            <ul class="nav nav-treeview">
              <li class="nav-item">
                <a href="${baseUri}pages/infoleak/index.html" class="nav-link" id="infoleak/index">
                  <i class="far nav-icon"></i>
                  <p>概述</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/infoleak/system_info.html" class="nav-link" id="infoleak/system_info">
                  <i class="far nav-icon"></i>
                  <p>系统信息泄露</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/infoleak/private_info.html" class="nav-link" id="infoleak/private_info">
                  <i class="far nav-icon"></i>
                  <p>隐私信息泄露</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/infoleak/account_info.html" class="nav-link" id="infoleak/account_info">
                  <i class="far nav-icon"></i>
                  <p>账户信息泄露</p>
                </a>
              </li>
            </ul>
          </li>
          <li class="nav-item has-treeview" id="authority">
            <a href="${baseUri}pages/authority/index.html" class="nav-link">
              <i class="fas fa-fighter-jet nav-icon"></i>
              <p>
                权限控制
                <i class="fas fa-angle-left right"></i>
              </p>
            </a>
            <ul class="nav nav-treeview">
              <li class="nav-item">
                <a href="${baseUri}pages/authority/index.html" class="nav-link" id="authority/index">
                  <i class="far nav-icon"></i>
                  <p>概述</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/authority/unauthorized.html" class="nav-link" id="authority/unauthorized">
                  <i class="far nav-icon"></i>
                  <p>未授权访问</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/authority/horizontal.html" class="nav-link" id="authority/horizontal">
                  <i class="far nav-icon"></i>
                  <p>水平越权</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/authority/vertical.html" class="nav-link" id="authority/vertical">
                  <i class="far nav-icon"></i>
                  <p>垂直越权</p>
                </a>
              </li>
            </ul>
          </li>
          <li class="nav-item has-treeview" id="sqli">
            <a href="${baseUri}pages/sqli/index.html" class="nav-link">
              <i class="fas fa-fighter-jet nav-icon"></i>
              <p>
                SQL注入
                <i class="fas fa-angle-left right"></i>
              </p>
            </a>
            <ul class="nav nav-treeview">
              <li class="nav-item">
                <a href="${baseUri}pages/sqli/index.html" class="nav-link" id="sqli/index">
                  <i class="far nav-icon"></i>
                  <p>概述</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/sqli/sqli_mysql.html" class="nav-link" id="sqli/sqli_mysql">
                  <i class="far nav-icon"></i>
                  <p>Mysql注入</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/sqli/sqli_mssql.html" class="nav-link" id="sqli/sqli_mssql">
                  <i class="far nav-icon"></i>
                  <p>Mssql注入</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/sqli/sqli_pgsql.html" class="nav-link" id="sqli/sqli_pgsql">
                  <i class="far nav-icon"></i>
                  <p>PostgreSql注入</p>
                </a>
              </li>
            </ul>  
          </li>
          <li class="nav-item has-treeview" id="xss">
            <a href="${baseUri}pages/xss/index.html" class="nav-link">
              <i class="fas fa-fighter-jet nav-icon"></i>
              <p>
                XSS跨站脚本
                <i class="fas fa-angle-left right"></i>
              </p>
            </a>
            <ul class="nav nav-treeview">
              <li class="nav-item">
                <a href="${baseUri}pages/xss/index.html" class="nav-link" id="xss/index">
                  <i class="far nav-icon"></i>
                  <p>概述</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/xss/xss_reflected.html" class="nav-link" id="xss/xss_reflected">
                  <i class="far nav-icon"></i>
                  <p>反射型XSS</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/xss/xss_stored.html" class="nav-link" id="xss/xss_stored">
                  <i class="far nav-icon"></i>
                  <p>存储型XSS</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/xss/xss_dom.html" class="nav-link" id="xss/xss_dom">
                  <i class="far nav-icon"></i>
                  <p>DOM型XSS</p>
                </a>
              </li>
            </ul>  
          </li>
          <li class="nav-item has-treeview" id="urlredirect">
            <a href="${baseUri}pages/urlredirect/index.html" class="nav-link">
              <i class="fas fa-fighter-jet nav-icon"></i>
              <p>
                URL重定向
                <i class="fas fa-angle-left right"></i>
              </p>
            </a>
            <ul class="nav nav-treeview">
              <li class="nav-item">
                <a href="${baseUri}pages/urlredirect/index.html" class="nav-link" id="urlredirect/index">
                  <i class="far nav-icon"></i>
                  <p>概述</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/urlredirect/urlredirect.html" class="nav-link" id="urlredirect/urlredirect">
                  <i class="far nav-icon"></i>
                  <p>不安全的URL跳转</p>
                </a>
              </li>
            </ul>  
          </li>
          <li class="nav-item has-treeview" id="ssrf">
            <a href="${baseUri}pages/ssrf/index.html" class="nav-link">
              <i class="fas fa-fighter-jet nav-icon"></i>
              <p>
                SSRF服务端请求伪造
                <i class="fas fa-angle-left right"></i>
              </p>
            </a>
            <ul class="nav nav-treeview">
              <li class="nav-item">
                <a href="${baseUri}pages/ssrf/index.html" class="nav-link" id="ssrf/index">
                  <i class="far nav-icon"></i>
                  <p>概述</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/ssrf/ssrf.html" class="nav-link" id="ssrf/ssrf">
                  <i class="far nav-icon"></i>
                  <p>SSRF远程解析</p>
                </a>
              </li>
            </ul>
          </li>
          <li class="nav-item has-treeview" id="csrf">
            <a href="${baseUri}pages/csrf/index.html" class="nav-link">
              <i class="fas fa-fighter-jet nav-icon"></i>
              <p>
                CSRF跨站请求伪造
                <i class="fas fa-angle-left right"></i>
              </p>
            </a>
            <ul class="nav nav-treeview">
              <li class="nav-item">
                <a href="${baseUri}pages/csrf/index.html" class="nav-link" id="csrf/index">
                  <i class="far nav-icon"></i>
                  <p>概述</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/csrf/csrf.html" class="nav-link" id="csrf/csrf">
                  <i class="far nav-icon"></i>
                  <p>CSRF</p>
                </a>
              </li>
            </ul>
          </li>
          <li class="nav-item has-treeview" id="upload">
            <a href="${baseUri}pages/upload/index.html" class="nav-link">
              <i class="fas fa-fighter-jet nav-icon"></i>
              <p>
                文件上传
                <i class="fas fa-angle-left right"></i>
              </p>
            </a>
            <ul class="nav nav-treeview">
              <li class="nav-item">
                <a href="${baseUri}pages/upload/index.html" class="nav-link" id="upload/index">
                  <i class="far nav-icon"></i>
                  <p>概述</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/upload/client.html" class="nav-link" id="upload/client">
                  <i class="far nav-icon"></i>
                  <p>前端校验</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/upload/server_1.html" class="nav-link" id="upload/server_1">
                  <i class="far nav-icon"></i>
                  <p>后端后缀黑名单</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/upload/server_2.html" class="nav-link" id="upload/server_2">
                  <i class="far nav-icon"></i>
                  <p>后端校验类型</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/upload/upload_dir.html" class="nav-link" id="upload/upload_dir">
                  <i class="far nav-icon"></i>
                  <p>目录穿越</p>
                </a>
              </li>
            </ul>
          </li>
          <li class="nav-item has-treeview" id="download">
            <a href="${baseUri}pages/download/index.html" class="nav-link">
              <i class="fas fa-fighter-jet nav-icon"></i>
              <p>
                文件下载
                <i class="fas fa-angle-left right"></i>
              </p>
            </a>
            <ul class="nav nav-treeview">
              <li class="nav-item">
                <a href="${baseUri}pages/download/index.html" class="nav-link" id="download/index">
                  <i class="far nav-icon"></i>
                  <p>概述</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/download/file_download.html" class="nav-link" id="download/file_download">
                  <i class="far nav-icon"></i>
                  <p>任意文件下载</p>
                </a>
              </li>
            </ul>
          </li>
          <li class="nav-item has-treeview" id="rce">
            <a href="${baseUri}pages/rce/index.html" class="nav-link">
              <i class="fas fa-fighter-jet nav-icon"></i>
              <p>
                RCE远程命令执行
                <i class="fas fa-angle-left right"></i>
              </p>
            </a>
            <ul class="nav nav-treeview">
              <li class="nav-item">
                <a href="${baseUri}pages/rce/index.html" class="nav-link" id="rce/index">
                  <i class="far nav-icon"></i>
                  <p>概述</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/rce/rce.html" class="nav-link" id="rce/rce">
                  <i class="far nav-icon"></i>
                  <p>命令执行</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/rce/rce_ping.html" class="nav-link" id="rce/rce_ping">
                  <i class="far nav-icon"></i>
                  <p>拼接命令执行</p>
                </a>
              </li>
            </ul>
          </li>
          <li class="nav-item has-treeview" id="ssti">
            <a href="${baseUri}pages/ssti/index.html" class="nav-link">
              <i class="fas fa-fighter-jet nav-icon"></i>
              <p>
                SSTI模板注入
                <i class="fas fa-angle-left right"></i>
              </p>
            </a>
            <ul class="nav nav-treeview">
              <li class="nav-item">
                <a href="${baseUri}pages/ssti/index.html" class="nav-link" id="ssti/index">
                  <i class="far nav-icon"></i>
                  <p>概述</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/ssti/ssti_jinja2.html" class="nav-link" id="ssti/ssti_jinja2">
                  <i class="far nav-icon"></i>
                  <p>JINJA2模板注入</p>
                </a>
              </li>
            </ul>
          </li>
          <li class="nav-item has-treeview" id="xxe">
            <a href="${baseUri}pages/xxe/index.html" class="nav-link">
              <i class="fas fa-fighter-jet nav-icon"></i>
              <p>
                XML外部实体注入
                <i class="fas fa-angle-left right"></i>
              </p>
            </a>
            <ul class="nav nav-treeview">
              <li class="nav-item">
                <a href="${baseUri}pages/xxe/index.html" class="nav-link" id="xxe/index">
                  <i class="far nav-icon"></i>
                  <p>概述</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/xxe/xml_parse.html" class="nav-link" id="xxe/xml_parse">
                  <i class="far nav-icon"></i>
                  <p>XXE</p>
                </a>
              </li>
            </ul>
          </li>
          <li class="nav-item has-treeview" id="serialize">
            <a href="${baseUri}pages/serialize/index.html" class="nav-link">
              <i class="fas fa-fighter-jet nav-icon"></i>
              <p>
                Python反序列化
                <i class="fas fa-angle-left right"></i>
              </p>
            </a>
            <ul class="nav nav-treeview">
              <li class="nav-item">
                <a href="${baseUri}pages/serialize/index.html" class="nav-link" id="serialize/index">
                  <i class="far nav-icon"></i>
                  <p>概述</p>
                </a>
              </li>
              <li class="nav-item">
                <a href="${baseUri}pages/serialize/pickle.html" class="nav-link" id="serialize/pickle">
                  <i class="far nav-icon"></i>
                  <p>pickle反序列化</p>
                </a>
              </li>
            </ul>
          </li>
          <li class="nav-item">
            <a href="${baseUri}pages/about_pilot.html" class="nav-link">
              <i class="nav-icon fas fa-book"></i>
              <p>
                关于靶场
              </p>
            </a>
          </li>
        </ul>
      </nav>`
    const Navbar = `
    <!-- Left navbar links -->
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" data-widget="pushmenu" href="#" role="button"><i class="fas fa-bars"></i></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" data-widget="fullscreen" href="#" role="button">
          <i class="fas fa-expand-arrows-alt"></i>
        </a>
      </li>
      <li class="nav-item d-none d-sm-inline-block">
        <a href="${baseUri}index.html" class="nav-link">主页</a>
      </li>
      <li class="nav-item d-none d-sm-inline-block">
        <a href="http://www.imfanqie.top" target="_blank" class="nav-link">作者博客</a>
      </li>
      <li class="nav-item d-none d-sm-inline-block">
        <a href="https://github.com/2740908911" target="_blank" class="nav-link">Github仓库</a>
      </li>
      <li class="nav-item d-none d-sm-inline-block">
        <a href="../../Pilot-Web.pdf" target="_blank" class="nav-link">靶场文档</a>
      </li>
    </ul>

    <!-- Right navbar links -->
    <ul class="navbar-nav ml-auto">
      <li class="nav-item">
        <strong> Pilot 漏洞测试教学靶场</strong>
      </li>
    </ul>`
    const Footer = `
    <img src="${baseUri}dist/img/pilot.png" width="2%" height="2%" style="margin-bottom: 3.5px;"> 
    <strong>  Pilot-Web © 2024 Developed by Fanqie. </strong>
    All rights reserved.
    <div class="float-right d-none d-sm-inline-block">
      <b>Version</b> 1.0
    </div>`
    let container = body.querySelector("#Container")
    container.innerHTML = Container
    let sidebar = body.querySelector("#sidebar")
    sidebar.innerHTML = Sidebar_Menu
    let navbar = body.querySelector("#Navbar")
    navbar.innerHTML = Navbar
    let footer = body.querySelector("footer")
    footer.innerHTML = Footer
})()

function setWrapperHeader(fatherTitle = "默认", childrenTitles = ["默认"]) {
    let childrenList = "";
    for (let children of childrenTitles) {
        childrenList += `<li class="breadcrumb-item active">${children}</li>`
    }
    let WrapperHeader = `<div class="container-fluid">
        <div class="row mb-2">
          <div class="col-sm-6">
            <h1 class="m-0">${fatherTitle}</h1>
          </div><!-- /.col -->
          <div class="col-sm-6">
            <ol class="breadcrumb float-sm-right">
              <li class="breadcrumb-item"><a href="">${fatherTitle}</a></li>
              ${childrenList}
            </ol>
          </div><!-- /.col -->
        </div><!-- /.row -->
      </div><!-- /.container-fluid -->`
    let wrapper_header = body.querySelector("#WrapperHeader")
    wrapper_header.innerHTML = WrapperHeader
}

function generateNote(mes) {
    return `<div class="callout callout-info">
              <h5><i class="fas fa-info"></i> Note:</h5>${mes}</div>`;
}

function setActiveClass() {
  const currentPageUrl = window.location.href;

  const match = currentPageUrl.match(/\/pages\/([^/]+)/);
  const matchHtml = currentPageUrl.match(/\/pages\/([^/]+\/[^/]+)\.html/);
  const NavItem = document.getElementById(match[1]);
  const NavLink = document.getElementById(matchHtml[1]);

  NavItem.classList.add('menu-open');
  NavLink.classList.add('active');
}

// 当页面加载完成时调用setActiveClass函数
document.addEventListener('DOMContentLoaded', setActiveClass);

if (document.location.pathname.indexOf("index") === -1) {
    let headers = document.getElementsByClassName('card-header')[0];
    let links = []; // 用于存储所有链接

    // 创建一个通用的链接添加函数
    function createLink(text, targetId, otherIds) {
        let link = document.createElement('a');
        link.style = 'float: right; cursor: pointer; margin-right: 10px; color: darkgray; font-weight: bold';
        link.innerText = text;
        headers.appendChild(link);
        links.push(link); // 将链接添加到数组中

        link.onclick = () => {
            let targetDiv = document.getElementById(targetId).style;
            let isShowing = targetDiv.display !== 'none'; // 判断当前是否显示

            // 设置所有链接为深灰色
            links.forEach(lnk => lnk.style.color = 'darkgray');

            // 根据展开状态切换颜色和显示
            if (isShowing) {
                targetDiv.display = 'none';
            } else {
                targetDiv.display = 'block';
                link.style.color = 'black'; // 设置当前链接为黑色
            }

            // 隐藏其他所有标签
            otherIds.forEach(id => {
                let otherDiv = document.getElementById(id).style;
                otherDiv.display = 'none';
            });
        };
    }

    // 添加所有链接
    createLink("知识梳理", 'repository', ['showSource', 'writeUp', 'hint']);
    createLink("源码解析", 'showSource', ['repository', 'writeUp', 'hint']);
    createLink("正确实现", 'writeUp', ['repository', 'showSource', 'hint']);
    createLink("思路提示", 'hint', ['repository', 'showSource', 'writeUp']);

    // 初始化标签的显示状态
    ['repository', 'showSource', 'writeUp', 'hint'].forEach(id => {
        document.getElementById(id).style.display = 'none';
    });
}




