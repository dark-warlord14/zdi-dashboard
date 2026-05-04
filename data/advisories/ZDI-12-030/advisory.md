# ZDI-12-030: IBM Rational Rhapsody BBFlashBack.Recorder.1 TestCompatibilityRecordMode Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-030
- **ZDI-CAN:** ZDI-CAN-1246
- **Date:** 2012-02-08
- **CVE:** CVE-2011-1388
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Rational Rhapsody
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-030/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Rational Rhapsody. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within BB FlashBack Recorder.dll. Uninitialized pointers may be passed as arguments to TestCompatibilityRecordMode() which allows a remote attacker to reliably corrupt controlled memory regions. This behavior can be exploited to remotely execute arbitrary code in the context of the user running the browser.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www.ibm.com/support/docview.wss?uid=swg21576352

## Disclosure Timeline

- 2011-06-29 - Vulnerability reported to vendor
- 2012-02-08 - Coordinated public release of advisory
