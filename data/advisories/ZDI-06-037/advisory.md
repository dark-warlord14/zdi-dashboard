# ZDI-06-037: America Online ICQ ActiveX Control Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-037
- **ZDI-CAN:** ZDI-CAN-102
- **Date:** 2006-11-06
- **CVE:** CVE-2006-5650
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** America Online
- **Affected Products:** ICQ
- **Credit:** Peter Vreugdenhil
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-037/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of AOL ICQ. User interaction is not required to exploit this vulnerability. The specific flaw exists in the DownloadAgent function of the ICQPhone.SipxPhoneManager ActiveX control with the following CLSID: 54BDE6EC-F42F-4500-AC46-905177444300 The vulnerable function takes a single URI argument of a file to download and execute under the context of the running user. A malicious ICQ avatar can be used as an exploitation vector, allowing attackers to exploit this vulnerability by simply messaging a target ICQ user.

## Additional Details

AOL has issued an update to correct this vulnerability on 10/31/2006. The update is automatically applied once connected to the ICQ service.

## Disclosure Timeline

- 2006-09-20 - Vulnerability reported to vendor
- 2006-11-06 - Coordinated public release of advisory
