# ZDI-15-572: Tibbo AggreGate SCADA/HMI Apache Axis AdminService Arbitrary Class Instantiation Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-572
- **ZDI-CAN:** ZDI-CAN-3135
- **Date:** 2015-11-20
- **CVE:** CVE-2015-7913
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Tibbo
- **Affected Products:** AggreGate SCADA/HMI
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-572/
## Vulnerability Details

This vulnerability allows attackers to elevate privileges on vulnerable installations of Tibbo AggreGate SCADA/HMI. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Windows service "AggreGate Server Service" (ag_server_service.exe). It offers the default Apache Axis AdminService, which can be contacted by local users to publish arbitrary classes via the 'deployment' method. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Tibbo has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-323-01

## Disclosure Timeline

- 2015-08-24 - Vulnerability reported to vendor
- 2015-11-20 - Coordinated public release of advisory
