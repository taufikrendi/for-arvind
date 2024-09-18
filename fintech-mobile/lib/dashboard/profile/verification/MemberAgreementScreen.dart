import 'package:flutter/material.dart';


class MemberAgreementPage extends StatefulWidget {

  @override
  State<StatefulWidget> createState() => new _State();
}

class _State extends State<MemberAgreementPage> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Padding(
            padding: EdgeInsets.all(10),
            child: ListView(
              children: <Widget>[
                Container(
                    alignment: Alignment.topLeft,
                    padding: EdgeInsets.all(10),
                    child: Text('Member Agreement',
                      style: TextStyle(color: Colors.black, fontSize: 48),
                    )
                ),
                //text field
              ],
            )));
  }
}