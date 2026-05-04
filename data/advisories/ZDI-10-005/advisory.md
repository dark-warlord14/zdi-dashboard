# ZDI-10-005: RealNetworks RealPlayer ASMRulebook Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-005
- **ZDI-CAN:** ZDI-CAN-252
- **Date:** 2010-01-21
- **CVE:** CVE-2009-4241
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-005/
## Vulnerability Details

This vulnerability allows remote attackers to execute code on vulnerable installations of RealPlayer. User interaction is required in that a user must open a malicious file or visit a malicious web site. The specific flaw exists during the parsing of files with improperly defined ASMRuleBook structures. A controllable memory allocation allows for an attacker to corrupt heap memory. Attacker controlled data from the corrupt heap is later used as an object pointer which can be leveraged to execute arbitrary code in the context of the currently logged in user.

## Disclosure Timeline

- 2007-11-07 - Vulnerability reported to vendor
- 2010-01-21 - Coordinated public release of advisory
- 2021-07-15 - Advisory Updated
