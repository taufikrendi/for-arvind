import 'package:flutter/material.dart';
import 'package:cooperation_apps/constants/verification.dart';
import 'package:cooperation_apps/constants/colors.dart';


class VerificationPage extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => new _State();
}

class _State extends State<VerificationPage> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Container(
          child: SafeArea(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: <Widget>[
                Container(
                  padding: EdgeInsets.all(16),
                  child: Center(
                    child: Text(
                      'Verifikasi Data diri',
                      style: TextStyle(
                          color: appBarText,
                          fontSize: 30
                      ),
                    ),
                  ),
                ),
                Container(
                  child: Expanded(
                    child: Column(
                      children: [
                        ListView.builder(
                            scrollDirection: Axis.vertical,
                            shrinkWrap: true,
                            itemCount: verification_list.length,
                            itemBuilder: (context, index) => GestureDetector(
                                onTap: () => Navigator.pushNamed(context, verification_list[index]['link']),
                                child: Card(
                                  margin: new EdgeInsets.symmetric(horizontal: 10.0, vertical: 6.0),
                                  child: ListTile(
                                    contentPadding: EdgeInsets.symmetric(horizontal: 20.0, vertical: 10.0),
                                    leading: Image(image:AssetImage(verification_list[index]['image'])),
                                    title: Text(verification_list[index]['title']),
                                    subtitle: Text(verification_list[index]['sub']),
                                    trailing: Icon(Icons.arrow_forward_ios_outlined),
                                  ),
                                )
                            )
                        ),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),
        )
    );
  }
}