import rospy
# from std_msgs.msg import String
# from std_msgs.msg import Bool
# from std_msgs.msg import Int32
# from spar_msgs.msg import TargetLocalisation
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

# def test_callback(msg):
#     rospy.loginfo("received test msg: '%s'" % msg.data)

def main():
    rospy.init_node('target_viz', anonymous=True)
    rospy.loginfo('starting gcs target visualization')

    pub = rospy.Publisher('targetviz', Marker, queue_size=10)
    # rospy.Subscriber('vocal/test', String, test_callback)

    marker = Marker()
    marker.header.frame_id = "map"
    marker.header.stamp = rospy.Time.now()
    marker.type = 1
    marker.id = 0
    marker.pose.position.x = 0
    marker.pose.position.y = 0
    marker.pose.position.z = 0
    marker.scale.x = 1.0
    marker.scale.y = 1.0
    marker.scale.z = 1.0
    marker.color.a = 1.0
    marker.text = "TEST"
    marker.points = []
    p = Point()
    p.x = 0
    p.y = 0
    p.z = 0
    #marker.points.append(p)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(marker)
        rate.sleep()

if __name__ == '__main__':
    main()
