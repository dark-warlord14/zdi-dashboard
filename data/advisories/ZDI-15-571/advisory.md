# ZDI-15-571: Tibbo AggreGate SCADA/HMI Server Service uploadDirectory Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-571
- **ZDI-CAN:** ZDI-CAN-3134
- **Date:** 2015-11-20
- **CVE:** CVE-2015-7912
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Tibbo
- **Affected Products:** AggreGate SCADA/HMI
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-571/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Tibbo AggreGate SCADA/HMI. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Windows service "AggreGate Server Service" (ag_server_service.exe). Through the "Ice Faces" servlet it is possible to upload arbitrary Java code inside an accessible web path, due to functionality which allows importation of application properties through uploaded xml files. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Tibbo has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-323-01

## Disclosure Timeline

- 2015-08-24 - Vulnerability reported to vendor
- 2015-11-20 - Coordinated public release of advisory
