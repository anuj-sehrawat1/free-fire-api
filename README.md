<body>
  <h1>Free Fire Player Info API</h1>
  <p>Get public data of any Free Fire player using their UID. This API decrypts and parses Free Fire's internal responses to provide data like player name, level, likes, Booyah pass level, bio, guild details, etc.</p>

  <p><strong>Author:</strong> ANUJ SEHRAWAT<br/>
     <strong>Telegram:</strong> <a href="https://t.me/tg_anujsehrawat">@tg_anujsehrawat</a><br/>
     <strong>Instagram:</strong> <a href="https://instagram.com/a9x2k">@a9x2k</a></p>

  <hr/>

  <h2>⚠️ Project Status: Deprecated</h2>

This API was built for learning purposes.
The Free Fire endpoints are no longer active due to upstream changes.
Architecture and implementation remain relevant.


  <h2>Demo</h2>
  <p>Try the API live:<br/>
  <a href="https://anuj-free-fire-api.vercel.app/player-info?id=2396094646" target="_blank">
    https://anuj-free-fire-api.vercel.app/player-info?id=2396094646
  </a></p>

  <h2>How It Works</h2>
  <ul>
    <li>Takes Free Fire UID as a query parameter.</li>
    <li>Encrypts the UID using AES and protocol format.</li>
    <li>Fetches a JWT token from external microservice.</li>
    <li>Sends POST request to Free Fire internal endpoint.</li>
    <li>Parses binary response using protobuf decoder.</li>
    <li>Extracts player info, guild data, and pet details.</li>
  </ul>

  <h2>API Endpoint</h2>
  <p><strong>GET</strong> <code>/player-info?id=&lt;PLAYER_UID&gt;</code></p>

  <h3>Query Parameters</h3>
  <table>
    <thead>
      <tr><th>Param</th><th>Type</th><th>Required</th><th>Description</th></tr>
    </thead>
    <tbody>
      <tr><td>id</td><td>string</td><td>Yes</td><td>Free Fire player UID</td></tr>
    </tbody>
  </table>

  <h3>Sample Response</h3>
  <pre><code>{
  "status": "success",
  "message": "Player information retrieved successfully",
  "data": {
    "basic_info": {
      "name": "ＦＬＡＳＯＮㅤ",
      "id": "2396094646",
      "likes": 1770,
      "level": 54,
      "server": "IND",
      "bio": "[c][b]Keep it Private, Until it Permanent",
      "booyah_pass_level": 14,
      "account_created": "2020-09-25 13:38:49"
    },
    "animal": null,
    "Guild": {
      "name": "ƘᴀʟㅤƳᴜɢㅤㅤㅤ",
      "id": 3037307585,
      "level": 3,
      "members_count": 16,
      "leader": {
        "id": 1970041770,
        "name": ".•ᴋᴇɴᴢᴏ༊*·",
        "level": 69,
        "booyah_pass_level": 28,
        "likes": 13185,
        "account_created": "2020-04-30 11:06:22"
      }
    }
  },
  "credits": "ANUJ SEHRAWAT (tg- @tg_anujsehrawat, insta- @a9x2k)",
  "timestamp": "2025-04-11 20:06:45"
}</code></pre>

  <h2>Error Codes</h2>
  <table>
    <thead>
      <tr><th>HTTP Code</th><th>Error Message</th><th>Reason / Fix</th></tr>
    </thead>
    <tbody>
      <tr><td>400</td><td>Player ID is required</td><td>Query param <code>id</code> missing</td></tr>
      <tr><td>500</td><td>Failed to generate JWT token</td><td>Token fetch failed</td></tr>
      <tr><td>500</td><td>Failed to parse player information: &lt;error&gt;</td><td>Format change or wrong UID</td></tr>
      <tr><td>502/503</td><td>API request failed with status code: xxx</td><td>Server down or rate-limited</td></tr>
      <tr><td>500</td><td>An unexpected error occurred: &lt;error&gt;</td><td>Internal exception or bug</td></tr>
    </tbody>
  </table>

  <h2>File Structure</h2>
  <table>
    <thead>
      <tr><th>File</th><th>Description</th></tr>
    </thead>
    <tbody>
      <tr><td>app.py</td><td>Main Flask app with logic for player info extraction</td></tr>
      <tr><td>index.py</td><td>Entrypoint for Vercel</td></tr>
      <tr><td>wsgi.py</td><td>Dev server entrypoint</td></tr>
      <tr><td>requirements.txt</td><td>Required dependencies</td></tr>
      <tr><td>vercel.json</td><td>Vercel deployment configuration</td></tr>
    </tbody>
  </table>

  <h2>Deploying to Vercel</h2>
  <p>API is pre-configured for Vercel.</p>

  <h3>Option 1: One-Click Deploy</h3>
  <p>
    <a href="https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fanuj-sehrawat1%2Ffree-fire-api&project-name=free-fire-api&repository-name=free-fire-api" target="_blank">
      <strong>→ Click here to Deploy on Vercel</strong>
    </a>
  </p>

  <h3>Option 2: Manual Deployment</h3>
  <ol>
    <li>Fork or clone this repo</li>
    <li>Install Vercel CLI:<br/>
      <code>npm install -g vercel</code>
    </li>
    <li>Run this to deploy:<br/>
      <code>vercel --prod</code>
    </li>
  </ol>

  <h2>Credits</h2>
  <p>Developed by <strong>Anuj Sehrawat</strong><br/>
  Telegram: <a href="https://t.me/tg_anujsehrawat">@tg_anujsehrawat</a><br/>
  Instagram: <a href="https://instagram.com/a9x2k">@a9x2k</a></p>
</body>
