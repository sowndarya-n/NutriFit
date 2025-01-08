$(document).ready(function() {
    // Function to show loading spinner
    // Function to show loading spinner
function showLoadingSpinner() {
    $('#chat-box').append('<div class="loader"></div>'); // Append loader separately
    $('#chat-input').prop('disabled', true); // Disable input while loading
}

// Function to hide loading spinner
function hideLoadingSpinner() {
    $('#chat-box').find('.loader').remove(); // Remove only the loader
    $('#chat-input').prop('disabled', false); // Re-enable input
}


    // Handle send button click
    $('#send-button').click(function() {
        const userMessage = $('#chat-input').val();
        if (userMessage) {
            console.log('User message:', userMessage);
            $('#chat-box').append('<div><strong>You:</strong> ' + userMessage + '</div>');
            showLoadingSpinner(); // Show spinner while waiting for response

            $.ajax({
                url: '', 
                type: 'POST',
                data: {
                    question: userMessage,
                    csrfmiddlewaretoken: '{{ csrf_token }}'
                },
                success: function(response) {
                    console.log('AJAX request succeeded');
                    console.log('Response:', response);

                    const botResponse = response.bot_response;
                    const chatHistory = response.chat_history;

                    // Debugging: Check chat history structure
                    console.log('Chat History:', chatHistory);

                    // Clear the chat box before appending new messages
                    $('#chat-box').empty();

                    // Append chat history
                    chatHistory.forEach(function(msg) {
                        console.log('Message:', msg); // Debugging: Check each message

                        const role = msg.role === 'user' ? 'You' : 'Bot';
                        $('#chat-box').append('<div><strong>' + role + ':</strong> ' + msg.content + '</div>');
                    });

                    // Optionally display the bot's response if needed
                    if (botResponse) {
                        $('#chat-box').append('<div><strong>Bot:</strong> ' + botResponse + '</div>');
                    }

                    $('#chat-input').val('');
                    hideLoadingSpinner(); // Hide spinner after response
                },
                error: function(xhr, status, error) {
                    console.error('AJAX request failed');
                    console.error('Status:', status);
                    console.error('Error:', error);
                    hideLoadingSpinner(); // Hide spinner on error
                }
            });
        } else {
            console.log('No message entered');
        }
    });
});