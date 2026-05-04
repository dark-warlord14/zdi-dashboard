# ZDI-12-028: IBM Rational Rhapsody BBFlashBack.FBRecorder.1 Control Multiple Remote Code Execution Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-12-028
- **ZDI-CAN:** ZDI-CAN-1288
- **Date:** 2012-02-08
- **CVE:** CVE-2011-1392
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Rational Rhapsody
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-028/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Rational Rhapsody. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaws exists within BB FlashBack Recorder.dll. The Filename property is vulnerable to directory traversal via the Start() method. PauseAndSave() is also vulnerable to directory traversal via its nextfilename parameter. InsertMarker() and InsertSoundToFBRAtMarker() have parameters that are vulnerable to script injection and can be combined with the previously mentioned vulnerabilities to achieve remote arbitrary code execution.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www.ibm.com/support/docview.wss?uid=swg21576352

## Disclosure Timeline

- 2011-06-29 - Vulnerability reported to vendor
- 2012-02-08 - Coordinated public release of advisory
