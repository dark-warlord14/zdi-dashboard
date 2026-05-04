# ZDI-10-232: Cisco ICM Setup Manager Agent.exe HandleUpgradeAll Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-232
- **ZDI-CAN:** ZDI-CAN-796
- **Date:** 2010-11-07
- **CVE:** CVE-2010-3040
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Cisco
- **Affected Products:** Unified Intelligent Contact Management
- **Credit:** sb
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-232/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco ICM. Authentication is not required to exploit this vulnerability. The flaw exists within the Agent.exe component which listens by default on TCP port 40078. When processing the HandleUpgradeAll packet type an unchecked copy of user supplied data is performed into a stack-based buffer of a controlled size. Successful exploitation of this vulnerability leads to remote code execution under the context of the SYSTEM user.

## Additional Details

Cisco has acknowledged this vulnerability in an Intellishield alert. http://tools.cisco.com/security/center/viewAlert.x?alertId=21726

## Disclosure Timeline

- 2010-06-01 - Vulnerability reported to vendor
- 2010-11-07 - Coordinated public release of advisory
