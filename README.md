<div class="markdown prose w-full break-words dark:prose-invert dark"><h1>Discord Personal Butler</h1><p>A versatile Discord bot that serves as a personal butler, playing sound effects based on user-defined events.</p><h2>Prerequisites</h2><p>Before running the bot, make sure you have the following:</p><ul><li>Python 3.7 or higher installed</li><li><a href="https://ffmpeg.org/" target="_new">FFmpeg</a> installed and added to the system's PATH environment variable</li><li>Discord bot token obtained from the Discord Developer Portal</li></ul><h2>Installation</h2><ol><li>Clone this repository to your local machine.</li><li>Install the required dependencies by running the following command:</li></ol><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span> </span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg> </button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language- ">pip install -r requirements.txt
</code></div></div></pre><ol start="3"><li>Create a file named <code>.env</code> in the project directory and add the following environment variables:</li></ol><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>plaintext</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg> </button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-plaintext">DISCORD_BOT_TOKEN=&lt;your-discord-bot-token&gt;
FFMPEG_PATH=&lt;path-to-ffmpeg-executable&gt;
</code></div></div></pre><p>Additionally, for each sound key defined in <code>Data/Sounds.json</code>, add an environment variable with the format <code>SOUND_&lt;sound_key&gt;=&lt;sound_file_path&gt;</code>. For example:</p><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>plaintext</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg> </button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-plaintext">SOUND_ALERT=/path/to/alert.mp3
SOUND_GOODBYE=/path/to/goodbye.mp3
SOUND_FART=/path/to/fart.mp3
...
</code></div></div></pre><ol start="4"><li>Create the necessary data files:</li></ol><ul><li>Create a JSON file named <code>Data/Sounds.json</code> and define the available sound keys. For example:</li></ul><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>json</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg> </button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-json"><span class="hljs-punctuation">[</span>
  <span class="hljs-string">"ALERT"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-string">"GOODBYE"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-string">"FART"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-string">"ALLAH"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-string">"XFART"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-string">"MEXI"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-string">"HELLO"</span>
<span class="hljs-punctuation">]</span>
</code></div></div></pre><ul><li>Create a JSON file named <code>Data/Users.json</code> and define the user-specific sound events. For example:</li></ul><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>json</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg> </button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-json"><span class="hljs-punctuation">{</span>
  <span class="hljs-attr">"user1#1111"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
    <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">"event"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"leave"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"sound"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"XFART"</span>
    <span class="hljs-punctuation">}</span><span class="hljs-punctuation">,</span>
    <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">"event"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"join"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"sound"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"MEXI"</span>
    <span class="hljs-punctuation">}</span>
  <span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"user2#2222"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
    <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">"event"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"join"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"sound"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"HELLO"</span>
    <span class="hljs-punctuation">}</span>
  <span class="hljs-punctuation">]</span>
<span class="hljs-punctuation">}</span>
</code></div></div></pre><ol start="5"><li>Run the bot by executing the following command:</li></ol><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span> </span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg> </button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language- ">python PersonalGreeter.py
</code></div></div></pre><h2>Usage</h2><p>The Discord Personal Butler bot listens for voice state updates in the connected Discord server and plays the corresponding sound effects based on user-defined events.</p><ul><li>To trigger a sound effect when a user joins a voice channel, add an entry in <code>Data/Users.json</code> for the specific user:</li></ul><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>json</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg> </button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-json"><span class="hljs-punctuation">{</span>
  <span class="hljs-attr">"user#1234"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
    <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">"event"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"join"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"sound"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"SOUND_KEY"</span>
    <span class="hljs-punctuation">}</span>
  <span class="hljs-punctuation">]</span>
<span class="hljs-punctuation">}</span>
</code></div></div></pre><p>Replace <code>"user#1234"</code> with the user's Discord username and discriminator, and <code>"SOUND_KEY"</code> with one of the available sound keys defined in <code>Data/Sounds.json</code>.</p><ul><li>To trigger a sound effect when a user leaves a voice channel, add an entry in <code>Data/Users.json</code> for the specific user:</li></ul><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>json</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg> </button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-json"><span class="hljs-punctuation">{</span>
  <span class="hljs-attr">"user#1234"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
    <span class="hljs-punctuation">{</span>
      <span class="hljs-attr">"event"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"leave"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"sound"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"SOUND_KEY"</span>
    <span class="hljs-punctuation">}</span>
  <span class="hljs-punctuation">]</span>
<span class="hljs-punctuation">}</span>
</code></div></div></pre><p>Replace <code>"user#1234"</code> with the user's Discord username and discriminator, and <code>"SOUND_KEY"</code> with one of the available sound keys defined in <code>Data/Sounds.json</code>.</p><ul><li>To stop the bot and disconnect it from all voice channels, use the command prefix <code>!</code> followed by <code>stop</code>:</li></ul><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>arduino</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg> </button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-arduino">!stop
</code></div></div></pre><h2>Contributing</h2><p>Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.</p><p>Please make sure to update tests as appropriate.</p><h2>License</h2><p><a href="https://choosealicense.com/licenses/mit/" target="_new">MIT</a></p></div>
