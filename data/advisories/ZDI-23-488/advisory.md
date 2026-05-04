# ZDI-23-488: Oracle ODP.NET Managed Driver Improper Certificate Validation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-488
- **ZDI-CAN:** ZDI-CAN-19864
- **Date:** 2023-05-01
- **CVE:** CVE-2023-21893
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** ODP.NET Managed Driver
- **Credit:** Georg Jung
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-488/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to compromise transport security on affected installations of Oracle ODP.NET Managed Driver. An attacker must first obtain the ability to intercept and alter network traffic in order to exploit this vulnerability. The specific flaw exists within the ValidateRemoteCertificate function. The issue results from the lack of proper validation of the server certificate. An attacker can leverage this vulnerability to disclose communications between the client and the server or to insert fraudulent server responses.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujan2023.html

## Disclosure Timeline

- 2023-02-08 - Vulnerability reported to vendor
- 2023-05-01 - Coordinated public release of advisory
