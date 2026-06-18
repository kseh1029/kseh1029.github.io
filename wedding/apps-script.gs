// ================================================
// 부산 그랜드 모먼트 웨딩 - Google Apps Script
// RSVP + 사진 업로드 (Google Drive)
// ================================================

const SHEET_NAME = 'RSVP';
const PHOTO_FOLDER_NAME = 'Wedding Photo';

/* ── GET: 업로드된 사진 목록 반환 (JSONP 지원) ── */
function doGet(e) {
  const callback = e && e.parameter && e.parameter.callback;
  try {
    const folder = getOrCreatePhotoFolder();
    const files = folder.getFiles();
    const photos = [];
    while (files.hasNext()) {
      const file = files.next();
      photos.push({
        id:       file.getId(),
        uploader: file.getDescription() || '',
        thumb:    'https://drive.google.com/thumbnail?id=' + file.getId() + '&sz=w600',
        date:     file.getDateCreated().toISOString(),
      });
    }
    photos.sort(function(a, b) { return new Date(b.date) - new Date(a.date); });
    const json = JSON.stringify({ status: 'ok', photos: photos });
    if (callback) {
      return ContentService.createTextOutput(callback + '(' + json + ')')
        .setMimeType(ContentService.MimeType.JAVASCRIPT);
    }
    return ContentService.createTextOutput(json)
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    const json = JSON.stringify({ status: 'error', msg: err.message });
    if (callback) {
      return ContentService.createTextOutput(callback + '(' + json + ')')
        .setMimeType(ContentService.MimeType.JAVASCRIPT);
    }
    return ContentService.createTextOutput(json)
      .setMimeType(ContentService.MimeType.JSON);
  }
}

/* ── POST: RSVP 또는 사진 업로드 ── */
function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);

    /* 사진 업로드 */
    if (data.type === 'photo') {
      const folder = getOrCreatePhotoFolder();
      const imageData = data.image.indexOf(',') !== -1
        ? data.image.split(',')[1]
        : data.image;
      const blob = Utilities.newBlob(
        Utilities.base64Decode(imageData),
        data.mimeType || 'image/jpeg',
        data.filename || ('photo_' + Date.now() + '.jpg')
      );
      const file = folder.createFile(blob);
      file.setDescription(data.uploader || '');
      file.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);
      return ContentService
        .createTextOutput(JSON.stringify({
          status: 'ok',
          id:     file.getId(),
          thumb:  'https://drive.google.com/thumbnail?id=' + file.getId() + '&sz=w600',
        }))
        .setMimeType(ContentService.MimeType.JSON);
    }

    /* RSVP */
    const sheet = getOrCreateSheet();
    sheet.appendRow([
      data.timestamp || new Date().toLocaleString('ko-KR', { timeZone: 'Asia/Seoul' }),
      data.name      || '',
      data.attendance|| '',
      data.count     || 0,
      data.message   || '',
    ]);
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'ok' }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', msg: err.message }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function getOrCreateSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    sheet.appendRow(['제출 시각', '이름', '참석 여부', '인원 수 (식권)', '메시지']);
    sheet.getRange(1, 1, 1, 5).setFontWeight('bold').setBackground('#c9a96e').setFontColor('white');
    sheet.setColumnWidth(1, 180);
    sheet.setColumnWidth(2, 100);
    sheet.setColumnWidth(3, 100);
    sheet.setColumnWidth(4, 120);
    sheet.setColumnWidth(5, 300);
    sheet.setFrozenRows(1);
  }
  return sheet;
}

function getOrCreatePhotoFolder() {
  const folders = DriveApp.getFoldersByName(PHOTO_FOLDER_NAME);
  if (folders.hasNext()) return folders.next();
  return DriveApp.createFolder(PHOTO_FOLDER_NAME);
}

function testSetup() {
  const sheet = getOrCreateSheet();
  sheet.appendRow([
    new Date().toLocaleString('ko-KR', { timeZone: 'Asia/Seoul' }),
    '테스트', '참석', 2, '테스트 메시지입니다',
  ]);
  Logger.log('✅ 시트 설정 완료: ' + sheet.getSheetId());
}
