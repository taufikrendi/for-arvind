import 'package:flutter/material.dart';
import 'package:cooperation_apps/all.dart';
import 'package:cooperation_apps/constants/colors.dart';

class IndexPage extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => new _IndexPageState();
}

class _IndexPageState extends State<IndexPage> {
  int _currentIndex = 0;
  final _pageOptions = [
    HomePage(),
    ActivityPage(),
    QRPage(),
    AssetPage(),
    ProfilePage()
  ];

  @override
  Widget build(BuildContext context) {
    final colorScheme = Theme.of(context).colorScheme;
    return Scaffold(
      body: _pageOptions[_currentIndex],
      bottomNavigationBar: BottomNavigationBar(
        type: BottomNavigationBarType.fixed,
        currentIndex: _currentIndex,
        backgroundColor: buttomNavBarBg,
        selectedItemColor: buttomSelectedItem,
        unselectedItemColor: buttomUnSelectedItem,
        items: [
          BottomNavigationBarItem(
              icon: new Image(image:AssetImage('images/logo.png')), label: 'Beranda'),
          BottomNavigationBarItem(
              icon: new Image(image:AssetImage('images/logo.png')), label: 'Aktifitas'),
          BottomNavigationBarItem(
              icon: new Image(image:AssetImage('images/logo.png')), label: 'QRIS'),
          BottomNavigationBarItem(
              icon: new Image(image:AssetImage('images/logo.png')), label: 'Performa'),
          BottomNavigationBarItem(
              icon: new Image(image:AssetImage('images/logo.png')), label: 'Profile'),
        ],
        onTap: (index) {
          setState(() {
            _currentIndex = index;
          });
        },
      ),
    );
  }
}
