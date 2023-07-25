const token = "token"; 
const { Client, GatewayIntentBits, Partials } = require('discord.js');
const client = new Client({
    intents:[
        GatewayIntentBits.Guilds,
    ],
    partials: [Partials.Channel]
});
client.on("ready", () =>{
    const date = new Date();
    console.log("iBot is ready at " + date);
});
client.login(token);