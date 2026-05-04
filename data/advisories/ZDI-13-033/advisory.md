# ZDI-13-033: EMC AlphaStor Device Manager 0x75 Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-033
- **ZDI-CAN:** ZDI-CAN-1701
- **Date:** 2013-02-14
- **CVE:** CVE-2013-0928
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** EMC
- **Affected Products:** AlphaStor
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-033/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of EMC AlphaStor for EMC Networker. Authentication is not required to exploit this vulnerability. The specific flaw exists within Device Manager (rrobotd.exe) which listens by default on port 3000. When parsing the 0x75 command, the process does not properly filter the user supplied data allowing for arbitrary command injection and execution. A remote attacker can abuse this to execute remote code under the context of the SYSTEM user.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://www.securityfocus.com/archive/1/525362/30/0/threaded

## Disclosure Timeline

- 2012-12-10 - Vulnerability reported to vendor
- 2013-02-14 - Coordinated public release of advisory
