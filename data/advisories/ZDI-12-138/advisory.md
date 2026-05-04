# ZDI-12-138: SAP Business Objects Financial Consolidation CtAppReg.dll username Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-138
- **ZDI-CAN:** ZDI-CAN-1430
- **Date:** 2012-08-17
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** SAP
- **Affected Products:** Business Objects Financial Consolidation
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-138/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SAP Business Objects Financial Consolidation. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within CtAppReg.dll. In the Check function, there is a vulnerability in the handling of the username parameter. If an overly long string is used as the username, it can overwrite heap memory. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

SAP has issued an update to correct this vulnerability. More details can be found at: https://service.sap.com/sap/support/notes/1685003

## Disclosure Timeline

- 2011-11-04 - Vulnerability reported to vendor
- 2012-08-17 - Coordinated public release of advisory
