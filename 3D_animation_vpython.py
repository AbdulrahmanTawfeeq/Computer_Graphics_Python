# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:30:56 2020

@author: Ahmad
"""

from vpython import *

local_light(
    color=color.red,
    pos=vector(1, 1, 1)
)

distant_light(
    direction=vector(-10, -10, -10),
    color=color.yellow
)

earth = sphere(
    pos=vector(-5, 0, 5),
    texture=textures.earth,
    size=vector(1, 1, 1)
)

ring = ring(
    pos=vector(0, 0, 5),
    texture=textures.rug,
    radius=1,
    thickness=0.09
)

box_right = box(
    pos=vector(5, 0, 5),
    texture=textures.wood,
    size=vector(2, 2, 2),
)

box_left = box(
    pos=vector(-4, 0, 5),
    texture=textures.wood,
    size=vector(2, 2, 2),
)

d = 0
opa = 0
opa2 = 0
while True:
    ring.rotate(axis=vector(1, 0, 0), angle=0.05)
    rate(7)
    earth.pos = vector(d, 0, 5)
    box_right.opacity = opa
    box_left.opacity = opa2
    d += 1
    opa += 0.1
    opa2 -= 0.1

    if (earth.pos.x >= 5):
        for i in range(10):
            ring.rotate(axis=vector(1, 0, 0), angle=0.05)
            rate(7)
            d -= 1
            opa -= 0.1
            opa2 += 0.1
            earth.pos = vector(d, 0, 5)
            box_right.opacity = opa
            box_left.opacity = opa2
