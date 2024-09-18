import 'package:flutter/material.dart';
import 'package:cooperation_apps/constants/assets.dart';
import 'package:cooperation_apps/constants/colors.dart';


class AssetPage extends StatefulWidget {

  @override
  State<StatefulWidget> createState() => new _AssetPageState();
}

class _AssetPageState extends State<AssetPage> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          backgroundColor: appBarBg,
          title: Center(
            child: new  Text(
              'Performa Anda',
              style: TextStyle(color: appBarText),
            ),
          ),
          automaticallyImplyLeading: false,
        ),
        body: Container(
          child: SafeArea(
             child: SingleChildScrollView(
               padding: EdgeInsets.all(5),
               child: Column(
                 children: <Widget>[
                   // Your Saving Nominal
                   Container(
                       padding: EdgeInsets.symmetric(horizontal: 10, vertical: 15),
                       child: Column(
                         children: <Widget>[
                           Container(
                             alignment: Alignment.center,
                             child: Text(
                               'Rp. xxx.xxx.xxx',
                               style: TextStyle(
                                 fontSize: 25,
                                 fontWeight: FontWeight.bold,
                               ),
                             ),
                           ),
                           Container(
                               alignment: Alignment.center,
                               child: Text(
                                 'Saldo Saat Ini',
                                 style: TextStyle(
                                   color: Colors.black38,
                                   fontSize: 12.5,
                                 ),
                               )
                           )
                         ],
                       )
                   ),

                   Card(
                     child: Container(
                       alignment: Alignment.center,
                       padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                       height: MediaQuery.of(context).size.height * 0.300,
                       width: MediaQuery.of(context).size.width * 0.90,
                       child:  Column(
                         children: <Widget>[
                           Container(
                             alignment: Alignment.centerLeft,
                             child: Text(
                               'Card 1',
                               style: TextStyle(fontSize: 20),
                             ),
                           ),
                           const Divider(
                             color: Colors.black38,
                             thickness: 1,
                           ),
                           Expanded(
                             child: ListView.builder(
                                 physics: NeverScrollableScrollPhysics(),
                                 itemCount: assets_list.length,
                                 itemBuilder: (context, index) {
                                   return Container(
                                       child: Row(
                                         mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                         children: <Widget>[
                                           Container(
                                             alignment: Alignment.centerLeft,
                                             child: Text(
                                               assets_list[index]['sub'],
                                               textAlign: TextAlign.left,
                                               style: TextStyle(
                                                 fontSize: 17.5,
                                               ),
                                             ),
                                           ),
                                           Container(
                                             alignment: Alignment.centerRight,
                                             child: Text(
                                               assets_list[index]['title'],
                                               textAlign: TextAlign.end,
                                               style: TextStyle(
                                                 fontSize: 17.5,
                                               ),
                                             ),
                                           )
                                         ],
                                       )
                                   );
                                 }
                             ),
                           ),
                         ],
                       ),
                     ),
                     shape: RoundedRectangleBorder(
                       borderRadius: BorderRadius.circular(20),
                     ),
                   ),

                   Card(
                     child: Container(
                       alignment: Alignment.center,
                       padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                       height: MediaQuery.of(context).size.height * 0.300,
                       width: MediaQuery.of(context).size.width * 0.90,
                       child:  Column(
                         children: <Widget>[
                           Container(
                             alignment: Alignment.centerLeft,
                             child: Text(
                               'Card 2',
                               style: TextStyle(fontSize: 20),
                             ),
                           ),
                           const Divider(
                             color: Colors.black38,
                             thickness: 1,
                           ),
                           Expanded(
                             child: ListView.builder(
                                 physics: NeverScrollableScrollPhysics(),
                                 itemCount: assets_list.length,
                                 itemBuilder: (context, index) {
                                   return Container(
                                       child: Row(
                                         mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                         children: <Widget>[
                                           Container(
                                             alignment: Alignment.centerLeft,
                                             child: Text(
                                               assets_list[index]['sub'],
                                               textAlign: TextAlign.left,
                                               style: TextStyle(
                                                 fontSize: 17.5,
                                               ),
                                             ),
                                           ),
                                           Container(
                                             alignment: Alignment.centerRight,
                                             child: Text(
                                               assets_list[index]['title'],
                                               textAlign: TextAlign.end,
                                               style: TextStyle(
                                                 fontSize: 17.5,
                                               ),
                                             ),
                                           )
                                         ],
                                       )
                                   );
                                 }
                             ),
                           ),
                         ],
                       ),
                     ),
                     shape: RoundedRectangleBorder(
                       borderRadius: BorderRadius.circular(20),
                     ),
                   ),
                   Card(
                     child: Container(
                       alignment: Alignment.center,
                       padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                       height: MediaQuery.of(context).size.height * 0.300,
                       width: MediaQuery.of(context).size.width * 0.90,
                       child:  Column(
                         children: <Widget>[
                           Container(
                             alignment: Alignment.centerLeft,
                             child: Text(
                               'Card 3',
                               style: TextStyle(fontSize: 20),
                             ),
                           ),
                           const Divider(
                             color: Colors.black38,
                             thickness: 1,
                           ),
                           Expanded(
                             child: ListView.builder(
                                 physics: NeverScrollableScrollPhysics(),
                                 itemCount: assets_list.length,
                                 itemBuilder: (context, index) {
                                   return Container(
                                       child: Row(
                                         mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                         children: <Widget>[
                                           Container(
                                             alignment: Alignment.centerLeft,
                                             child: Text(
                                               assets_list[index]['sub'],
                                               textAlign: TextAlign.left,
                                               style: TextStyle(
                                                 fontSize: 17.5,
                                               ),
                                             ),
                                           ),
                                           Container(
                                             alignment: Alignment.centerRight,
                                             child: Text(
                                               assets_list[index]['title'],
                                               textAlign: TextAlign.end,
                                               style: TextStyle(
                                                 fontSize: 17.5,
                                               ),
                                             ),
                                           )
                                         ],
                                       )
                                   );
                                 }
                             ),
                           ),
                         ],
                       ),
                     ),
                     shape: RoundedRectangleBorder(
                       borderRadius: BorderRadius.circular(20),
                     ),
                   ),
                   Card(
                     child: Container(
                       alignment: Alignment.center,
                       padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                       height: MediaQuery.of(context).size.height * 0.300,
                       width: MediaQuery.of(context).size.width * 0.90,
                       child:  Column(
                         children: <Widget>[
                           Container(
                             alignment: Alignment.centerLeft,
                             child: Text(
                               'Card 4',
                               style: TextStyle(fontSize: 20),
                             ),
                           ),
                           const Divider(
                             color: Colors.black38,
                             thickness: 1,
                           ),
                           Expanded(
                             child: ListView.builder(
                                 physics: NeverScrollableScrollPhysics(),
                                 itemCount: assets_list.length,
                                 itemBuilder: (context, index) {
                                   return Container(
                                       child: Row(
                                         mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                         children: <Widget>[
                                           Container(
                                             alignment: Alignment.centerLeft,
                                             child: Text(
                                               assets_list[index]['sub'],
                                               textAlign: TextAlign.left,
                                               style: TextStyle(
                                                 fontSize: 17.5,
                                               ),
                                             ),
                                           ),
                                           Container(
                                             alignment: Alignment.centerRight,
                                             child: Text(
                                               assets_list[index]['title'],
                                               textAlign: TextAlign.end,
                                               style: TextStyle(
                                                 fontSize: 17.5,
                                               ),
                                             ),
                                           )
                                         ],
                                       )
                                   );
                                 }
                             ),
                           ),
                         ],
                       ),
                     ),
                     shape: RoundedRectangleBorder(
                       borderRadius: BorderRadius.circular(20),
                     ),
                   ),
                   Card(
                     child: Container(
                       alignment: Alignment.center,
                       padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                       height: MediaQuery.of(context).size.height * 0.300,
                       width: MediaQuery.of(context).size.width * 0.90,
                       child:  Column(
                         children: <Widget>[
                           Container(
                             alignment: Alignment.centerLeft,
                             child: Text(
                               'Card 5',
                               style: TextStyle(fontSize: 20),
                             ),
                           ),
                           const Divider(
                             color: Colors.black38,
                             thickness: 1,
                           ),
                           Expanded(
                             child: ListView.builder(
                                 physics: NeverScrollableScrollPhysics(),
                                 itemCount: assets_list.length,
                                 itemBuilder: (context, index) {
                                   return Container(
                                       child: Row(
                                         mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                         children: <Widget>[
                                           Container(
                                             alignment: Alignment.centerLeft,
                                             child: Text(
                                               assets_list[index]['sub'],
                                               textAlign: TextAlign.left,
                                               style: TextStyle(
                                                 fontSize: 17.5,
                                               ),
                                             ),
                                           ),
                                           Container(
                                             alignment: Alignment.centerRight,
                                             child: Text(
                                               assets_list[index]['title'],
                                               textAlign: TextAlign.end,
                                               style: TextStyle(
                                                 fontSize: 17.5,
                                               ),
                                             ),
                                           )
                                         ],
                                       )
                                   );
                                 }
                             ),
                           ),
                         ],
                       ),
                     ),
                     shape: RoundedRectangleBorder(
                       borderRadius: BorderRadius.circular(20),
                     ),
                   ),
                 ],
               ),
             )
          ),
        ),
    );
  }
}