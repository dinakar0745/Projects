import 'package:flutter/material.dart';
import 'package:expence/datetime/date_time_helper.dart';
import 'package:expence/models/expense_item.dart';
import 'package:expence/data/expense_data.dart';
import 'package:provider/provider.dart';
import 'package:expence/components/expense_tile.dart';
import 'package:expence/components/expense_summary.dart';


class HomePage extends StatefulWidget{
  const HomePage({super.key});

  @override
 _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  //text Controllers
  final newExpenseNameController = TextEditingController();
  final newExpenseAmountController = TextEditingController();

  //add new Expense
  void addNewExpense(){
    showDialog(
      context: context,
      builder: (context) =>AlertDialog(
        title: Text('Add new Expense'),
        content: Column(
          mainAxisSize:MainAxisSize.min,
          children: [
            //Expense Name
            TextField(
              controller: newExpenseNameController,
            ),

            //Expense Amount
            TextField(
              controller: newExpenseAmountController,
            ),
          ],
        ),
        actions:[

          //save button
          MaterialButton(
            onPressed: save,
            child: Text('Save'),
          ),

          //cancel button
          MaterialButton(
            onPressed: cancel,
            child: Text('Cancel'),
          ),
        ],
      ),
    );
  }

  //save
  void save() {
    ExpenseItem newExpense = ExpenseItem(
      name: newExpenseNameController.text,
      amount: newExpenseAmountController.text,
      dateTime: DateTime.now(),
    );
    Provider.of<ExpenseData>(context, listen: false).addNewExpense(newExpense);

    Navigator.pop(context);
    clear();
  }

  // cancel
  void cancel() {
    Navigator.pop(context);
    clear();
  }

  //clear controllers
  void clear(){
    newExpenseNameController.clear();
    newExpenseAmountController.clear();
  }

  @override
  Widget build(BuildContext context){
    return Consumer<ExpenseData>(
      builder: (context,value,child) => Scaffold(
        backgroundColor:Colors.grey[300],
        floatingActionButton: FloatingActionButton(
          onPressed: addNewExpense,
          child:Icon(Icons.add),
        ),
        body: ListView(children: [
          //weekly summary
          ExpenseSummary(startOfWeek: value.startOfWeekDate()),

          // expense list
          ListView.builder(
            shrinkWrap: true,
            physics: const NeverScrollableScrollPhysics(),
            itemCount: value.getAllExpenseList().length,
            itemBuilder: (context, index) => ExpenseTile(
              name: value.getAllExpenseList()[index].name,
              amount: value.getAllExpenseList()[index].amount,
              dateTime: value.getAllExpenseList()[index].dateTime,
            ),
          ),
        ]),
      ),
    );
  }
}