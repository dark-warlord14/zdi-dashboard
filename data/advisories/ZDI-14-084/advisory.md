# ZDI-14-084: (Pwn2Own) Mozilla Firefox ArrayBuffer Out-Of-Bounds Read/Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-084
- **ZDI-CAN:** ZDI-CAN-2220
- **Date:** 2014-04-11
- **CVE:** CVE-2014-1513
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-084/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of ArrayBuffer objects. The issue lies in improper handling when neutering an ArrayBuffer object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2014/mfsa2014-31.html

## Disclosure Timeline

- 2014-03-12 - Vulnerability reported to vendor
- 2014-04-11 - Coordinated public release of advisory
