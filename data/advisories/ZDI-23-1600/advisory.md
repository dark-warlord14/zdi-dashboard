# ZDI-23-1600: Siemens SINEMA Server sysLocation Cross-Site Scripting Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1600
- **ZDI-CAN:** ZDI-CAN-19823
- **Date:** 2023-11-14
- **CVE:** CVE-2023-35796
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** SINEMA Server
- **Credit:** Andreas Finstad
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1600/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens SINEMA Server. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of SNMP sysLocation OID. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://cert-portal.siemens.com/productcert/html/ssa-594373.html

## Disclosure Timeline

- 2023-04-13 - Vulnerability reported to vendor
- 2023-11-14 - Coordinated public release of advisory
