import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class ChangePinPage extends StatefulWidget {

  @override
  State<StatefulWidget> createState() => new _State();
}

class _State extends State<ChangePinPage> {

  TextEditingController pinControllerOne = TextEditingController();
  TextEditingController pinControllerTwo = TextEditingController();
  TextEditingController pinControllerThree = TextEditingController();
  TextEditingController pinControllerFour = TextEditingController();
  TextEditingController pinControllerFive = TextEditingController();
  TextEditingController pinControllerSix = TextEditingController();

  var firstField = FocusNode();
  var secondField = FocusNode();
  var thirdField = FocusNode();
  var fourField = FocusNode();
  var fiveField = FocusNode();
  var sixField = FocusNode();

  @override
  void dispose() {
    // Clean up the controller when the widget is disposed.
    firstField.dispose();
    secondField.dispose();
    thirdField.dispose();
    fourField.dispose();
    fiveField.dispose();
    sixField.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final focus = FocusScope.of(context);
    return Scaffold(
        body: Padding(
            padding: EdgeInsets.all(10),
            child: ListView(
              children: <Widget>[
                Container(
                    alignment: Alignment.center,
                    padding: EdgeInsets.all(10),
                    child: Center(
                      child: Text('Masukkan Pin Transaksi Anda!'),
                    )
                ),
                Container(
                    alignment: Alignment.center,
                    padding: EdgeInsets.all(10),
                    child: new Image(image:AssetImage('images/logo.png'))
                ),
                Row(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: <Widget>[
                        Container(
                          width: 30,
                          child: Center(
                            child: TextFormField(
                              focusNode: firstField,
                              textAlign: TextAlign.center,
                              obscureText: true,
                              controller: pinControllerOne,
                              onChanged: (value) {
                                if (value.length == 1) {
                                  focus.requestFocus(secondField);
                                }
                              },
                              keyboardType: TextInputType.number,
                              textInputAction: TextInputAction.next,
                              style: TextStyle(fontSize: 45.0),
                              inputFormatters: [
                                LengthLimitingTextInputFormatter(1),
                              ]
                            ),
                          ),
                        )
                      ],
                    ),
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: <Widget>[
                        Container(
                          width: 30,
                          child: TextFormField(
                            focusNode: secondField,
                            textAlign: TextAlign.center,
                            obscureText: true,
                            controller: pinControllerTwo,
                            onChanged: (value) {
                              if (value.length == 1) {
                                focus.requestFocus(thirdField);
                              }else{
                                focus.requestFocus(firstField);
                              }
                            },
                            keyboardType: TextInputType.number,
                            textInputAction: TextInputAction.next,
                            style: TextStyle(fontSize: 45.0),
                            inputFormatters: [
                              LengthLimitingTextInputFormatter(1),
                            ]
                          ),
                        )
                      ],
                    ),
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: <Widget>[
                        Container(
                          width: 30,
                          child: TextFormField(
                            focusNode: thirdField,
                            textAlign: TextAlign.center,
                            obscureText: true,
                            controller: pinControllerThree,
                            onChanged: (value) {
                              if (value.length == 1) {
                                focus.requestFocus(fourField);
                              }else{
                                focus.requestFocus(secondField);
                              }
                            },
                            keyboardType: TextInputType.number,
                            textInputAction: TextInputAction.next,
                            style: TextStyle(fontSize: 45.0),
                            inputFormatters: [
                              LengthLimitingTextInputFormatter(1),
                            ]
                          ),
                        )
                      ],
                    ),
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: <Widget>[
                        Container(
                          width: 30,
                          child: TextFormField(
                            focusNode: fourField,
                            textAlign: TextAlign.center,
                            obscureText: true,
                            controller: pinControllerFour,
                            onChanged: (value) {
                              if (value.length == 1) {
                                focus.requestFocus(fiveField);
                              }else{
                                focus.requestFocus(thirdField);
                              }
                            },
                            keyboardType: TextInputType.number,
                            textInputAction: TextInputAction.next,
                            style: TextStyle(fontSize: 45.0),
                            inputFormatters: [
                              LengthLimitingTextInputFormatter(1),
                            ]
                          ),
                        )
                      ],
                    ),
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: <Widget>[
                        Container(
                          width: 30,
                          child: TextFormField(
                            focusNode: fiveField,
                            textAlign: TextAlign.center,
                            obscureText: true,
                            controller: pinControllerFive,
                            onChanged: (value) {
                              if (value.length == 1) {
                                focus.requestFocus(sixField);
                              }else{
                                focus.requestFocus(fourField);
                              }
                            },
                            keyboardType: TextInputType.number,
                            textInputAction: TextInputAction.next,
                            style: TextStyle(fontSize: 45.0),
                            inputFormatters: [
                              LengthLimitingTextInputFormatter(1),
                            ]
                          ),
                        )
                      ],
                    ),
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: <Widget>[
                        Container(
                          width: 30,
                          child: TextFormField(
                            focusNode: sixField,
                            textAlign: TextAlign.center,
                            obscureText: true,
                            controller: pinControllerSix,
                            onChanged: (value) {
                              if (value.length == 1) {
                                print(pinControllerOne.text+pinControllerTwo.text+
                                    pinControllerThree.text+pinControllerFour.text+
                                    pinControllerFive.text+pinControllerSix.text);
                              }else{
                                focus.requestFocus(fiveField);
                              }
                            },
                            keyboardType: TextInputType.number,
                            textInputAction: TextInputAction.done,
                            style: TextStyle(fontSize: 45.0),
                            inputFormatters: [
                              LengthLimitingTextInputFormatter(1),
                            ]
                          ),
                        )
                      ],
                    ),
                  ],
                ),
                // Container(
                //     height: 50,
                //     padding: EdgeInsets.fromLTRB(10, 0, 10, 10),
                //     child: ElevatedButton(
                //       style: ButtonStyle(backgroundColor: MaterialStateProperty.all<Color>(Colors.red)),
                //       child: Text('Simpan'),
                //       onPressed: () {
                //       },
                //     )
                // ),
              ],
            )
        )
    );
  }
}