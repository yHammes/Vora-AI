function enviar_mensagem(question, user_id, session_id) {
  fetch("https://vora-ai-back-end.vercel.app/send_message", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_id: user_id,
      session_id: session_id,
      question: question,
    }),
  }).then((response) => {
    if (!response.ok) {
      throw new Error("HTTP error: " + response.status);
    }
    console.log(response);
    return response.json();
  });
}

answer = enviar_mensagem("boa noite", 6, 22);
