async function send_message(question, user_id, session_id) {
  return fetch("https://vora-ai-back-end.vercel.app/send_message", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_id: user_id,
      session_id: session_id,
      question: question,
    }),
  }).then(async (response) => {
    const errorText = await response.text();
    if (!response.ok) return { status: response.status, data: errorText };

    return { status: response.status, data: errorText };
  });
}

async function register(user_name, password) {
  return fetch("https://vora-ai-back-end.vercel.app/register", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_name: user_name,
      password: password,
    }),
  }).then(async (response) => {
    const errorText = await response.text();
    if (!response.ok) return { status: response.status, data: errorText };
    return { status: response.status, data: errorText };
  });
}

async function login(user_name, password) {
  return fetch("https://vora-ai-back-end.vercel.app/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_name: user_name,
      password: password,
    }),
  }).then(async (response) => {
    const errorText = await response.text();
    if (!response.ok) return { status: response.status, data: errorText };
    return { status: response.status, data: errorText };
  });
}

async function main() {
  const response = await register("Joao22222", "2341312312");
  console.log(response);
}

main();
