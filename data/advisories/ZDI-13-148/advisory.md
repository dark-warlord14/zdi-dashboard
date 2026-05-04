# ZDI-13-148: Oracle Java Runtime Environment AWT mediaLib Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-148
- **ZDI-CAN:** ZDI-CAN-1698
- **Date:** 2013-06-27
- **CVE:** CVE-2013-0809
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** axtaxt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-148/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within AWT mediaLib. The specific issue lies in the handling of width and height values. The width and height are multiplied against one value when allocating a buffer but is multiplied against another value when copying data into the buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/alert-cve-2013-1493-1915081.html

## Disclosure Timeline

- 2013-01-22 - Vulnerability reported to vendor
- 2013-06-27 - Coordinated public release of advisory
