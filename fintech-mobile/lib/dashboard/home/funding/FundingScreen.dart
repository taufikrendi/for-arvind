import 'package:flutter/material.dart';


class FundingPage extends StatefulWidget {

  @override
  State<StatefulWidget> createState() => new _State();
}

class _State extends State<FundingPage> {

  bool _validate = false;

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
                    child: Text('Funding!',
                      style: TextStyle(color: Colors.black, fontSize: 48),
                    )
                ),
              ],
            )));
  }
}