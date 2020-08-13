

function getLink(key_hex, iv_hex, b64_data) {
        var key = CryptoJS.enc.Hex.parse(key_hex);
        var iv = CryptoJS.enc.Hex.parse(iv_hex);
        var result = CryptoJS.AES.decrypt(b64_data, key, {iv: iv, mode: CryptoJS.mode.CBC, padding: CryptoJS.pad.NoPadding});
        return result.toString(CryptoJS.enc.Utf8).replace(/\0/g, '');
    }

var iv_128 = '31333537393234363830363534333231';
var key_256 = '3932547c57ecd5401242451d9c9cd65ad86ed213326904ec8368b3c4f3c79283';
var video_link = 'plWTCrMfJEQNjyuHww66hD1ymtfdt14mimNNy/7wGy0kIIhG84YOsj3J3Sui52yJfP4MqeyzQImStCFt2Hjug6hJVA4wxhDZhtSI82EOO7GrZ2dZ4XFtVrhPUG3D/OID5407/K7HxpbUojFlOKZ7G3DDzJYFWbfaLG32bwv0fCqgYkM5YdB6JXSqhnYD87U2';
var data = getLink(key_256,iv_128,video_link)
document.write(data);



// if (support_hls) {
//             var enc_hls_link = hls_video_link[video_id];
//             link_type = "application/x-mpegURL";
//             target_link = getLink(key_256, iv_128, enc_hls_link);
//         } else if (support_flash) {//Tam thoi bo qua flash
//             var enc_rtmp_link = rtmp_video_link[video_id];
//             target_link = getLink(key_256, iv_128, enc_rtmp_link);
//             link_type = "rtmp/mp4";
//         } else if (support_mpd) {
//             var enc_mpd_link = mpd_video_link[video_id];
//             link_type = "application/dash+xml";
//             target_link = getLink(key_256, iv_128, enc_mpd_link);
//         } else {
//             var enc_http_link = http_video_link[video_id];
//             target_link = getLink(key_256, iv_128, enc_http_link);
//             link_type = "video/mp4";
//         }