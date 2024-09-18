import 'dart:async';
import 'package:camera/camera.dart';
import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart' show kIsWeb;
import 'all.dart';


Future<void> main() async {
  if (kIsWeb) {
    runApp(
      MaterialApp(
        debugShowCheckedModeBanner: true,
        theme: new ThemeData(scaffoldBackgroundColor: const Color(0xFFEFEFEF)),
        initialRoute: '/',
        routes: {
          '/': (context) => LoginPage(),
          '/forgot-password/': (context) => ForgotPage(),
          '/registrations/': (context) => RegisterPage(),
          '/home/profile/verification/selfie/': (context) => WebCameraPage(),
        },
      ),
    );
  } else {
    WidgetsFlutterBinding.ensureInitialized();
    final cameras = await availableCameras();

    runApp(
      MaterialApp(
        debugShowCheckedModeBanner: true,
        theme: new ThemeData(scaffoldBackgroundColor: const Color(0xFFEFEFEF)),
        initialRoute: '/',
        routes: {
          '/': (context) => OnBoardingScreen(),
          '/login/': (context) => LoginPage(),
          '/forgot-password/': (context) => ForgotPage(),
          '/registrations/': (context) => RegisterPage(),
          '/home/': (context) => IndexPage(),
          '/home/activity/': (context) => ActivityPage(),
          '/home/asset/': (context) => AssetPage(),
          '/home/buy/qris/': (context) => QRPage(),
          '/home/index/': (context) => HomePage(),
          '/home/funding/': (context) => FundingPage(),
          '/home/profile/': (context) => ProfilePage(),
          '/home/profile/messages/': (context) => MessagePage(),
          '/home/profile/verification/': (context) => VerificationPage(),
          '/home/profile/verification/selfie/': (context) => CameraPage(camera: cameras[1],),
          '/home/profile/verification/principal-saving/': (context) => PrincipalSavingPage(),
          '/home/profile/verification/member-agreement/': (context) => MemberAgreementPage(),
          '/home/profile/verification/profile/': (context) => ProfileVerificationPage(),
          '/home/profile/change-password/': (context) => ChangePasswordPage(),
          '/home/profile/change-pin/': (context) => ChangePinPage(),
          '/home/profile/account-bank/': (context) => AccountBankPage(),
          '/home/profile/account-bank/add/': (context) => AddAccountBankPage(),
        },
      ),
    );
  }
}