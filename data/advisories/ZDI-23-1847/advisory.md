# ZDI-23-1847: NETGEAR ProSAFE Network Management System saveNodeLabel Cross-Site Scripting Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1847
- **ZDI-CAN:** ZDI-CAN-21838
- **Date:** 2023-12-20
- **CVE:** CVE-2023-50231
- **CVSS:** 8.0
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** ProSAFE Network Management System
- **Credit:** Alex Williams of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1847/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of NETGEAR ProSAFE Network Management System. Minimal user interaction is required to exploit this vulnerability. The specific flaw exists within the saveNodeLabel method. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065901/Security-Advisory-for-Stored-Cross-Site-Scripting-on-the-NMS300-PSV-2023-0106

## Disclosure Timeline

- 2023-08-09 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory
