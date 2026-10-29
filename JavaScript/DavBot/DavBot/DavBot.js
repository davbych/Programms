const mineflayer  = require("mineflayer");

//let ip = "create_makaka.aternos.me";
//let port = 30922;

let ip = "localhost";
let port = "59053";

const DavBot = mineflayer.createBot({
    host: ip,
    username: "DavBot",
    auth: "offline",
    port: port,
    version: "1.21.11",
})


DavBot.once("spawn", () => {
    DavBot.chat("Здравствуйте, товарищи! \nОбращайтесь ко мне так: DavBot, ты бот?");
    console.log("\n - DavBot на сервере '" + ip + ":" + port + "'! \n\n|------КОМАНДЫ ДЛЯ DAVBOT------|\n1. DavBot, привет!\n2. DavBot, ты бот?\n3. DavBot, где ты?\n4. DavBot, иди ко мне.\n5*. DavBot, спой гимн СССР.\n6. DavBot, выйди. / выйди пожалуйста.\n\n|------СООБЩЕНИЯ ИЗ ЧАТА ------|");
})

DavBot.on("message", (message) => {console.log(message.toAnsi())})

DavBot.on("error", (err) => {console.log(err)})
DavBot.on("kicked", (kicked) => {console.log(kicked)})

//timeout: 1000 = 1 секунда.
DavBot.on("chat", (username, message) => {
    if (username == DavBot.username) return;
    if (username == "Davbych" && message == "DavBot, привет!") {setTimeout(() => DavBot.chat(username + ", здравствуйте! Я как раз хотел вас поприветствовать первым!"), 2000)}
    if (username == "Davbych" && message == "DavBot, ты бот?") {DavBot.chat(username + ", агась. Я - бот.")} else if (message == "Davbot, ты бот?") {DavBot.chat(username + ", да, но тебе я не подчиняюсь.")}
    if (message == "DavBot, ты где?") {DavBot.chat(username + ", я нахожусь на координатах: x, y, z");}
    if (message == "Да" || message == "да") {DavBot.chat("Да.")}
    if (username == "Davbych" && message == "DavBot, выйди") {DavBot.quit();} else if (message == "DavBot, выйди") {DavBot.chat(username + ", а как же волшебное слово? =)");} else if (message == "DavBot, выйди, пожалуйста") DavBot.quit();
})






/*
DavBot.on('chat',(username,message)=>{
    if(username === DavBot.username) return
    switch (message){
        case 'Спать':
            goToSleep()
            break
        case 'Вставай':
            wakeUp()
            break
    }
});

DavBot.on('sleep',()=>{
DavBot.chat('Спокойной ночи')});
DavBot.on('wake',()=>{
    DavBot.chat('Доброе утро')});

async function goToSleep(){
    const bed = DavBot.findBlock({
        matching: block => DavBot.isABed(block)})
    if (bed) {
        try {
            await DavBot.sleep(bed)
            DavBot.chat("Я сплю")
        } catch (err) {
            DavBot.chat(`Я не могу уснуть: ${err.message}`) }
    } else {
        DavBot.chat('По близости нет кровати') } }

async function  wakeUp() {
    try {
        await DavBot.wake()
    } catch (err) {
        DavBot.chat(`Я не могу проснуться: ${err.message}`)
    }}*/
