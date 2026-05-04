# ZDI-12-139: SAP Crystal Reports crystalras.exe OBUnmarshal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-139
- **ZDI-CAN:** ZDI-CAN-1441
- **Date:** 2012-08-17
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** SAP
- **Affected Products:** Crystal Reports
- **Credit:** e6af8de8b1d4b2b6d5ba2610cbf9cd38
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-139/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SAP Crystal Reports. Authentication is not required to exploit this vulnerability. The flaw exists within the ebus-3-3-2-7.dll component which is used by the crystalras.exe service. This process listens on a random TCP port. When unmarshalling GIOP ORB encapsulated data the process invokes a memcpy constrained by a user controlled value. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

SAP has issued an update to correct this vulnerability. More details can be found at: https://service.sap.com/sap/support/notes/1662272

## Disclosure Timeline

- 2011-11-21 - Vulnerability reported to vendor
- 2012-08-17 - Coordinated public release of advisory
