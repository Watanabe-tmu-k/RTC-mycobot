# MyCobotControllerRTC
## 概要
* mycobot制御のためのRTC．
* URL-"elephantrobotics/pymycobot"
  * https://github.com/elephantrobotics/pymycobot

## コンポーネント内容
1. MyCobotControllerPy
   * InPort → アーム先端手の座標(xyz)の位置に移動させる
      * mycobot.send_coords([x,y,z,rx,ry,rz],speed,0)
   * InPort → グリッパーの開閉
      * mycobot.set_gripper_value(value, speed)
2. SendPoseData
   * アーム先端手の座標を送信する(x,y,z)
   * グリッパーの状態を送信する(0:open, 1:close)
   * コンフィギュレーションで値を変更(slider)
