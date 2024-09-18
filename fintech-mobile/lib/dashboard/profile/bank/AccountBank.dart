import 'package:flutter/material.dart';
import 'package:cooperation_apps/constants/colors.dart';

class AccountBankPage extends StatefulWidget {

  @override
  State<StatefulWidget> createState() => new _AccountBankPageState();
}

class _AccountBankPageState extends State<AccountBankPage> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Container(
          child: SafeArea(
            child: Column(
              children: <Widget>[
                Container(
                  padding: EdgeInsets.symmetric(horizontal: 32, vertical: 10),
                  height: 300,
                  width: 500,
                  child: new GestureDetector(
                      onTap: (){},
                      child: new Card(
                        child: Container(
                          width: 200,
                          child: Column(
                            children: [
                              Image(image:AssetImage('images/logo.png')),
                              ListTile(
                                title: Text(
                                  'Bagus Setya Wardana',
                                  style: TextStyle(color: slideMenuTextH.withOpacity(0.6), fontSize: 20),
                                ),
                                subtitle: Text(
                                  'xxxx xxxx xxxx xxxx',
                                  style: TextStyle(color: slideMenuTextH.withOpacity(0.6), fontSize: 12.5),
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                    ),
                ),
                Container(
                    height: 50,
                    padding: EdgeInsets.fromLTRB(10, 0, 10, 10),
                    child: ElevatedButton(
                      style: ButtonStyle(backgroundColor: MaterialStateProperty.all<Color>(buttonGeneric)),
                      child: Text('Tambah Rekening'),
                      onPressed: () {
                        Navigator.pushNamed(context, '/home/');
                      },
                    )),
              ],
            ),
          ),
        )
    );
  }
}