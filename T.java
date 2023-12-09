import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class TimeTableGenerator extends JFrame {
    private JLabel teacherLabel, classLabel, subjectLabel, durationLabel;
    private JComboBox<String> teacherComboBox, classComboBox, subjectComboBox, durationComboBox;
    private JButton generateButton;
    private JTextArea timeTableTextArea;

    private String[] teachers = { "Teacher 1", "Teacher 2", "Teacher 3", "Teacher 4", "Teacher 5" };
    private String[] classes = { "Class 1", "Class 2", "Class 3", "Class 4", "Class 5" };
    private String[] subjects = { "Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5" };
    private String[] durations = { "1 Hour", "2 Hours", "3 Hours" };

    public TimeTableGenerator() {
        super("Time Table Generator");

        // Create labels, combo boxes, button, and text area

        // ...

        // Add components to content pane

        // ...

        // Add event listeners

        // ...
    }

    private void generateTimeTable() {
        String teacher = (String) teacherComboBox.getSelectedItem();
        String className = (String) classComboBox.getSelectedItem();
        String subject = (String) subjectComboBox.getSelectedItem();
        String duration = (String) durationComboBox.getSelectedItem();

        // Generate timetable logic

        int days = 5; // Number of days in a week
        int periodsPerDay = 6; // Number of periods per day

        // Create a two-dimensional array for the timetable
        String[][] timetable = new String[periodsPerDay][days];

        // Populate the timetable with the selected options
        for (int day = 0; day < days; day++) {
            for (int period = 0; period < periodsPerDay; period++) {
                timetable[period][day] = teacher + " - " + className + " - " + subject + " (" + duration + ")";
            }
        }

        // Format the timetable into a matrix
        StringBuilder result = new StringBuilder();

        // Print header row with days
        result.append(String.format("%-15s", "Period/Day"));
        for (int day = 0; day < days; day++) {
            result.append(String.format("%-20s", "Day " + (day + 1)));
        }
        result.append("\n");

        // Print timetable rows
        for (int period = 0; period < periodsPerDay; period++) {
            result.append(String.format("%-15s", "Period " + (period + 1)));

            for (int day = 0; day < days; day++) {
                result.append(String.format("%-20s", timetable[period][day]));
            }

            result.append("\n");
        }

        timeTableTextArea.setText(result.toString());
    }

    // Main method

    // ...
}
