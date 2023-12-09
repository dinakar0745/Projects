import 'package:expence/bargraph/individual_bar.dart';

class BarData {
  final double sunAmount;
  final double monAmount;
  final double tueAmount;
  final double wenAmount;
  final double thurAmount;
  final double friAmount;
  final double satAmount;

  BarData({
    required this.sunAmount;
    required this.monAmount;
    required this.tueAmount;
    required this.wenAmount;
    required this.thurAmount;
    required this.friAmount;
    required this.satAmount;
  });

  List<IndividualBar> barData=[];

  //Initilize bar data
  void initializeBarData() {
    barData = [
      //sun
      IndividualBar(x=0,y:sunAmount),
      
      //mon
      IndividualBar(x=1,y:monAmount),
      
      //tue
      IndividualBar(x=2,y:tueAmount),
      
      //wed
      IndividualBar(x=3,y:wenAmount),
      
      //thur
      IndividualBar(x=4,y:thurAmount),
      
      //fri
      IndividualBar(x=5,y:friAmount),
      
      //sat
      IndividualBar(x=6,y:satAmount),
    ];
  }
}