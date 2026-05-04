# ZDI-15-120: Moxa SoftCMS SStreamVideo Activex Control OpenForIPCamTest Method Stack Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-120
- **ZDI-CAN:** ZDI-CAN-2519
- **Date:** 2015-04-08
- **CVE:** CVE-2015-1000
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Moxa
- **Affected Products:** SoftCMS
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-120/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Moxa SoftCMS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the RTSPVIDEO.rtspvideoCtrl.1 ActiveX control. By passing an overly long string to the OpenForIPCamTest method's StrRtspPath parameter, an attacker can overflow a buffer on the stack. This vulnerability could be used to execute arbitrary code in the context of the browser.

## Additional Details

Moxa has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-097-01

## Disclosure Timeline

- 2015-02-05 - Vulnerability reported to vendor
- 2015-04-08 - Coordinated public release of advisory
