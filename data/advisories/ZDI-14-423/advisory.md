# ZDI-14-423: Honeywell OPOS Suite HWOPOSSCANNER.ocx Open Method Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-423
- **ZDI-CAN:** ZDI-CAN-2528
- **Date:** 2014-12-11
- **CVE:** CVE-2014-8269
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Honeywell
- **Affected Products:** OPOS Suite
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-423/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Honeywell OPOS Suite. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the HWOPOSSCANNER.ocx. The control does not check the length of an attacker-supplied string to the Open method before copying it into a fixed length buffer on the stack. This allows an attacker to execute arbitrary code in the context of the browser process.

## Additional Details

Honeywell has issued an update to correct this vulnerability. More details can be found at: http://www.kb.cert.org/vuls/id/659684

## Disclosure Timeline

- 2014-10-16 - Vulnerability reported to vendor
- 2014-12-11 - Coordinated public release of advisory
