# ZDI-13-035: EMC AlphaStor Device Manager 0x41 Command Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-035
- **ZDI-CAN:** ZDI-CAN-1703
- **Date:** 2013-02-14
- **CVE:** CVE-2013-0930
- **CVSS:** 7.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:C/I:C/A:C
- **Affected Vendors:** EMC
- **Affected Products:** AlphaStor
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-035/
## Vulnerability Details

This vulnerability potentially allows remote attackers to execute arbitrary code on vulnerable installations of EMC AlphaStor for EMC Networker. Authentication is not required to exploit this vulnerability. The specific flaw exists within Device Manager (rrobotd.exe) which listens by default on port 3000. When parsing the 0x41 command, the process creates a file path using user-supplied data which can exceed the size of the stack buffer used, allowing an attacker partial control over memory. An attacker may be able to leverage this vulnerability into remote execution of arbitrary code as SYSTEM.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://www.securityfocus.com/archive/1/525474

## Disclosure Timeline

- 2013-01-07 - Vulnerability reported to vendor
- 2013-02-14 - Coordinated public release of advisory
