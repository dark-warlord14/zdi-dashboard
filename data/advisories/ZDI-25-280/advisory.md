# ZDI-25-280: Cisco IOS XE SNMP GET-NEXT ciscoFlashChipCode Unexpected Sign Extension Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-280
- **ZDI-CAN:** ZDI-CAN-25024
- **Date:** 2025-05-01
- **CVE:** CVE-2025-20170
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** IOS
- **Credit:** leg00m
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-280/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Cisco IOS XE. Authentication is required to exploit this vulnerability. The specific flaw exists within the SNMP service, which listens on UDP port 161 by default. The issue results from the lack of proper validation of user-supplied data, which can result in an unexpected sign extension. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snmp-dos-sdxnSUcW

## Disclosure Timeline

- 2024-10-08 - Vulnerability reported to vendor
- 2025-05-01 - Coordinated public release of advisory
- 2025-05-01 - Advisory Updated
