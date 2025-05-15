import mediapipe as mp
import cv2
import numpy as np
import os


def init_result_back(obj):
    global g_resultBack
    g_resultBack = obj


def bigdirdetect(source,save_dir):
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')  # 设置输出视频为mp4格式
    # cap_fps是帧率，可以根据随意设置
    cap_fps = 15
    videoname=os.path.basename(source)

    # 初始化MediaPipe Pose模块
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    #vediopath = r'tw.mp4'
    # 摄像头捕捉
    cap = cv2.VideoCapture(source)
    cc=0
    with mp_pose.Pose(min_detection_confidence=0.5,
                      min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame1 = frame.copy()
            # 将BGR帧转换为RGB帧
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(frame_rgb)
            # 绘制关键点
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            frame1 = cv2.cvtColor(frame1,cv2.COLOR_BGR2RGB)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results_output = [frame1, frame]
            resout = np.hstack((frame1, frame))
            cc=cc+1
            if cc == 1:
                savevideo = 'output_' + videoname
                height, width = resout.shape[0:2]
                sizex = (width, height)
                videox = cv2.VideoWriter(savevideo, fourcc, cap_fps, sizex)
            resout = cv2.cvtColor(resout, cv2.COLOR_BGR2RGB)
            videox.write(resout)

            g_resultBack.result_back_detect(results_output)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
    videox.release()
    cap.release()
    cv2.destroyAllWindows()


    #return img1,save_path,temp_quxaian_numc

if __name__ == '__main__':

    # source = r'F:\testdata'
    # start_time = 7111345
    # stop_time = 10052244
    # weights = r'best.pt'
    # save_dir = os.getcwd()+'\\DetectResults'
    # if not os.path.isdir(save_dir):
    #     os.makedirs(save_dir)
    #
    # with torch.no_grad():
    #     bigdirdetect(source,weights,save_dir, start_time, stop_time)


    print('Completed')

