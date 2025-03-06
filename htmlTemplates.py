
css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://imgs.search.brave.com/BREf3KSIGY_38F_At9qDfCTDRGmHs8VZE_3GruQf31g/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4t/aWNvbnMtcG5nLmZs/YXRpY29uLmNvbS8x/MjgvMzc3MS8zNzcx/NDE3LnBuZw" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://imgs.search.brave.com/SOnFSbgRAkA8ZJXScrie_PaKPtkjZNiS3QqEsrS4iSI/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/cG5naXRlbS5jb20v/cGltZ3MvbS81MTYt/NTE2NzMwNF90cmFu/c3BhcmVudC1iYWNr/Z3JvdW5kLXdoaXRl/LXVzZXItaWNvbi1w/bmctcG5nLWRvd25s/b2FkLnBuZw">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''