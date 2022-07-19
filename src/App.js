import React, { useState, useEffect } from "react";

const App = () => {
  const [data, setData] = useState("");

  useEffect(() => {
    (async function () {
      const { text } = await (await fetch(`/api/message`)).json();
      setData(text);
    })();
  });

  return <div>{data}</div>;
};

export default App;
