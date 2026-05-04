# ZDI-18-299: Hewlett Packard Enterprise Universal CMDB Product Installation File Access Control Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-299
- **ZDI-CAN:** ZDI-CAN-5487
- **Date:** 2018-04-12
- **CVE:** CVE-2018-6491
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Universal CMDB
- **Credit:** TrendyTofu - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-299/
## Vulnerability Details

This vulnerability allows local attackers to escalate privilege on vulnerable installations of Hewlett Packard Enterprise Universal CMDB. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within an access control set with insufficient privileges during the installation of the product. An attacker can leverage this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://softwaresupport.hpe.com/document/-/facetsearch/document/KM03141180

## Disclosure Timeline

- 2017-12-15 - Vulnerability reported to vendor
- 2018-04-12 - Coordinated public release of advisory
- 2018-04-12 - Advisory Updated
