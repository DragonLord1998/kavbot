
const { Client, Intents } = require('discord.js');
const client = new Client({ intents: [Intents.FLAGS.GUILDS] });

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('interactionCreate', async interaction => {
  if (!interaction.isCommand()) return;

  if (interaction.commandName === 'hi') {
    console.log("Got command");
    await interaction.reply('Pong!');
  }
});

client.login('ODc3NDU5NzcyNjE2NjIyMTMw.YRy8GA.wkgrn_-dV-zQgRXGkoWJy02dEWE');