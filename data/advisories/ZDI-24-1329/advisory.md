# ZDI-24-1329: Axis Communications Autodesk Plugin AxisAddin axisapphelpfiles Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1329
- **ZDI-CAN:** ZDI-CAN-25281
- **Date:** 2024-10-08
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Axis Communications
- **Affected Products:** Autodesk Plugin
- **Credit:** Nitesh Surana (@_niteshsurana) of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1329/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Axis Communications Autodesk Plugin. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of a cloud resource. The issue results from allowing unauthorized access to a storage account. An attacker can leverage this vulnerability to execute code on systems dependent on the cloud resource.

## Additional Details

Fixed in version 25.3.711 ( https://www.axis.com/support/tools/axis-plugin-for-autodesk-revit )

## Disclosure Timeline

- 2024-09-03 - Vulnerability reported to vendor
- 2024-10-08 - Coordinated public release of advisory
- 2024-10-08 - Advisory Updated
