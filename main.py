import cv2
import numpy as np
import screen_brightness_control as sbc
from hand_tracker import HandTracker

# Initialize Hand Tracker
tracker = HandTracker()

# Start webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Mirror effect
    results = tracker.detect_hands(frame)

    # Draw landmarks
    tracker.draw_landmarks(frame, results)

    # Get finger positions
    thumb_pos, index_pos = tracker.get_finger_positions(results, frame.shape)

    if thumb_pos and index_pos:
        x1, y1 = thumb_pos
        x2, y2 = index_pos

        # Draw circles on fingertips
        cv2.circle(frame, (x1, y1), 10, (0, 255, 0), -1)
        cv2.circle(frame, (x2, y2), 10, (0, 255, 0), -1)

        # Calculate distance between thumb and index finger
        distance = np.linalg.norm([x2 - x1, y2 - y1])

        # Map distance to brightness (scaled between 10% - 100%)
        brightness = np.interp(distance, [30, 200], [10, 100])
        sbc.set_brightness(int(brightness))

        # Display brightness level
        cv2.putText(frame, f'Brightness: {int(brightness)}%', (50, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Show output
    cv2.imshow("Brightness Control", frame)

    # Exit on 'Q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
