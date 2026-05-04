# ZDI-25-1182: LibreNMS Alert Rule API Cross-Site Scripting Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1182
- **ZDI-CAN:** ZDI-CAN-28575
- **Date:** 2025-12-23
- **CVE:** CVE-2025-68614
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** LibreNMS
- **Affected Products:** LibreNMS
- **Credit:** Simon Humbert of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1182/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary script on affected installations of LibreNMS. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of the name parameter provided to the rules endpoint. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of arbitrary script. An attacker can leverage this vulnerability to execute script in the context of a target user.

## Additional Details

LibreNMS has issued an update to correct this vulnerability. More details can be found at: https://github.com/librenms/librenms/security/advisories/GHSA-c89f-8g7g-59wj

## Disclosure Timeline

- 2025-11-18 - Vulnerability reported to vendor
- 2025-12-23 - Coordinated public release of advisory
- 2025-12-23 - Advisory Updated
