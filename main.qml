import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.12

Window {
    id: mainWindow
    width: 420
    height: 400
    visible: true
    color: "#00000000"
    title: qsTr("Hello World")
    flags: Qt.FramelessWindowHint

    Rectangle {
        id: appRect
        visible: true
        anchors.fill: parent
        clip: false
        anchors.rightMargin: 5
        anchors.leftMargin: 5
        anchors.bottomMargin: 5
        anchors.topMargin: 5
        radius: 5
        border.width: 0

        Rectangle {
            id: topBar
            height: 30
            color: "#247c9b"
            radius: 0
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 0

            DragHandler {
                onActiveChanged: if (active) {
                                     mainWindow.startSystemMove()
                                 }
            }

            Label {
                id: titleLbl
                x: 179
                y: 7
                color: "#ffffff"
                text: qsTr("Midpoint Visualizer")
                anchors.verticalCenter: parent.verticalCenter
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.horizontalCenter: parent.horizontalCenter
            }

            TopButton {
                id: closeButton
                x: 370
                width: 30
                text: "X"
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.rightMargin: 0
                anchors.bottomMargin: 0
                anchors.topMargin: 0
                onClicked: mainWindow.close()
            }
        }

        Rectangle {
            id: contentRect
            width: 200
            color: "#353535"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: topBar.bottom
            anchors.bottom: parent.bottom
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.bottomMargin: 0
            anchors.topMargin: 0

            GridLayout {
                id: gridLayout
                anchors.fill: parent
                columns: 3
                rows: 4
                anchors.rightMargin: 10
                anchors.leftMargin: 10
                anchors.bottomMargin: 10
                anchors.topMargin: 10

                Label {
                    id: pointLbl
                    color: "#e1e1e1"
                    text: qsTr("Point")
                    font.bold: true
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    Layout.fillHeight: false
                    Layout.fillWidth: false
                    font.pointSize: 15
                }

                Label {
                    id: xLbl
                    color: "#e1e1e1"
                    text: qsTr("X")
                    font.bold: true
                    horizontalAlignment: Text.AlignLeft
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    font.pointSize: 15
                }

                Label {
                    id: yLbl
                    color: "#e1e1e1"
                    text: qsTr("Y")
                    font.bold: true
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    font.pointSize: 15
                }

                Label {
                    id: coord1Lbl
                    color: "#e1e1e1"
                    text: qsTr("1")
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    font.pointSize: 15
                }

                SpinBox {
                    id: x1Sb
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    value: _coord1.x
                    onValueChanged: _coord1.x = value
                }

                SpinBox {
                    id: y1Sb1
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    value: _coord1.y
                    onValueChanged: _coord1.y = value
                }

                Label {
                    id: coord2Lbl
                    color: "#e1e1e1"
                    text: qsTr("2")
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    font.pointSize: 15
                }

                SpinBox {
                    id: x2Sb
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    value: _coord2.x
                    onValueChanged: _coord2.x = value
                }

                SpinBox {
                    id: y2Sb
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    value: _coord2.y
                    onValueChanged: _coord2.y = value
                }

                Label {
                    id: midpointLbl
                    color: "#e1e1e1"
                    text: qsTr("Midpoint:")
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    font.pointSize: 15
                }

                Label {
                    id: xMidLbl
                    property string modelValue
                    color: "#e1e1e1"
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    modelValue: _midpoint.x
                    text: modelValue.toString()
                    font.pointSize: 15
                }

                Label {
                    id: yMidLbl
                    property string modelValue
                    color: "#e1e1e1"
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    modelValue: _midpoint.y
                    text: modelValue.toString()
                    font.pointSize: 15
                }

            }
        }
    }
}
