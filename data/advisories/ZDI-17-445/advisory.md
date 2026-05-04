# ZDI-17-445: Cisco Prime Collaboration Provisioning ScriptMgr Servlet Authentication Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-445
- **ZDI-CAN:** ZDI-CAN-4343
- **Date:** 2017-06-26
- **CVE:** CVE-2017-6622
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Cisco
- **Affected Products:** Prime Collaboration Provisioning
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-445/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco Prime Collaboration Provisioning. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ScriptMgr servlet, which listens on TCP port 443 by default. A crafted request can bypass authentication for this resource. An attacker can leverage this vulnerability to execute arbitrary code under the context of root.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20170517-pcp1

## Disclosure Timeline

- 2017-02-01 - Vulnerability reported to vendor
- 2017-06-26 - Coordinated public release of advisory
