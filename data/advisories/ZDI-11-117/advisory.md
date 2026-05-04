# ZDI-11-117: McAfee Firewall Reporter GeneralUtilities.pm isValidClient Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-117
- **ZDI-CAN:** ZDI-CAN-938
- **Date:** 2011-04-11
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** McAfee
- **Affected Products:** Firewall Reporter
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-117/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of McAfee Firewall Reporter. Authentication is not required to exploit this vulnerability. The specific flaw exists within the code responsible for authenticating users. The GernalUtilities.pm file contains code to validate sessions by parsing cookie values without sanitization. The faulty logic simply checks for the existence of a particular file, without verifying its contents. By using a directory traversal technique an attacker can point the cgisess cookie value to an arbitrary file that exists on the server and thus bypass authentication.

## Additional Details

Fixed February 9, 2011 Bulletin modified April 11, 2011: https://kc.mcafee.com/corporate/index?page=content&id=SB10015

## Disclosure Timeline

- 2010-09-22 - Vulnerability reported to vendor
- 2011-04-11 - Coordinated public release of advisory
