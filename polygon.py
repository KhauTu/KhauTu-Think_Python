ó
*Ð[c           @   sl   d  d l  Z  d  d l Z e  j   Z d   Z d   Z d   Z d   Z d   Z e e d  e  j	   d S(   iÿÿÿÿNc         C   s:   x. t  d  D]  } |  j |  |  j d  q W|  GHd  S(   Ni   iZ   (   t   ranget   fdt   lt(   t   tt   lengtht   i(    (    s&   /Users/dongkhautu/Desktop/mypolygon.pyt   square   s    c         C   s:   x. t  |  D]  } |  j |  |  j |  q W|  GHd S(   sf   Draws n line segments with the given length
    and angle (in degrees) between them. t is turtle.
    N(   R    R   R   (   R   t   nR   t   angleR   (    (    s&   /Users/dongkhautu/Desktop/mypolygon.pyt   polyline   s    c         C   s!   d | } t  |  | | |  d  S(   Ng     v@(   R	   (   R   R   R   R   (    (    s&   /Users/dongkhautu/Desktop/mypolygon.pyt   polygon   s    
c         C   s^   d t  j | | d } t | d  d } | | } t |  | } t |  | | |  d  S(   Ni   ih  i   i   (   t   matht   pit   intt   floatR	   (   R   t   rR   t
   arc_lengthR   t   step_lengtht
   step_angle(    (    s&   /Users/dongkhautu/Desktop/mypolygon.pyt   arc%   s
    
c         C   s   t  |  | d  d  S(   Nih  (   R   (   R   R   (    (    s&   /Users/dongkhautu/Desktop/mypolygon.pyt   circle-   s    i2   (
   t   turtleR   t   Turtlet   bobR   R	   R
   R   R   t   mainloop(    (    (    s&   /Users/dongkhautu/Desktop/mypolygon.pyt   <module>   s   						