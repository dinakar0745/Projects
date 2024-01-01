import 'package:flutter/material.dart';
import 'package:agora_rtc_engine/rtc_engine.dart';
import 'package:agora_rtc_engine/rtc_local_view.dart' as rtc_local_view;
import 'package:agora_rtc_engine/rtc_remote_view.dart' as rtc_remote_view;



class IntercomScreen extends StatefulWidget {
  final String appId;
  final String token;
  final int channelId;

  const IntercomScreen({super.key, required this.appId, required this.token, required this.channelId});

  @override
  _IntercomScreenState createState() => _IntercomScreenState();
}

class _IntercomScreenState extends State<IntercomScreen> {
  late RtcEngine _engine;

  @override
  void initState() {
    super.initState();
    initializeRTC();
  }

  Future<void> initializeRTC() async {
    _engine = await RtcEngine.create(widget.appId);

    await _engine.enableAudio(); // Enable audio

    _engine.setEventHandler(RtcEngineEventHandler(
      joinChannelSuccess: (String channel, int uid, int elapsed) {
        print('Join channel success');
      },
      userJoined: (int uid, int elapsed) {
        print('User joined: $uid');
      },
      userOffline: (int uid, UserOfflineReason reason) {
        print('User offline: $uid');
      },
    ));

    await _engine.joinChannel(widget.token, widget.channelId.toString(), null, 0);
  }

  @override
  void dispose() {
    _engine.leaveChannel();
    _engine.destroy();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Intercom'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Expanded(
              child: Stack(
                children: [
                  rtc_remote_view.SurfaceView(
                    uid: 0,
                  ),
                  rtc_local_view.SurfaceView(
                    channelId: 'YOUR_CHANNEL_ID',
                  ),
                ],
              ),
            ),
            const SizedBox(height: 20),
            // ElevatedButton(
            //   onPressed: () {
            //     _engine.muteLocalAudioStream(!_engine.isLocalAudioMuted);
            //     setState(() {});
            //   },
            //   child: Text(_engine.isLocalAudioMuted ? 'Unmute' : 'Mute'),
            // ),
          ],
        ),
      ),
    );
  }
}


class MyApp extends StatelessWidget {
  final String appId = 'ec4d3e2b231141aab4e86c0945b6ad46';
  final String token = 'YOUR_TOKEN';
  final int channelId = 123;

  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Intercom App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const IntercomScreen(appId: appId, token: token, channelId: channelId),
    );
  }
}

void main() {
  runApp(const MyApp());
}
