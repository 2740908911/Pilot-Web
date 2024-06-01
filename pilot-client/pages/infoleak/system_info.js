(function() {
    var internalAPI = "http://10.1.20.6:8081/this/is/the/second/system_info/vulnerability";
    // 这个js代码中，泄露了系统中内网IP，可能被攻击者进一步利用而扩大危害。

    function obscureData(data) {
        return data.split('').map((c, i) => String.fromCharCode(c.charCodeAt(0) + i % 5)).join('');
    }

    function fetchData(url, callback) {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                callback(xhr.responseText);
            }
        };
        xhr.open('GET', url, true);
        xhr.send();
    }

    function processResponse(data) {
        console.log("Response Received: ", data);
    }

    function shuffleString(str) {
        var arr = str.split('');
        for (let i = arr.length - 1; i > 0; i--) {
            let j = Math.floor(Math.random() * (i + 1));
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
        return arr.join('');
    }

    function periodicCheck() {
        setInterval(() => {
            fetchData(internalAPI, processResponse);
        }, 10000);
    }

    function init() {
        console.log("Initializing application...");
        periodicCheck();
    }

})();
