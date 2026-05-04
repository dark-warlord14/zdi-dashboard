# ZDI-13-034: EMC AlphaStor Device Manager 0x75 Command Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-034
- **ZDI-CAN:** ZDI-CAN-1702
- **Date:** 2013-02-14
- **CVE:** CVE-2013-0929
- **CVSS:** 7.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:C/I:C/A:C
- **Affected Vendors:** EMC
- **Affected Products:** AlphaStor
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-034/
## Vulnerability Details

This vulnerability potentially allows remote attackers to execute arbitrary code on vulnerable installations of EMC AlphaStor for EMC Networker. Authentication is not required to exploit this vulnerability. The specific flaw exists within Device Manager (rrobotd.exe) which listens by default on port 3000. When parsing the 0x75 command, the process uses unfiltered user supplied data as a format string, allowing an attacker partial control over memory. Should an attacker leverage this vulnerability into remote execution of arbitrary code, that code would run with SYSTEM privileges.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://www.securityfocus.com/archive/1/525362/30/0/threaded

## Disclosure Timeline

- 2012-12-10 - Vulnerability reported to vendor
- 2013-02-14 - Coordinated public release of advisory
