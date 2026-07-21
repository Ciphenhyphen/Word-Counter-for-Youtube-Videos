browser.contextMenus.create({
    id: "yt_chart_ext",
    title: "View word occurrences with YT_Ch",
    contexts: ["tab", "link"]
});

browser.contextMenus.onClicked.addListener((info, tab) => {
    // get link -> parse to obtain vid ID -> send ID to native application
    // verify URL before saving into variable
    
    if(info.linkUrl){
        var url = info.linkUrl;
        var ID = url.replace(/^.*?(\?|&)(v=([^&]+)).*$/i,'$3'); 
        sendToNative(ID);
    }else{
        console.log(error)
    }
    
});

var port = null

function connect(){
    if (port == null){
        port = browser.runtime.connectNative("YT_Chart_ext");
        port.onMessage.addListener(onNativeMessage);
        port.onDisconnect.addListener(onDisconnected);
    }
}

function onNativeMessage(messageToSend){
    console.log("Received" + messageToSend)
}

function onDisconnected(p){
    if(p.error){
        console.log(`Disconnected due to an error: ${p.error.message}`);
    }else{
        console.log('Disconnected', p);
    }
}

function sendToNative(ID){
    port.postMessage(ID);
}