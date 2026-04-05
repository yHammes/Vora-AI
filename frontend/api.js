const BASE_URL = "https://vora-ai-back-end.vercel.app";

async function request(endpoint, body) {
  const url = `${BASE_URL}/${endpoint}`;
  console.log(`[${endpoint}] Request started`, { url, ...body });

  try {
    const response = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    const data = await response.text();
    const level = response.ok ? "log" : "warn";
    console[level](
      `[${endpoint}] Request ${response.ok ? "successful" : "failed"}`,
      { status: response.status, data },
    );

    return { status: response.status, data };
  } catch (error) {
    console.error(`[${endpoint}] Unexpected error`, {
      error: error.message,
      stack: error.stack,
    });
    throw error;
  }
}

function send_message(question, user_id, session_id) {
  if (!user_id) {
    window.location.href = "index.html";
    return;
  }

  return request("send_message", { user_id, session_id, question });
}

function register(user_name, password) {
  return request("register", { user_name, password });
}

function login(user_name, password) {
  return request("login", { user_name, password });
}
