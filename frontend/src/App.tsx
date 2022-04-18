import { useEffect, useState } from "react";
import "./App.css";

interface UnreadMesssages {
  messages: Array<any>;
}

function App() {
  const [unreadMessages, setUnreadMessages] = useState({} as UnreadMesssages);
  useEffect(() => {
    // DJANGO RESOURCES NEED TRAILING SLASH FOR SOME GODDAMN REASON
    // PROD_BACKEND - LEAVE THIS ENABLED BY DEFAULT SINCE THIS GETS SERVED until we flag on env vars
    // fetch("https://okada-api.com/unread_messages/")
    //   .then((response) => response.json())
    //   .then((data) =>
    //     setUnreadMessages({messages: data.results })
    //   );
    // LOCAL_BACKEND
    fetch("http://127.0.0.1:8000/unread_messages/")
      .then((response) => response.json())
      .then((data) => {
        setUnreadMessages({ messages: data.results });
      });
  });

  if (unreadMessages && unreadMessages?.messages?.length == 0) {
    return <>No Message Data</>;
  }

  const current_time_ms = Math.floor(Date.now() / 1000);
  const window = 2500; // look back for unread messages in past 120 seconds

  const filteredMessages = unreadMessages?.messages?.filter((message) => {
    if (message.scraper_run_time > current_time_ms - window) {
      return true;
    }
  });
  const unreadCount = filteredMessages?.length;

  // console.log(unreadMessages);

  return (
    <>
      <div>{`${unreadCount} unread messages in past ${window} seconds`}</div>
      <div>
        {filteredMessages?.map((message) => {
          return (
            <div>
              {`${message.sender_name}` + " " + `${message.scraper_run_time}`}
            </div>
          );
        })}
      </div>
    </>
  );
}

export default App;
