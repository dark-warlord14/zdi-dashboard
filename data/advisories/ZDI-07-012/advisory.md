# ZDI-07-012: Yahoo! Messenger AudioConf ActiveX Control Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-012
- **ZDI-CAN:** ZDI-CAN-110
- **Date:** 2007-04-03
- **CVE:** CVE-2007-1680
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Yahoo!
- **Affected Products:** Yahoo! Messenger
- **Credit:** Peter Vreugdenhil
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-012/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Yahoo Messenger. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the ActiveX control Yahoo.AudioConf: DLL: yacscom.dll CLSID: 2B323CD9-50E3-11D3-9466-00A0C9700498 When large values are specified for the 'socksHostname' and 'hostname' properties, and the createAndJoinConference() method is called, a stack overflow occurs. Exploitation can result in code execution under the context of the current user.

## Additional Details

Yahoo! has issued an update to correct this vulnerability. More details can be found at: http://messenger.yahoo.com/security_update.php?id=031207

## Disclosure Timeline

- 2006-10-27 - Vulnerability reported to vendor
- 2007-04-03 - Coordinated public release of advisory
