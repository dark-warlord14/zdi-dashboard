# ZDI-13-288: (Pwn2Own) Adobe Flash RTMP Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-288
- **ZDI-CAN:** ZDI-CAN-1826
- **Date:** 2015-09-18
- **CVE:** CVE-2013-2555
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** VUPEN Security [ http://www.vupen.com ]
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-288/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of RTMP data. The issue lies in the ability to exchange objects, allowing for an object confusion vulnerability. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb13-11.html

## Disclosure Timeline

- 2013-07-13 - Vulnerability reported to vendor
- 2015-09-18 - Coordinated public release of advisory
