# ZDI-25-271: Cisco IOS XE SNMP OID Handling Out-Of-Bounds Read Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-271
- **ZDI-CAN:** ZDI-CAN-25577
- **Date:** 2025-05-01
- **CVE:** CVE-2025-20172
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** Cisco
- **Affected Products:** IOS
- **Credit:** leg00m
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-271/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Cisco IOS XE. Authentication is required to exploit this vulnerability. The specific flaw exists within the SNMP service, which listens on UDP port 161 by default. The issue results from the lack of proper validation of user-supplied data, which can result in a read before the start of an allocated array. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snmp-dos-sdxnSUcW

## Disclosure Timeline

- 2024-10-15 - Vulnerability reported to vendor
- 2025-05-01 - Coordinated public release of advisory
- 2025-05-01 - Advisory Updated
