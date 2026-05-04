# ZDI-19-996: Dell EMC Storage Monitoring and Reporting Java RMI Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-996
- **ZDI-CAN:** ZDI-CAN-8929
- **Date:** 2019-11-26
- **CVE:** CVE-2019-18580
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Dell
- **Affected Products:** EMC Storage Monitoring and Reporting
- **Credit:** tint0 of Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-996/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Dell EMC Storage Monitoring and Reporting. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Java RMI service, which listens on TCP port 52569 by default. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Dell has issued an update to correct this vulnerability. More details can be found at: https://www.dell.com/support/security/es-es/details/538977/DSA-2019-176-Dell-EMC-Storage-Monitoring-and-Reporting-SMR-Java-RMI-Deserialization-of-Untruste

## Disclosure Timeline

- 2019-07-25 - Vulnerability reported to vendor
- 2019-11-26 - Coordinated public release of advisory
