function add_impression(user_id, event_type, content_id, session_id) {
       $.ajax({
              type: 'POST',
              url: '/log',
              data: {
                     "event_type": event_type,
                     "user_id": user_id,
                     "content_id": content_id,
                     "session_id": session_id
              },
              fail: function () {
                     console.log('log failed(' + event_type + ')')
              }
       })
};