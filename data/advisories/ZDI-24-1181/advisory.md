# ZDI-24-1181: Axis Communications Autodesk Plugin Exposure of Sensitive Information Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1181
- **ZDI-CAN:** ZDI-CAN-24830
- **Date:** 2024-08-23
- **CVE:** N/A
- **CVSS:** 7.6
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:H
- **Affected Vendors:** Axis Communications
- **Affected Products:** Autodesk Plugin
- **Credit:** Nitesh Surana (@_niteshsurana) of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1181/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected services of Axis Communications Autodesk Plugin. Authentication is not required to exploit this vulnerability. The specific flaw exists within the AzureBlobRestAPI.dll module. The issue results from exposed credentials. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Fixed in plugin Version 25.3.710 ( https://www.axis.com/support/tools/axis-plugin-for-autodesk-revit#download-block )

## Disclosure Timeline

- 2024-07-16 - Vulnerability reported to vendor
- 2024-08-23 - Coordinated public release of advisory
- 2024-08-23 - Advisory Updated
