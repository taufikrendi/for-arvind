import 'package:flutter/material.dart';

final List menus_slide = [
  {
    'title': 'Simpanan',
    'image': 'images/logo.png'
  },
  {
    'title': 'Pinjaman',
    'image': 'images/logo.png'
  },
  {
    'title': 'Bantu Anggota',
    'image': 'images/logo.png'
  },
  {
    'title': 'Tagihan',
    'image': 'images/logo.png'
  },
  {
    'title': 'Ziswaf',
    'image': 'images/logo.png'
  },
  {
    'title': 'Top Up',
    'image': 'images/logo.png'
  },
  {
    'title': 'Penarikan',
    'image': 'images/logo.png'
  },
  {
    'title': 'Voucher Game',
    'image': 'images/logo.png'
  }
];

final List menus_list = [
  {
    'title': 'XX-XX-XXXX',
    'sub': 'Periode Simpanan Wajib',
  },
  {
    'title': 'Rp. xxx.xxx.xxx',
    'sub': 'Simpanan Wajib',
  },
  {
    'title': 'Rp. xxx.xxx.xxx',
    'sub': 'Total SHU',
  },
  {
    'title': 'Rp. xxx.xxx.xxx',
    'sub': 'Total Aset',
  },
  {
    'title': 'Rp. xxx.xxx.xxx',
    'sub': 'Penarikan Saldo (Bulan)',
  },
  {
    'title': 'Rp. xxx.xxx.xxx',
    'sub': 'Sisa Pinjaman',
  },
  {
    'title': 'Rp. xxx.xxx.xxx',
    'sub': 'Angsuran Terbayar',
  },
];

final List news_slide = [
  {
    'title': 'lorem ipsum',
    'sub': 'lorem ipsum',
    'link': '/login/',
    'image': 'images/logo.png'
  },
  {
    'title': 'lorem ipsum',
    'sub': 'lorem ipsum',
    'link': '/login/',
    'image': 'images/logo.png'
  },
  {
    'title': 'lorem ipsum',
    'sub': 'lorem ipsum',
    'link': '/login/',
    'image': 'images/logo.png'
  },
  {
    'title': 'lorem ipsum',
    'sub': 'lorem ipsum',
    'link': '/login/',
    'image': 'images/logo.png'
  },
  {
    'title': 'lorem ipsum',
    'sub': 'lorem ipsum',
    'link': '/login/',
    'image': 'images/logo.png'
  }
];

final List savings_list = [
  {
    'title': 'Simpanan Wajib',
    'sub': 'Minimun Rp. 10.000 Setiap Bulan',
    'link': '/login/',
    'image': 'images/logo.png'
  },
  {
    'title': 'Deposito Syariah',
    'sub': 'Deposito dengan Skema Syariah',
    'link': '/login/',
    'image': 'images/logo.png'
  },
  {
    'title': 'Simpanan Haji & Umrah',
    'sub': 'Tabungan Rencana Haji & Umrah',
    'link': '/login/',
    'image': 'images/logo.png'
  },
  {
    'title': 'Simpanan Pendidikan',
    'sub': 'Tabungan Rencana Pendidikan',
    'link': '/login/',
    'image': 'images/logo.png'
  }
];

final List ppob_list = [
  {
    'title': 'Top Up / Bayar Listrik PLN',
    'sub': 'Top Up / Bayar Tagihan Listrik PLN',
    'link': '/login/',
    'image': 'images/logo.png'
  },
  {
    'title': 'Pulsa / Data / Pasca Bayar',
    'sub': 'Top Up Pulsa / Quota Internet / Pasca Bayar',
    'link': '/login/',
    'image': 'images/logo.png'
  },
  {
    'title': 'PDAM',
    'sub': 'Bayar Tagihan Air',
    'link': '/login/',
    'image': 'images/logo.png'
  },
  {
    'title': 'Tagihan TV Kabel',
    'sub': 'Bayar Tagihan TV Kabel',
    'link': '/login/',
    'image': 'images/logo.png'
  }
];

final List topup_list = [
  {
    'title': 'Top Up OVO',
    'sub': 'Top Up Saldo OVO',
    'link': '/login/',
    'image': 'images/logo.png'
  },
  {
    'title': 'Top Up Go-Pay',
    'sub': 'Top Up Saldo Go-Pay',
    'link': '/login/',
    'image': 'images/logo.png'
  },
  {
    'title': 'Top Up ShoopePay',
    'sub': 'Top Up Saldo ShoopePay',
    'link': '/login/',
    'image': 'images/logo.png'
  },
  {
    'title': 'Top Up Uang Elektronik',
    'sub': 'Top Up Saldo Uang Elektronik',
    'link': '/login/',
    'image': 'images/logo.png'
  },
];

final List withdraw_list = [
  {
    'title': 'Status Penarikan',
    'sub': 'Status Pencairan Dana',
    'link': '/login/',
    'image': 'images/logo.png'
  },
  {
    'title': 'Penarikan dari Simpanan Wajib',
    'sub': 'Cairkan Dana Simpanan Wajib Anda',
    'link': '/login/',
    'image': 'images/logo.png'
  },
  {
    'title': 'Penarikan dari SHU',
    'sub': 'Cairkan Dana SHU',
    'link': '/login/',
    'image': 'images/logo.png'
  },
  {
    'title': 'Penarikan dari Bantu Anggota',
    'sub': 'Cairkan Dana Bagi Hasil Bantu Anggota',
    'link': '/login/',
    'image': 'images/logo.png'
  }
];

viewSavings(BuildContext context) {
  showModalBottomSheet(
    context: context,
    isScrollControlled: true,
    backgroundColor: Colors.transparent,
    //elevates modal bottom screen
    elevation: 10,
    // gives rounded corner to modal bottom screen
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(20.0),
    ),
    builder: (context) => SingleChildScrollView(
      child: Container(
          height: MediaQuery.of(context).size.height * 0.500,
          decoration: new BoxDecoration(
            color: Colors.white,
            borderRadius: new BorderRadius.only(
              topLeft: const Radius.circular(25.0),
              topRight: const Radius.circular(25.0),
            ),
          ),
          child: Container(
              padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
              child: Column(
                  children: <Widget>[
                    Divider(
                      thickness: 10,
                      color: Colors.grey,
                      indent: 185,
                      endIndent: 175,
                    ),
                    ListView.builder(
                        scrollDirection: Axis.vertical,
                        shrinkWrap: true,
                        itemCount: savings_list.length,
                        physics: NeverScrollableScrollPhysics(),
                        itemBuilder: (context, index){
                          return Column(
                            children: <Widget>[
                              GestureDetector(
                                onTap: (){
                                  Navigator.pushNamed(context, savings_list[index]['link']);
                                },
                                child: ListTile(
                                    leading: new Image(image:AssetImage(savings_list[index]['image'])),
                                    title: Text(savings_list[index]['title']),
                                    subtitle: Text(savings_list[index]['sub']),
                                    trailing: Icon(Icons.arrow_forward_ios_outlined)
                                ),
                              ),
                              Divider(),
                            ],
                          );
                        }
                    ),
                  ]
              )
          )
      ),
    )
  );
}

viewPayment(BuildContext context) {
  showModalBottomSheet(
    context: context,
    isScrollControlled: true,
    backgroundColor: Colors.transparent,
    //elevates modal bottom screen
    elevation: 10,
    // gives rounded corner to modal bottom screen
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(20.0),
    ),
    builder: (context) => SingleChildScrollView(
      child: Container(
          height: MediaQuery.of(context).size.height * 0.500,
          decoration: new BoxDecoration(
            color: Colors.white,
            borderRadius: new BorderRadius.only(
              topLeft: const Radius.circular(25.0),
              topRight: const Radius.circular(25.0),
            ),
          ),
          child: Container(
              padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
              child: Column(
                  children: <Widget>[
                    Divider(
                      thickness: 10,
                      color: Colors.grey,
                      indent: 185,
                      endIndent: 175,
                    ),
                    ListView.builder(
                        scrollDirection: Axis.vertical,
                        shrinkWrap: true,
                        itemCount: savings_list.length,
                        physics: NeverScrollableScrollPhysics(),
                        itemBuilder: (context, index){
                          return Column(
                            children: <Widget>[
                              GestureDetector(
                                onTap: (){
                                  Navigator.pushNamed(context, ppob_list[index]['link']);
                                },
                                child: ListTile(
                                    leading: new Image(image:AssetImage(ppob_list[index]['image'])),
                                    title: Text(ppob_list[index]['title']),
                                    subtitle: Text(ppob_list[index]['sub']),
                                    trailing: Icon(Icons.arrow_forward_ios_outlined)
                                ),
                              ),
                              Divider(),
                            ],
                          );
                        }
                    ),
                  ]
              )
          )
      ),
    )
  );
}

viewTopUp(BuildContext context) {
  showModalBottomSheet(
    context: context,
    isScrollControlled: true,
    backgroundColor: Colors.transparent,
    //elevates modal bottom screen
    elevation: 10,
    // gives rounded corner to modal bottom screen
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(20.0),
    ),
    builder: (context) => SingleChildScrollView(
      child: Container(
          height: MediaQuery.of(context).size.height * 0.500,
          decoration: new BoxDecoration(
            color: Colors.white,
            borderRadius: new BorderRadius.only(
              topLeft: const Radius.circular(25.0),
              topRight: const Radius.circular(25.0),
            ),
          ),
          child: Container(
              padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
              child: Column(
                  children: <Widget>[
                    Divider(
                      thickness: 10,
                      color: Colors.grey,
                      indent: 185,
                      endIndent: 175,
                    ),
                    ListView.builder(
                        scrollDirection: Axis.vertical,
                        shrinkWrap: true,
                        itemCount: savings_list.length,
                        physics: NeverScrollableScrollPhysics(),
                        itemBuilder: (context, index){
                          return Column(
                            children: <Widget>[
                              GestureDetector(
                                onTap: (){
                                  Navigator.pushNamed(context, topup_list[index]['link']);
                                },
                                child: ListTile(
                                    leading: new Image(image:AssetImage(topup_list[index]['image'])),
                                    title: Text(topup_list[index]['title']),
                                    subtitle: Text(topup_list[index]['sub']),
                                    trailing: Icon(Icons.arrow_forward_ios_outlined)
                                ),
                              ),
                              Divider(),
                            ],
                          );
                        }
                    ),
                  ]
              )
          )
      ),
    )
  );
}

viewWithDraw(BuildContext context) {
  showModalBottomSheet(
    context: context,
    isScrollControlled: true,
    backgroundColor: Colors.transparent,
    //elevates modal bottom screen
    elevation: 10,
    // gives rounded corner to modal bottom screen
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(20.0),
    ),
    builder: (context) => SingleChildScrollView(
      child: Container(
          height: MediaQuery.of(context).size.height * 0.500,
          decoration: new BoxDecoration(
            color: Colors.white,
            borderRadius: new BorderRadius.only(
              topLeft: const Radius.circular(25.0),
              topRight: const Radius.circular(25.0),
            ),
          ),
          child: Container(
              padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
              child: Column(
                  children: <Widget>[
                    Divider(
                      thickness: 10,
                      color: Colors.grey,
                      indent: 185,
                      endIndent: 175,
                    ),
                    ListView.builder(
                        scrollDirection: Axis.vertical,
                        shrinkWrap: true,
                        itemCount: savings_list.length,
                        physics: NeverScrollableScrollPhysics(),
                        itemBuilder: (context, index){
                          return Column(
                            children: <Widget>[
                              GestureDetector(
                                onTap: (){
                                  Navigator.pushNamed(context, withdraw_list[index]['link']);
                                },
                                child: ListTile(
                                    leading: new Image(image:AssetImage(withdraw_list[index]['image'])),
                                    title: Text(withdraw_list[index]['title']),
                                    subtitle: Text(withdraw_list[index]['sub']),
                                    trailing: Icon(Icons.arrow_forward_ios_outlined)
                                ),
                              ),
                              Divider(),
                            ],
                          );
                        }
                    ),
                  ]
              )
          )
      ),
    )
  );
}