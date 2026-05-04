# ZDI-25-858: Axis Communications Autodesk Plugin AzureBlobRestAPI axiscontentfiles Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-858
- **ZDI-CAN:** ZDI-CAN-25774
- **Date:** 2025-08-21
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Axis Communications
- **Affected Products:** Autodesk Plugin
- **Credit:** Nitesh Surana (@_niteshsurana) of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-858/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Axis Communications Autodesk Plugin. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of a cloud resource. The issue results from allowing unauthorized access to a storage account. An attacker can leverage this vulnerability to execute code on systems dependent on the cloud resource.

## Additional Details

Fixed in version 25.3.718 ( https://www.axis.com/support/tools/axis-plugin-for-autodesk-revit )

## Disclosure Timeline

- 2025-03-11 - Vulnerability reported to vendor
- 2025-08-21 - Coordinated public release of advisory
- 2025-08-21 - Advisory Updated
