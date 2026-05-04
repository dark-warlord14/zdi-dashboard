# ZDI-25-276: Cisco IOS XE SNMP GET-NEXT cilmCurrentImageLevel Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-276
- **ZDI-CAN:** ZDI-CAN-25019
- **Date:** 2025-05-01
- **CVE:** CVE-2025-20174
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** IOS
- **Credit:** leg00m
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-276/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Cisco IOS XE. Authentication is required to exploit this vulnerability. The specific flaw exists within the SNMP service, which listens on UDP port 161 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snmp-dos-sdxnSUcW

## Disclosure Timeline

- 2024-10-08 - Vulnerability reported to vendor
- 2025-05-01 - Coordinated public release of advisory
- 2025-05-01 - Advisory Updated
