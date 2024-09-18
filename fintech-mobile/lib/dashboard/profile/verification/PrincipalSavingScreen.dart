import 'package:flutter/material.dart';
import 'package:cooperation_apps/constants/colors.dart';
import 'package:flutter/services.dart';


class PrincipalSavingPage extends StatefulWidget {

  @override
  State<StatefulWidget> createState() => new _PrincipalSavingPageState();
}

class _PrincipalSavingPageState extends State<PrincipalSavingPage> {
  TextEditingController nameController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Container(
          child: SingleChildScrollView(
            child: Column(
              children: <Widget>[
                //title
                Container(
                  padding: EdgeInsets.all(30),
                  child: Center(
                    child: Text(
                      'Pembayaran Simpanan Pokok & Wajib',
                      style: TextStyle(
                          color: appBarText,
                          fontSize: 30
                      ),
                    ),
                  ),
                ),
                //name
                Container(
                  padding: EdgeInsets.all(10),
                  child: TextFormField(
                    controller: nameController,
                    keyboardType: TextInputType.number,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Simpanan Pokok',
                    ),
                  ),
                ),
                Container(
                  padding: EdgeInsets.all(10),
                  child: TextFormField(
                    controller: nameController,
                    keyboardType: TextInputType.number,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Simpanan Wajib',
                    ),
                  ),
                ),
                //button save
                Container(
                    height: 50,
                    padding: EdgeInsets.fromLTRB(10, 0, 10, 10),
                    child: ElevatedButton(
                      style: ButtonStyle(backgroundColor: MaterialStateProperty.all<Color>(buttonGeneric)),
                      child: Text('Simpan'),
                      onPressed: () {
                      },
                    )
                ),
              ],
            ),
          ),
        )
    );
  }
}