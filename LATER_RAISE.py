def later_raise():
    import mediapipe as mp
    import numpy as np
    import time
    import cv2
    from playsound import playsound as pl

    def rightangle(a, b, c):
        a = np.array(a)
        b = np.array(b)
        c = np.array(c)

        rad = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        ang = np.abs(rad * 180) / np.pi

        if ang > 180:
            ang = 360 - ang

        cv2.rectangle(frame, (10, 10), (250, 250), (225, 225, 225), cv2.FILLED)
        cv2.putText(frame, str(int(ang)), tuple(np.multiply(b, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 2,
                    (255, 0, 222), 1, cv2.LINE_AA)
        return ang

    def leftangle(la, lb, lc):
        a = np.array(la)
        b = np.array(lb)
        c = np.array(lc)

        rad = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        ang = np.abs(rad * 180) / np.pi

        if ang > 180:
            ang = 360 - ang
        cv2.rectangle(frame, (400, 600), (950, 660), (0, 225, 225), cv2.FILLED)
        cv2.rectangle(frame, (530, 25), (900, 80), (0, 225, 225), cv2.FILLED)
        cv2.putText(frame, "    LATER RASIE", (453, 60), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 23, 224), 1, cv2.LINE_AA)
        cv2.putText(frame, str(int(ang)), tuple(np.multiply(b, [640, 480]).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 2,
                    (255, 0, 222), 2, cv2.LINE_AA)
        return ang
    wrong_value=0
    counter_value = 0
    list_count = []
    cap = cv2.VideoCapture(0)
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    mp_draw = mp.solutions.drawing_utils
    list_count = []
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    while True:
        ret, frame = cap.read()

        color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = pose.process(color)

        try:
            landmarks_marks = result.pose_landmarks.landmark
            laa = landmarks_marks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks_marks[
                mp_pose.PoseLandmark.LEFT_HIP.value].y
            lbb = landmarks_marks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks_marks[
                mp_pose.PoseLandmark.LEFT_ELBOW.value].y
            lcc = landmarks_marks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks_marks[
                mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
            left_angle = leftangle(laa, lcc, lbb)
            aa= landmarks_marks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, landmarks_marks[
                mp_pose.PoseLandmark.RIGHT_HIP.value].y
            bb = landmarks_marks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks_marks[
                mp_pose.PoseLandmark.RIGHT_ELBOW.value].y
            cc = landmarks_marks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks_marks[
                mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y
            right_angle = rightangle(aa, cc, bb)

            if left_angle > 90 and right_angle > 90:
                stage = "UP"
            elif left_angle < 30 and right_angle < 30 and stage == "UP":
                stage = "DOWN"
                counter_value += 1
                print(counter_value)
                list_count.append(counter_value)
                if counter_value == 30:
                    break

            right = 180 - ((right_angle+left_angle))
            right1 = np.interp(right, [0, 100], [400, 200])
            cv2.rectangle(frame, (1150, 200), (1200, 400), (0, 255, 0), 5)
            cv2.rectangle(frame, (1150, int(right1)), (1200, 400), (0, 23, 224), -1)
            cv2.putText(frame, stage, (10, 130), cv2.FONT_HERSHEY_TRIPLEX, 2, (0, 23, 224), 1, cv2.LINE_AA)

        except:
            pass
        cv2.putText(frame, " STAGE:-", (10, 80), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 23, 224), 1, cv2.LINE_AA)
        cv2.putText(frame, f"Correct Poses: {counter_value}", (10, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,
                    cv2.LINE_AA)
        cv2.putText(frame, f"Incorrect Poses: {wrong_value}", (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, " COUNT:-", (10, 180), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 23, 224), 1, cv2.LINE_AA)
        cv2.putText(frame, str(counter_value), (10, 230), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 23, 224), 1, cv2.LINE_AA)
        cv2.putText(frame, "PRESS a FOR EXIT", (450, 650), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 23, 224), 1, cv2.LINE_AA)

        if result.pose_landmarks:
            mp_draw.draw_landmarks(frame,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)

        cv2.imshow("img", frame)
        if cv2.waitKey(1) & 0xFF == ord("a"):
            break

    cap.release()
    cv2.destroyAllWindows()

    def graph_value():
        # print(list_count)
        return list_count

    return graph_value

#later_raise()